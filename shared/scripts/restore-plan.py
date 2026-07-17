#!/usr/bin/env python3
"""Restore a compact Journal checkpoint for CLI or SessionStart hooks."""

from __future__ import annotations

import argparse
import json
import sys

from harness_core import (
    HarnessError,
    find_project_root,
    load_config,
    parse_hook_input,
    render_restore,
    resolve_journal,
    restore_payload,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--plan-id", default=None)
    parser.add_argument("--format", choices=("text", "json"), default="text")
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
        payload = restore_payload(journal, config.project_root)
        print(json.dumps(payload) if args.format == "json" else render_restore(payload))
        return 0
    except HarnessError as exc:
        if args.hook:
            print(f"[Project Harness] Journal restore skipped: {exc}")
            return 0
        print(f"project-harness: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
