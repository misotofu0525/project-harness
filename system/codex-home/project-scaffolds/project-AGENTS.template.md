# Project rules for [project-name]

## Purpose
- This file is the project entrypoint.
- Keep it thin.
- Load only the minimum project context needed for the current task.

## Canonical Paths
- Project entrypoint: `AGENTS.md`
- Project state: `handbook/PROJECT_CONTEXT.md`
- Short architecture map: `handbook/ARCHITECTURE.md` or project-defined equivalent
- Short code taste guide: `handbook/GOLDEN_PRINCIPLES.md` or project-defined equivalent
- Verification entrypoint: `handbook/VERIFICATION.md` or project-defined equivalent
- Cross-session task state: `memory/active-tasks.json`
- Active plan bundle: `docs/plans/active/<task>/`
- Active plan file: `docs/plans/active/<task>/task_plan.md`
- Completed plan bundles: `docs/plans/completed/<task>/`

## Load Order
- Read `handbook/PROJECT_CONTEXT.md` first.
- If the task depends on architecture and `handbook/ARCHITECTURE.md` exists, read it next.
- If the task is complex, read the active task bundle in `docs/plans/active/` when it exists.
- Within the active task bundle, read `task_plan.md` first and `findings.md` or `progress.md` only when needed.
- If the work spans sessions and `memory/active-tasks.json` exists, read it next.
- Read project-specific docs only when the scenario clearly requires them.

## Workflow Routes
- If the task is complex or multi-step, use the planning workflow.
- If the task is debugging or failure investigation, use the debugging workflow.
- If the task is near completion, use the verification workflow before declaring done.
- If the task is being resumed after a gap, re-read `handbook/PROJECT_CONTEXT.md` and active task state first.
- If the task is straightforward, work directly.

## Project Hard Rules
- Never modify [critical paths or files] without explicit confirmation.
- Use the project's real commands and conventions. Do not guess.
- Keep changes small unless the task explicitly requires broader change.
- Prefer existing patterns over introducing new structure.

## Verification
- Canonical verification doc: `handbook/VERIFICATION.md` or `[path-or-none]`
- Fastest relevant check: `[command-or-script]`
- Full verification when needed: `[command-or-script]`
- Prefer repo-local scripts or task runners over hand-assembled checks.

## Project-Specific Docs
- Architecture: `handbook/ARCHITECTURE.md` or `[path-or-none]`
- Golden principles: `handbook/GOLDEN_PRINCIPLES.md` or `[path-or-none]`
- Verification guide: `handbook/VERIFICATION.md` or `[path-or-none]`
- Decisions or ADRs: `[path-or-none]`
- References: `[path-or-none]`
- Debugging guide: `[path-or-none]`
- Review guide: `[path-or-none]`

## Notes
- Delete placeholder text after setup.
- Delete sections that do not matter for this project.
- Keep this file short enough that reading it is cheap.
