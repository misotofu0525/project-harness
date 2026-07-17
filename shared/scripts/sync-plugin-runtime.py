#!/usr/bin/env python3
"""Materialize canonical shared assets into self-contained plugin packages."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


RUNTIME_FILES = (
    "harness_core.py",
    "setup-project.py",
    "create-plan.py",
    "resolve-plan.py",
    "restore-plan.py",
    "pre-compact.py",
    "verify-task.py",
    "context-impact.py",
    "archive-plan.py",
)
PLUGIN_ROOTS = (
    Path("plugins/codex/project-harness"),
    Path("plugins/claude-code/project-harness"),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    template_dir = repo_root / "shared" / "templates"
    mismatches: list[str] = []

    for relative_plugin_root in PLUGIN_ROOTS:
        plugin_root = repo_root / relative_plugin_root
        if not plugin_root.is_dir():
            mismatches.append(f"missing plugin root: {relative_plugin_root}")
            continue
        lib_dir = plugin_root / "lib"
        copied_template_dir = plugin_root / "templates"
        if not args.check:
            lib_dir.mkdir(parents=True, exist_ok=True)
            copied_template_dir.mkdir(parents=True, exist_ok=True)
        for name in RUNTIME_FILES:
            source = script_dir / name
            target = lib_dir / name
            if args.check:
                if not target.is_file() or target.read_bytes() != source.read_bytes():
                    mismatches.append(f"runtime drift: {target.relative_to(repo_root)}")
            else:
                shutil.copy2(source, target)
        for source in sorted(template_dir.iterdir(), key=lambda path: path.name):
            if not source.is_file():
                continue
            target = copied_template_dir / source.name
            if args.check:
                if not target.is_file() or target.read_bytes() != source.read_bytes():
                    mismatches.append(f"template drift: {target.relative_to(repo_root)}")
            else:
                shutil.copy2(source, target)

    if mismatches:
        print("\n".join(mismatches))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
