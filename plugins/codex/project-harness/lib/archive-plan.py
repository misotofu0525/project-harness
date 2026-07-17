#!/usr/bin/env python3
"""Archive a Journal after explicit finish prerequisites pass."""

from __future__ import annotations

import argparse
import sys

from harness_core import HarnessError, archive_journal, find_project_root, load_config, resolve_journal


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--plan-id", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        config = load_config(find_project_root(args.project_root), require_file=True)
        journal = resolve_journal(config, args.plan_id)
        if journal is None:
            raise HarnessError("no active Journal to archive")
        destination = archive_journal(config, journal, dry_run=args.dry_run)
        print(destination)
        return 0
    except HarnessError as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
