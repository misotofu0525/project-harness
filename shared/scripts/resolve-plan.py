#!/usr/bin/env python3
"""Resolve the active Project Harness Journal deterministically."""

from __future__ import annotations

import argparse
import json
import sys

from harness_core import HarnessError, find_project_root, load_config, resolve_journal


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--plan-id", default=None)
    parser.add_argument("--format", choices=("path", "json"), default="path")
    args = parser.parse_args()
    try:
        root = find_project_root(args.project_root)
        config = load_config(root, require_file=True)
        journal = resolve_journal(config, args.plan_id)
    except HarnessError as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 2
    if journal is None:
        if args.format == "json":
            print(json.dumps({"status": "none"}))
        return 0
    if args.format == "json":
        print(json.dumps({"status": "resolved", "task_id": journal.task_id, "path": str(journal.path)}))
    else:
        print(journal.path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
