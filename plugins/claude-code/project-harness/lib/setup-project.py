#!/usr/bin/env python3
"""Install the minimal Project Harness project layer without creating a Journal."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def toml_array(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(value) for value in values) + "]"


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--fast", action="append", default=[])
    parser.add_argument("--full", action="append", default=[])
    args = parser.parse_args()
    root = Path(args.project_root).expanduser().resolve()
    templates = Path(__file__).resolve().parent.parent / "templates"
    try:
        root.mkdir(parents=True, exist_ok=True)
        harness = (templates / "harness.toml").read_text(encoding="utf-8")
        harness = harness.replace("fast = []", f"fast = {toml_array(args.fast)}", 1)
        harness = harness.replace("full = []", f"full = {toml_array(args.full)}", 1)
        files = {
            root / "AGENTS.md": templates / "AGENTS.md",
            root / "CLAUDE.md": templates / "CLAUDE.md",
            root / ".harness.toml": None,
            root / "docs/agent/index.md": templates / "context-index.md",
            root / "docs/agent/verification.md": templates / "verification.md",
        }
        existing = [str(path) for path in files if path.exists()]
        if existing:
            raise FileExistsError("refusing partial setup; files already exist: " + ", ".join(existing))
        for target, source in files.items():
            content = harness if source is None else source.read_text(encoding="utf-8")
            write_new(target, content)
        (root / "docs/plans/active").mkdir(parents=True, exist_ok=True)
        (root / "docs/plans/completed").mkdir(parents=True, exist_ok=True)
        print(root)
        return 0
    except (OSError, FileNotFoundError) as exc:
        print(f"project-harness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
