from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_ROOT = REPO_ROOT / "shared" / "scripts"
sys.path.insert(0, str(SCRIPT_ROOT))

from harness_core import (  # noqa: E402
    HarnessError,
    archive_journal,
    context_impact,
    finish_problems,
    git_changed_paths,
    load_config,
    record_verification,
    render_restore,
    resolve_journal,
    restore_payload,
    run_commands,
)


def config_text(fast: list[str] | None = None, full: list[str] | None = None) -> str:
    return "\n".join(
        [
            "version = 1",
            'task_root = "docs/plans"',
            'context_index = "docs/agent/index.md"',
            "",
            "[verification]",
            f"fast = {json.dumps(fast or ['true'])}",
            f"full = {json.dumps(full or ['true'])}",
            "",
        ]
    )


class HarnessFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        (self.root / ".harness.toml").write_text(config_text(), encoding="utf-8")
        (self.root / "docs/plans/active").mkdir(parents=True)
        (self.root / "docs/plans/completed").mkdir(parents=True)
        (self.root / "docs/agent").mkdir(parents=True)
        (self.root / "docs/agent/index.md").write_text("# Index\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def journal(
        self,
        task_id: str,
        *,
        done: bool = False,
        verification: str = "pending",
        diff_review: str = "pending",
        context_review: str = "pending",
        context_notes: str = "",
    ) -> Path:
        target = self.root / "docs/plans/active" / task_id
        target.mkdir()
        marker = "x" if done else " "
        (target / "task_plan.md").write_text(
            "\n".join(
                [
                    f"# Task Plan: {task_id}",
                    "",
                    "## Goal",
                    "",
                    f"Deliver {task_id}.",
                    "",
                    "## Done When",
                    "",
                    f"- [{marker}] Observable criterion",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        (target / "findings.md").write_text("# Findings\n", encoding="utf-8")
        (target / "progress.md").write_text(
            "\n".join(
                [
                    "# Progress",
                    "",
                    "## Latest Checkpoint",
                    "",
                    "- Current focus: implement the core",
                    "- Next action: run verification",
                    "- Blocked on: nothing",
                    "- Last meaningful update: checkpoint saved",
                    "",
                    "## Session Log",
                    "",
                    "SECRET_LOW_SIGNAL_LOG_ENTRY",
                    "",
                    "## Verification Evidence",
                    "",
                    f"- Result: {verification}",
                    "",
                    "## Diff Review",
                    "",
                    f"- Result: {diff_review}",
                    "- Notes: reviewed",
                    "",
                    "## Project Context Review",
                    "",
                    f"- Result: {context_review}",
                    "- Modules:",
                    f"- Notes: {context_notes}",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return target


class PlanResolutionTests(HarnessFixture):
    def test_config_rejects_boolean_version(self) -> None:
        (self.root / ".harness.toml").write_text("version = true\n", encoding="utf-8")
        with self.assertRaisesRegex(HarnessError, "unsupported"):
            load_config(self.root)

    def test_two_tasks_have_isolated_journal_directories(self) -> None:
        first = self.journal("task-a")
        second = self.journal("task-b")
        self.assertNotEqual(first, second)
        self.assertEqual({path.name for path in first.iterdir()}, {"task_plan.md", "findings.md", "progress.md"})
        self.assertEqual({path.name for path in second.iterdir()}, {"task_plan.md", "findings.md", "progress.md"})

    def test_plan_id_environment_selects_exact_task(self) -> None:
        self.journal("task-a")
        self.journal("task-b")
        config = load_config(self.root)
        previous = os.environ.get("PLAN_ID")
        os.environ["PLAN_ID"] = "task-b"
        try:
            self.assertEqual(resolve_journal(config).task_id, "task-b")
        finally:
            if previous is None:
                os.environ.pop("PLAN_ID", None)
            else:
                os.environ["PLAN_ID"] = previous

    def test_unique_active_task_restores_automatically(self) -> None:
        self.journal("only-task")
        self.assertEqual(resolve_journal(load_config(self.root)).task_id, "only-task")

    def test_multiple_active_tasks_without_plan_id_fail_clearly(self) -> None:
        self.journal("task-a")
        self.journal("task-b")
        with self.assertRaisesRegex(HarnessError, "set PLAN_ID explicitly"):
            resolve_journal(load_config(self.root))

    def test_no_active_task_does_not_force_a_journal(self) -> None:
        self.assertIsNone(resolve_journal(load_config(self.root)))


class RestoreAndCheckpointTests(HarnessFixture):
    def test_lifecycle_hooks_are_silent_without_harness_config(self) -> None:
        empty = self.root / "unconfigured"
        empty.mkdir()
        for script in ("restore-plan.py", "pre-compact.py"):
            completed = subprocess.run(
                [sys.executable, str(SCRIPT_ROOT / script), "--hook"],
                input=json.dumps({"cwd": str(empty)}),
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(completed.stdout, "")

    def test_session_restore_contains_checkpoint_not_full_log(self) -> None:
        self.journal("restore-me")
        config = load_config(self.root)
        payload = restore_payload(resolve_journal(config), self.root)
        rendered = render_restore(payload)
        self.assertIn("implement the core", rendered)
        self.assertIn("run verification", rendered)
        self.assertNotIn("SECRET_LOW_SIGNAL_LOG_ENTRY", rendered)

    def test_precompact_emits_non_blocking_checkpoint_reminder(self) -> None:
        self.journal("compact-me")
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT_ROOT / "pre-compact.py"),
                "--hook",
                "--project-root",
                str(self.root),
                "--plan-id",
                "compact-me",
            ],
            input=json.dumps({"cwd": str(self.root), "hook_event_name": "PreCompact"}),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)
        output = json.loads(completed.stdout)
        self.assertTrue(output["continue"])
        self.assertIn("Latest Checkpoint", output["systemMessage"])

    def test_progress_template_has_checkpoint_without_realtime_task_status(self) -> None:
        template = (REPO_ROOT / "shared/templates/progress.md").read_text(encoding="utf-8")
        self.assertIn("## Latest Checkpoint", template)
        self.assertNotRegex(template.lower(), r"task status|status: (running|waiting|complete)")


class VerifiedCompletionTests(HarnessFixture):
    def test_changed_paths_work_before_first_commit(self) -> None:
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        staged = self.root / "staged.txt"
        staged.write_text("staged\n", encoding="utf-8")
        subprocess.run(["git", "add", "staged.txt"], cwd=self.root, check=True)
        (self.root / "untracked.txt").write_text("untracked\n", encoding="utf-8")

        paths = git_changed_paths(self.root)

        self.assertIn("staged.txt", paths)
        self.assertIn("untracked.txt", paths)

    def test_context_impact_suggests_existing_scoped_modules(self) -> None:
        for module in ("architecture.md", "distribution.md", "verification.md"):
            (self.root / "docs/agent" / module).write_text(f"# {module}\n", encoding="utf-8")
        impact = context_impact(
            [
                "AGENTS.md",
                "shared/scripts/verify-task.py",
                "plugins/codex/project-harness/.codex-plugin/plugin.json",
            ],
            load_config(self.root),
        )
        modules = {item["module"] for item in impact["candidates"]}
        self.assertEqual(modules, {"architecture.md", "distribution.md", "verification.md"})

    def test_unchecked_done_when_blocks_archive(self) -> None:
        self.journal(
            "incomplete",
            verification="passed",
            diff_review="passed",
            context_review="no-impact",
        )
        journal = resolve_journal(load_config(self.root), "incomplete")
        self.assertIn("unchecked", " ".join(finish_problems(journal)))

    def test_failed_verification_is_recorded_and_blocks_finish(self) -> None:
        self.journal("verify-fail", done=True, diff_review="passed", context_review="no-impact")
        (self.root / ".harness.toml").write_text(
            config_text(full=[f'{sys.executable} -c "import sys; sys.exit(7)"']),
            encoding="utf-8",
        )
        config = load_config(self.root)
        journal = resolve_journal(config, "verify-fail")
        results = run_commands(config, "full")
        self.assertFalse(record_verification(journal, "full", results))
        self.assertIn("Verification Evidence", " ".join(finish_problems(journal)))

    def test_unhandled_context_impact_blocks_archive(self) -> None:
        self.journal("context-pending", done=True, verification="passed", diff_review="passed")
        journal = resolve_journal(load_config(self.root), "context-pending")
        self.assertIn("Project Context Review", " ".join(finish_problems(journal)))

    def test_completed_task_moves_to_completed(self) -> None:
        self.journal(
            "ready",
            done=True,
            verification="passed",
            diff_review="passed",
            context_review="no-impact",
        )
        config = load_config(self.root)
        journal = resolve_journal(config, "ready")
        destination = archive_journal(config, journal)
        self.assertFalse(journal.path.exists())
        self.assertEqual(destination, self.root / "docs/plans/completed/ready")
        self.assertTrue((destination / "task_plan.md").is_file())


if __name__ == "__main__":
    unittest.main()
