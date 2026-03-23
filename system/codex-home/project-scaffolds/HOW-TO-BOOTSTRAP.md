# How To Bootstrap Project Docs

This directory is for bootstrapping project-level docs.

These files are scaffolding, not default runtime context.

## Use

Start with the smallest possible set:

1. Copy `project-AGENTS.template.md` to `AGENTS.md`
2. Create `handbook/` and copy `PROJECT_CONTEXT.template.md` to `handbook/PROJECT_CONTEXT.md`
3. Copy `active-tasks.template.json` only if work commonly spans sessions

Do not create extra files by default just because a template exists.

## Harness-Ready Upgrade

Add the next layer only when the project is active enough to benefit from it:

- Copy `ARCHITECTURE.template.md` to `handbook/ARCHITECTURE.md` when the codebase is no longer trivial.
- Copy `GOLDEN_PRINCIPLES.template.md` to `handbook/GOLDEN_PRINCIPLES.md` when code taste or architectural preferences need a stable home.
- Copy `VERIFICATION.template.md` to `handbook/VERIFICATION.md` when the project has more than one meaningful check.
- Copy `plan.template.md` into `docs/plans/active/<task>/task_plan.md` only for complex tasks.
- If you use a multi-file planning workflow, store `findings.md` and `progress.md` in the same task directory.
- Move finished task plan directories from `docs/plans/active/<task>/` to `docs/plans/completed/<task>/`.

## Principles

- Keep project `AGENTS.md` thin. It should route, not explain everything.
- Keep `handbook/PROJECT_CONTEXT.md` factual and current.
- Keep project current docs under `handbook/` so the root stays mostly entrypoint-shaped.
- Keep project knowledge in repo-local docs, not in chat history.
- Treat plans as artifacts, not disposable notes.
- Prefer executable verification commands or scripts over prose-only instructions.
- Delete sections that are not true for the project.
- Add project-specific docs only when they are repeatedly useful.
- Create plan artifacts only for complex tasks, using your planning workflow.
- Prefer task-scoped plan directories over root-level planning files.

## Suggested Bootstrap

For a new project, the recommended minimum is:

- `AGENTS.md`
- `handbook/PROJECT_CONTEXT.md`

Optional later:

- `memory/active-tasks.json`
- `handbook/ARCHITECTURE.md`
- `handbook/GOLDEN_PRINCIPLES.md`
- `handbook/VERIFICATION.md`
- `docs/plans/active/`
- `docs/plans/completed/`
- project-specific workflow docs or references

## Why file templates, not prompt templates

Prompt templates are easy to overuse and easy to leak into runtime context.

File templates are better for:

- consistent structure
- lower context noise
- easier review and iteration
- clearer project ownership

## Suggested Order

1. Start with `AGENTS.md` and `handbook/PROJECT_CONTEXT.md`.
2. Add `handbook/ARCHITECTURE.md` once the codebase has multiple moving parts.
3. Add `handbook/VERIFICATION.md` once verification is no longer a single obvious command.
4. Add task-scoped plan artifacts only for non-trivial work.
