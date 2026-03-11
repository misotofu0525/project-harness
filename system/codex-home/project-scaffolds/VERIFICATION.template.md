# [project-name] Verification

## Purpose
- This file defines the canonical verification paths for this project.
- Keep commands copy-pastable and current.
- Prefer repo-local scripts or task runners over ad-hoc command sequences.

## Fast Feedback
- Smallest useful check: `[command-or-script]`
- Typical use:
- Expected runtime:

## Full Verification
- Full project check: `[command-or-script]`
- When to run it:
- Expected runtime:

## Reproduction and Smoke Checks
- Local repro command: `[command-or-script]`
- Smoke or end-to-end check: `[command-or-script-or-none]`
- Required fixture, sample data, or environment:

## Structural Checks
- Architecture or dependency check: `[command-or-script-or-none]`
- Lint or static analysis check: `[command-or-script-or-none]`
- Naming, schema, or boundary check: `[command-or-script-or-none]`
- What these checks are protecting:

## Non-Negotiable Checks
- Must pass before declaring completion:
- Must not be modified as part of normal task completion:

## Failure Triage
- First file or log to inspect:
- Common failure mode:
- Recovery step:

## Notes
- Promote repeated manual checks into scripts over time.
- Prefer one stable entrypoint per check class.
- Promote repeated code smell or taste issues into mechanical checks.
- Remove stale commands quickly.
