#!/usr/bin/env python3
"""Run configured verification for a Journal-backed task."""

from __future__ import annotations

import argparse
import json
import sys

from harness_core import (
    HarnessError,
    find_project_root,
    load_config,
    record_verification,
    resolve_journal,
    run_commands,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--plan-id", default=None)
    parser.add_argument("--mode", choices=("fast", "full"), default="full")
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        config = load_config(find_project_root(args.project_root), require_file=True)
        journal = resolve_journal(config, args.plan_id)
        if journal is None:
            raise HarnessError("no active Journal; verification requires --plan-id or one active task")
        results = run_commands(config, args.mode)
        passed = all(item["exit_code"] == 0 for item in results)
        if args.record:
            record_verification(journal, args.mode, results)
        if args.json:
            print(json.dumps({"passed": passed, "mode": args.mode, "results": results}))
        else:
            for item in results:
                print(f"$ {item['command']}")
                if item["stdout"]:
                    print(str(item["stdout"]).rstrip())
                if item["stderr"]:
                    print(str(item["stderr"]).rstrip(), file=sys.stderr)
                print(f"exit {item['exit_code']}")
        return 0 if passed else 1
    except HarnessError as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
