#!/usr/bin/env python3
"""Emit a lightweight, non-blocking PreCompact checkpoint reminder."""

from __future__ import annotations

import argparse
import json
import sys

from harness_core import HarnessError, find_project_root, load_config, parse_hook_input, resolve_journal


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--plan-id", default=None)
    parser.add_argument("--hook", action="store_true")
    args = parser.parse_args()
    try:
        hook_input = parse_hook_input(sys.stdin.read()) if args.hook else {}
        root_arg = args.project_root or hook_input.get("cwd")
        root = find_project_root(str(root_arg) if root_arg else None)
        if args.hook and not (root / ".harness.toml").is_file():
            return 0
        config = load_config(root, require_file=True)
        journal = resolve_journal(config, args.plan_id)
        if journal is None:
            return 0
        message = (
            f"Project Harness: compaction is starting for Journal {journal.task_id}. "
            "If the current work crossed a semantic boundary, update Latest Checkpoint; "
            "the next SessionStart restore will use the checkpoint already on disk."
        )
        if args.hook:
            print(json.dumps({"continue": True, "systemMessage": message}))
        else:
            print(message)
        return 0
    except HarnessError as exc:
        if args.hook:
            print(json.dumps({"continue": True, "systemMessage": f"Project Harness: {exc}"}))
            return 0
        print(f"project-harness: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
