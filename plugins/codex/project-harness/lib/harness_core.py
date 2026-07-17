#!/usr/bin/env python3
"""Shared deterministic core for Project Harness scripts."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tomllib
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


PLAN_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
JOURNAL_FILES = ("task_plan.md", "findings.md", "progress.md")


class HarnessError(RuntimeError):
    """An actionable Project Harness error."""


@dataclass(frozen=True)
class HarnessConfig:
    project_root: Path
    task_root: Path
    context_index: Path
    verification_fast: tuple[str, ...]
    verification_full: tuple[str, ...]

    @property
    def active_root(self) -> Path:
        return self.task_root / "active"

    @property
    def completed_root(self) -> Path:
        return self.task_root / "completed"


@dataclass(frozen=True)
class Journal:
    task_id: str
    path: Path

    @property
    def task_plan(self) -> Path:
        return self.path / "task_plan.md"

    @property
    def findings(self) -> Path:
        return self.path / "findings.md"

    @property
    def progress(self) -> Path:
        return self.path / "progress.md"


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def find_project_root(start: str | Path | None = None) -> Path:
    current = Path(start or Path.cwd()).expanduser().resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".harness.toml").is_file():
            return candidate
    return current


def _safe_relative_path(root: Path, raw: object, field: str) -> Path:
    if not isinstance(raw, str) or not raw.strip():
        raise HarnessError(f"{field} must be a non-empty relative path")
    value = Path(raw)
    if value.is_absolute():
        raise HarnessError(f"{field} must be relative to the project root")
    resolved = (root / value).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise HarnessError(f"{field} escapes the project root: {raw}") from exc
    return resolved


def _command_list(raw: object, field: str) -> tuple[str, ...]:
    if not isinstance(raw, list) or not all(isinstance(item, str) and item.strip() for item in raw):
        raise HarnessError(f"{field} must be an array of non-empty command strings")
    return tuple(item.strip() for item in raw)


def load_config(project_root: str | Path, *, require_file: bool = False) -> HarnessConfig:
    root = Path(project_root).expanduser().resolve()
    config_path = root / ".harness.toml"
    if not config_path.is_file():
        if require_file:
            raise HarnessError(f"missing Project Harness config: {config_path}")
        data: dict[str, object] = {}
    else:
        try:
            data = tomllib.loads(config_path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            raise HarnessError(f"cannot read {config_path}: {exc}") from exc

    version = data.get("version", 1)
    if not isinstance(version, int) or isinstance(version, bool) or version != 1:
        raise HarnessError(f"unsupported Project Harness config version: {version!r}")

    verification = data.get("verification", {})
    if not isinstance(verification, dict):
        raise HarnessError("verification must be a TOML table")

    return HarnessConfig(
        project_root=root,
        task_root=_safe_relative_path(root, data.get("task_root", "docs/plans"), "task_root"),
        context_index=_safe_relative_path(
            root, data.get("context_index", "docs/agent/index.md"), "context_index"
        ),
        verification_fast=_command_list(verification.get("fast", []), "verification.fast"),
        verification_full=_command_list(verification.get("full", []), "verification.full"),
    )


def validate_plan_id(plan_id: str) -> str:
    value = plan_id.strip()
    if not PLAN_ID_PATTERN.fullmatch(value):
        raise HarnessError(
            "PLAN_ID must start with an alphanumeric character and contain only "
            "letters, digits, dots, underscores, or hyphens"
        )
    return value


def _journal_from_path(active_root: Path, path: Path) -> Journal:
    resolved_root = active_root.resolve()
    resolved = path.resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as exc:
        raise HarnessError(f"Journal escapes active task root: {path}") from exc
    missing = [name for name in JOURNAL_FILES if not (resolved / name).is_file()]
    if missing:
        raise HarnessError(f"Journal {resolved.name!r} is missing: {', '.join(missing)}")
    return Journal(task_id=resolved.name, path=resolved)


def active_journals(config: HarnessConfig) -> list[Journal]:
    root = config.active_root
    if not root.is_dir():
        return []
    journals: list[Journal] = []
    for path in sorted(root.iterdir(), key=lambda item: item.name):
        if path.is_dir() and not path.name.startswith(".") and (path / "task_plan.md").is_file():
            journals.append(_journal_from_path(root, path))
    return journals


def resolve_journal(config: HarnessConfig, plan_id: str | None = None) -> Journal | None:
    explicit = plan_id if plan_id is not None else os.environ.get("PLAN_ID")
    if explicit is not None and explicit.strip():
        task_id = validate_plan_id(explicit)
        candidate = config.active_root / task_id
        if not candidate.is_dir():
            raise HarnessError(f"PLAN_ID {task_id!r} does not name an active Journal")
        return _journal_from_path(config.active_root, candidate)

    journals = active_journals(config)
    if not journals:
        return None
    if len(journals) == 1:
        return journals[0]
    task_ids = ", ".join(journal.task_id for journal in journals)
    raise HarnessError(f"multiple active Journals found; set PLAN_ID explicitly. Active tasks: {task_ids}")


def section(markdown: str, title: str) -> str:
    pattern = re.compile(rf"^##[ \t]+{re.escape(title)}[ \t]*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(markdown)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^#{1,2}[ \t]+", markdown[start:], re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(markdown)
    return markdown[start:end].strip()


def replace_section(markdown: str, title: str, body: str) -> str:
    heading_pattern = re.compile(
        rf"^##[ \t]+{re.escape(title)}[ \t]*$", re.MULTILINE | re.IGNORECASE
    )
    match = heading_pattern.search(markdown)
    replacement = f"## {title}\n\n{body.strip()}\n"
    if not match:
        return markdown.rstrip() + "\n\n" + replacement
    start = match.start()
    next_heading = re.search(r"^#{1,2}[ \t]+", markdown[match.end() :], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(markdown)
    suffix = markdown[end:].lstrip("\n")
    return markdown[:start].rstrip() + "\n\n" + replacement + ("\n" + suffix if suffix else "")


def first_content_line(value: str) -> str:
    for line in value.splitlines():
        cleaned = re.sub(r"^[-*+]\s+", "", line.strip())
        if cleaned:
            return cleaned
    return ""


def checkpoint_fields(progress_markdown: str) -> dict[str, str]:
    checkpoint = section(progress_markdown, "Latest Checkpoint")
    fields: dict[str, str] = {}
    for line in checkpoint.splitlines():
        match = re.match(r"^-\s*([^:]+):\s*(.*)$", line.strip())
        if match:
            fields[match.group(1).strip().lower()] = match.group(2).strip()
    return fields


def restore_payload(journal: Journal, project_root: Path) -> dict[str, object]:
    plan_text = journal.task_plan.read_text(encoding="utf-8")
    progress_text = journal.progress.read_text(encoding="utf-8")
    checkpoint = checkpoint_fields(progress_text)
    resolved_root = project_root.resolve()
    rel = lambda path: path.resolve().relative_to(resolved_root).as_posix()
    return {
        "task_id": journal.task_id,
        "goal": first_content_line(section(plan_text, "Goal")),
        "checkpoint": {
            "current_focus": checkpoint.get("current focus", ""),
            "next_action": checkpoint.get("next action", ""),
            "blocked_on": checkpoint.get("blocked on", ""),
            "last_meaningful_update": checkpoint.get("last meaningful update", ""),
        },
        "paths": {
            "task_plan": rel(journal.task_plan),
            "findings": rel(journal.findings),
            "progress": rel(journal.progress),
        },
    }


def render_restore(payload: dict[str, object]) -> str:
    checkpoint = payload["checkpoint"]
    paths = payload["paths"]
    assert isinstance(checkpoint, dict)
    assert isinstance(paths, dict)
    lines = [
        "[Project Harness] Restore this Journal before continuing:",
        f"- Task: {payload['task_id']}",
        f"- Goal: {payload['goal']}",
        f"- Current focus: {checkpoint.get('current_focus', '')}",
        f"- Next action: {checkpoint.get('next_action', '')}",
        f"- Blocked on: {checkpoint.get('blocked_on', '')}",
        f"- Last meaningful update: {checkpoint.get('last_meaningful_update', '')}",
        f"- Task plan: {paths.get('task_plan', '')}",
        f"- Findings: {paths.get('findings', '')}",
        f"- Progress: {paths.get('progress', '')}",
        "Read the Journal files as needed and continue from the checkpoint.",
    ]
    return "\n".join(lines)


def parse_hook_input(raw: str) -> dict[str, object]:
    if not raw.strip():
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise HarnessError(f"invalid hook input JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise HarnessError("hook input must be a JSON object")
    return value


def run_commands(config: HarnessConfig, mode: str) -> list[dict[str, object]]:
    commands: Sequence[str]
    if mode == "fast":
        commands = config.verification_fast
    elif mode == "full":
        commands = config.verification_full
    else:
        raise HarnessError(f"unknown verification mode: {mode}")
    if not commands:
        raise HarnessError(f"verification.{mode} has no configured commands")

    results: list[dict[str, object]] = []
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=config.project_root,
            shell=True,
            text=True,
            capture_output=True,
            check=False,
        )
        results.append(
            {
                "command": command,
                "exit_code": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
            }
        )
        if completed.returncode != 0:
            break
    return results


def record_verification(journal: Journal, mode: str, results: Iterable[dict[str, object]]) -> bool:
    materialized = list(results)
    passed = bool(materialized) and all(item["exit_code"] == 0 for item in materialized)
    command_lines = [
        f"  - `{item['command']}` -> exit {item['exit_code']}" for item in materialized
    ]
    body = "\n".join(
        [
            f"- Result: {'passed' if passed else 'failed'}",
            f"- Mode: {mode}",
            f"- Recorded: {utc_timestamp()}",
            "- Commands:",
            *command_lines,
        ]
    )
    current = journal.progress.read_text(encoding="utf-8")
    journal.progress.write_text(replace_section(current, "Verification Evidence", body), encoding="utf-8")
    return passed


def result_field(markdown: str, heading: str) -> str:
    value = section(markdown, heading)
    match = re.search(r"^-\s*Result:\s*([^\n]+)$", value, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip().lower() if match else ""


def done_when_problems(plan_markdown: str) -> list[str]:
    value = section(plan_markdown, "Done When")
    if not value:
        return ["task_plan.md has no Done When section"]
    checkboxes = re.findall(r"^-\s*\[([ xX])\]\s+.+$", value, re.MULTILINE)
    if not checkboxes:
        return ["Done When must contain an explicit checklist"]
    if any(marker == " " for marker in checkboxes):
        return ["one or more Done When criteria are unchecked"]
    return []


def finish_problems(journal: Journal) -> list[str]:
    problems = done_when_problems(journal.task_plan.read_text(encoding="utf-8"))
    progress = journal.progress.read_text(encoding="utf-8")
    if result_field(progress, "Verification Evidence") != "passed":
        problems.append("Verification Evidence result must be passed")
    if result_field(progress, "Diff Review") != "passed":
        problems.append("Diff Review result must be passed")
    context_result = result_field(progress, "Project Context Review")
    if context_result not in {"no-impact", "updated", "follow-up"}:
        problems.append("Project Context Review must be no-impact, updated, or follow-up")
    if context_result == "follow-up":
        context = section(progress, "Project Context Review")
        notes = re.search(r"^-\s*Notes:\s*(.+)$", context, re.MULTILINE | re.IGNORECASE)
        if not notes or not notes.group(1).strip():
            problems.append("Project Context Review follow-up requires concrete Notes")
    return problems


def archive_journal(config: HarnessConfig, journal: Journal, *, dry_run: bool = False) -> Path:
    problems = finish_problems(journal)
    if problems:
        raise HarnessError("finish prerequisites failed:\n- " + "\n- ".join(problems))
    destination = config.completed_root / journal.task_id
    if destination.exists():
        raise HarnessError(f"completed destination already exists: {destination}")
    if dry_run:
        return destination
    config.completed_root.mkdir(parents=True, exist_ok=True)
    shutil.move(str(journal.path), str(destination))
    return destination


def git_changed_paths(project_root: Path) -> list[str]:
    commands = (
        ["git", "diff", "--name-only", "--"],
        ["git", "diff", "--cached", "--name-only", "--"],
        ["git", "ls-files", "--others", "--exclude-standard"],
    )
    results = [
        subprocess.run(
            command,
            cwd=project_root,
            text=True,
            capture_output=True,
            check=False,
        )
        for command in commands
    ]
    if any(result.returncode != 0 for result in results):
        raise HarnessError("context impact check requires a readable git working tree")
    return sorted(
        {
            line
            for result in results
            for line in result.stdout.splitlines()
            if line
        }
    )


def context_impact(paths: Iterable[str], config: HarnessConfig) -> dict[str, object]:
    normalized = sorted({Path(path).as_posix() for path in paths})
    candidates: dict[str, set[str]] = {}

    def add(module: str, reason: str) -> None:
        candidates.setdefault(module, set()).add(reason)

    for path in normalized:
        name = Path(path).name
        parts = Path(path).parts
        if path == ".harness.toml" or "scripts" in parts or path.startswith(".github/workflows/") or name in {
            "package.json",
            "pyproject.toml",
            "Cargo.toml",
            "go.mod",
            "Makefile",
        }:
            add("verification.md", f"verification surface changed: {path}")
        if ".codex-plugin" in parts or ".claude-plugin" in parts or path.endswith("hooks/hooks.json"):
            add("distribution.md", f"plugin distribution surface changed: {path}")
        if name in {"AGENTS.md", "CLAUDE.md"} or path.endswith("docs/agent/index.md"):
            add("architecture.md", f"context routing surface changed: {path}")
        if any(part in {"migrations", "schema", "schemas", "database", "db"} for part in parts):
            add("data.md", f"data or schema surface changed: {path}")
        if parts and parts[0] in {"apps", "packages", "services"}:
            add("architecture.md", f"top-level system boundary changed: {path}")

    module_root = config.context_index.parent
    items = [
        {
            "module": module,
            "path": (module_root / module).relative_to(config.project_root).as_posix(),
            "exists": (module_root / module).is_file(),
            "reasons": sorted(reasons),
        }
        for module, reasons in sorted(candidates.items())
    ]
    return {"changed_paths": normalized, "candidates": items}
