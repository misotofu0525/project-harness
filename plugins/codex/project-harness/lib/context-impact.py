#!/usr/bin/env python3
"""Suggest scoped project-context modules affected by changed paths."""

from __future__ import annotations

import argparse
import json
import sys

from harness_core import HarnessError, context_impact, find_project_root, git_changed_paths, load_config


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--path", action="append", default=[])
    args = parser.parse_args()
    try:
        config = load_config(find_project_root(args.project_root), require_file=True)
        paths = args.path or git_changed_paths(config.project_root)
        print(json.dumps(context_impact(paths, config), indent=2))
        return 0
    except HarnessError as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
