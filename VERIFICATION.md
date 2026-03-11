# context-engineering Verification

## Purpose
- This file defines the canonical verification paths for this project.
- Keep commands copy-pastable and current.
- Prefer simple structural checks over prose-only confidence.

## Fast Feedback
- Smallest useful check: `find . -maxdepth 2 -type f | sort`
- Typical use: confirm root cleanliness and high-level file layout after document moves or bootstrap changes.
- Expected runtime: a few seconds

## Full Verification
- Full project check: `rg -n '\\[project-name\\]|\\[path-or-none\\]|\\[command|\\[task-name\\]' AGENTS.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md docs`
- When to run it: after creating or editing project-level docs and templates.
- Expected runtime: a few seconds

## Reproduction and Smoke Checks
- Local repro command: `find docs/plans -maxdepth 4 -type f | sort`
- Smoke or end-to-end check: `find . -maxdepth 1 -type f | sort`
- Required fixture, sample data, or environment: none

## Structural Checks
- Architecture or dependency check: `find docs/research -maxdepth 3 -type f | sort`
- Managed system mirror check: `find system/codex-home -maxdepth 3 -type f | sort`
- Lint or static analysis check: `rg -n '\\[project-name\\]|\\[path-or-none\\]|\\[command|\\[task-name\\]' AGENTS.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md docs`
- Naming, schema, or boundary check: `find docs/plans -maxdepth 4 -type f | sort`
- What these checks are protecting:
  - root cleanliness
  - placeholder-free entry docs
  - predictable placement of research notes and plan bundles
  - presence of the managed Codex home mirror

## Non-Negotiable Checks
- Must pass before declaring completion:
  - no root-level `task_plan.md`, `findings.md`, or `progress.md`
  - no scaffold placeholder text in project entry docs
  - research sources remain accessible under `docs/research/sources/`
  - managed Codex home mirror contains only policy and scaffold assets
- Must not be modified as part of normal task completion:
  - provenance metadata inside preserved source captures

## Failure Triage
- First file or log to inspect: `PROJECT_CONTEXT.md`
- Common failure mode: moved files without updating links or operating docs
- Recovery step: fix paths first, then re-run the structural checks above

## Notes
- Promote repeated manual checks into scripts over time.
- Prefer one stable entrypoint per check class.
- Promote repeated repository hygiene issues into mechanical checks.
- Remove stale commands quickly.
