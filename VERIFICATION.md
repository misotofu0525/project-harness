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
- Full project check: `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md PROJECT_CONTEXT.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md VERIFICATION.md docs system/codex-home --glob '!system/codex-home/project-scaffolds/**'`
- When to run it: after creating or editing project-level docs and templates.
- Expected runtime: a few seconds

## Reproduction and Smoke Checks
- Local repro command: `find docs/plans -maxdepth 4 -type f | sort`
- Smoke or end-to-end check: `find . -maxdepth 1 -type f | sort`
- Required fixture, sample data, or environment: none

## Structural Checks
- Architecture or dependency check: `find docs/research -maxdepth 3 -type f | sort`
- Managed shared skill mirror check: `find system/codex-home/skills -maxdepth 3 -type f | sort`
- Live shared skill check: `find ~/.codex/skills -maxdepth 2 \\( -type d -o -type f \\) | sort`
- Managed system mirror check: `find system/codex-home -maxdepth 3 -type f | sort`
- Lint or static analysis check: `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md PROJECT_CONTEXT.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md VERIFICATION.md docs system/codex-home --glob '!system/codex-home/project-scaffolds/**'`
- Naming, schema, or boundary check: `find docs/plans -maxdepth 4 -type f | sort`
- What these checks are protecting:
  - root cleanliness
  - placeholder-free entry docs
  - placeholder-free managed shared skill files
  - predictable placement of research notes and plan bundles
  - presence of mirrored shared skills under `system/codex-home/skills/`
  - presence of the managed Codex home mirror and live skill copy

## Non-Negotiable Checks
- Must pass before declaring completion:
  - no root-level `task_plan.md`, `findings.md`, or `progress.md`
  - no scaffold placeholder text in project entry docs
  - no scaffold placeholder text in managed shared skill files
  - research sources remain accessible under `docs/research/sources/`
  - managed shared skills remain under `system/codex-home/skills/`
  - managed Codex home mirror contains only policy, scaffold, and shared skill assets
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
