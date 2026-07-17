from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_PLUGIN = ROOT / "plugins/codex/project-harness"
CLAUDE_PLUGIN = ROOT / "plugins/claude-code/project-harness"


class RepositoryContractTests(unittest.TestCase):
    def test_setup_creates_project_layer_without_forcing_a_journal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "project"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "shared/scripts/setup-project.py"),
                    "--project-root",
                    str(target),
                    "--fast",
                    "true",
                    "--full",
                    "true",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "CLAUDE.md").is_file())
            self.assertEqual(list((target / "docs/plans/active").iterdir()), [])

    def test_duplicate_task_registry_is_retired(self) -> None:
        self.assertFalse((ROOT / "memory/active-tasks.json").exists())
        self.assertFalse((ROOT / "shared/templates/active-tasks.template.json").exists())

    def test_docs_syncer_configuration_is_retired(self) -> None:
        self.assertFalse((ROOT / ".codex/agents/docs_syncer.toml").exists())
        candidates = [ROOT / "AGENTS.md", ROOT / ".harness.toml", ROOT / "docs/agent/index.md"]
        for path in candidates:
            self.assertNotIn("docs_syncer", path.read_text(encoding="utf-8"))

    def test_root_agents_is_a_small_router_not_a_forced_full_load(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        line_count = len(agents.splitlines())
        self.assertGreaterEqual(line_count, 60)
        self.assertLessEqual(line_count, 100)
        self.assertIn("Load only modules", agents)
        self.assertNotIn("PROJECT_CONTEXT.md", agents)
        self.assertNotRegex(agents.lower(), r"read (all|every) .*context")

    def test_claude_rules_are_path_scoped_and_not_permanent_context(self) -> None:
        claude = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertIn("@AGENTS.md", claude)
        rules_root = ROOT / ".claude/rules"
        for rule in rules_root.rglob("*.md") if rules_root.is_dir() else []:
            text = rule.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), rule)
            self.assertRegex(text, r"(?m)^paths:\s*$")

    def test_codex_and_claude_plugin_manifests_have_valid_package_shape(self) -> None:
        codex_manifest = json.loads(
            (CODEX_PLUGIN / ".codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        claude_manifest = json.loads(
            (CLAUDE_PLUGIN / ".claude-plugin/plugin.json").read_text(encoding="utf-8")
        )
        for manifest in (codex_manifest, claude_manifest):
            self.assertEqual(manifest["name"], "project-harness")
            self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
            self.assertTrue(manifest["description"])
        for plugin in (CODEX_PLUGIN, CLAUDE_PLUGIN):
            self.assertTrue((plugin / "hooks/hooks.json").is_file())
            self.assertEqual(
                {path.name for path in (plugin / "skills").iterdir() if path.is_dir()},
                {"setup-project", "task-memory", "finish-task"},
            )
            hooks = json.loads((plugin / "hooks/hooks.json").read_text(encoding="utf-8"))["hooks"]
            self.assertEqual(set(hooks), {"SessionStart", "PreCompact"})
            self.assertNotIn("Stop", hooks)

    def test_repository_has_no_machine_local_absolute_links(self) -> None:
        forbidden = ("/" + "Users/", "/" + "home/", "file" + "://")
        offenders: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if any(token in text for token in forbidden):
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [])

    def test_git_diff_check_passes(self) -> None:
        completed = subprocess.run(
            ["git", "diff", "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
