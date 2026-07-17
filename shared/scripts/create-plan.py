#!/usr/bin/env python3
"""Create one isolated Project Harness Journal from canonical templates."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from harness_core import HarnessError, find_project_root, load_config, validate_plan_id


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan_id")
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--title", default="Task title")
    parser.add_argument("--goal", default="State the intended end state in one sentence.")
    args = parser.parse_args()
    try:
        config = load_config(find_project_root(args.project_root), require_file=True)
        task_id = validate_plan_id(args.plan_id)
        target = config.active_root / task_id
        if target.exists():
            raise HarnessError(f"active Journal already exists: {task_id}")
        template_root = Path(__file__).resolve().parent.parent / "templates"
        required = ("task_plan.md", "findings.md", "progress.md")
        missing = [name for name in required if not (template_root / name).is_file()]
        if missing:
            raise HarnessError(f"missing packaged Journal templates: {', '.join(missing)}")
        target.mkdir(parents=True)
        for name in required:
            content = (template_root / name).read_text(encoding="utf-8")
            if name == "task_plan.md":
                content = content.replace("Task title", args.title, 1)
                content = content.replace(
                    "State the intended end state in one sentence.", args.goal, 1
                )
            (target / name).write_text(content, encoding="utf-8")
        print(target)
        return 0
    except (HarnessError, OSError) as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
