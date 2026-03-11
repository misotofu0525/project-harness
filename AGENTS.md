# Project rules for context-engineering

## Purpose
- This repository is a research project for exploring harness engineering, context engineering, and Codex workflow design.
- Keep the root thin and predictable.
- Load only the minimum project context needed for the current task.

## Canonical Paths
- Project entrypoint: `AGENTS.md`
- Project state: `PROJECT_CONTEXT.md`
- Short architecture map: `ARCHITECTURE.md`
- Short code and workflow taste guide: `GOLDEN_PRINCIPLES.md`
- Verification entrypoint: `VERIFICATION.md`
- Research index: `docs/research/index.zh.md`
- Managed system mirror: `system/codex-home/`
- Managed shared skills mirror: `system/codex-home/skills/`
- Cross-session task state: `memory/active-tasks.json`
- Active plan bundle: `docs/plans/active/<task>/`
- Active plan file: `docs/plans/active/<task>/task_plan.md`
- Completed plan bundles: `docs/plans/completed/<task>/`

## Load Order
- Read `PROJECT_CONTEXT.md` first.
- If the task affects repository structure, workflow design, or system boundaries, read `ARCHITECTURE.md` next.
- If the task is about a managed shared skill, read the relevant `system/codex-home/skills/<skill>/SKILL.md` after the core entry docs.
- If the task is complex, read the active task bundle in `docs/plans/active/` when it exists.
- Within the active task bundle, read `task_plan.md` first and `findings.md` or `progress.md` only when needed.
- If the task depends on earlier research outputs, read `docs/research/index.zh.md` and only the relevant source or note files.
- If the task is about Codex global policy, shared scaffolds, or shared skills, read `system/codex-home/` rather than assuming `~/.codex/` is the only tracked source.
- If the work spans sessions, read `memory/active-tasks.json` when it exists.

## Required Procedures
- If the task is multi-step research, repository restructuring, or workflow design, use the planning workflow and keep the active task bundle current.
- If the task depends on external agent frameworks, APIs, or product behavior, verify against current official documentation before updating project guidance.
- If the task changes repository structure or operating conventions, update `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, and `VERIFICATION.md` in the same turn.
- If the task changes the managed global Codex policy, shared scaffolds, or shared skills, update the mirror under `system/codex-home/` and the live `~/.codex/` copy together unless the task explicitly says otherwise.
- If the task produces durable research output, store it under `docs/research/notes/` or `docs/research/sources/`, not in the repository root.
- Before declaring completion, verify that no temporary planning files remain in the repository root and that no scaffold placeholders remain in the entry docs.

## Project Hard Rules
- Preserve source captures under `docs/research/sources/` and keep provenance metadata intact.
- Keep the repository root reserved for high-signal entry docs only.
- Prefer moving or archiving temporary files over leaving duplicates in multiple locations.
- Use explicit file paths and source provenance when summarizing research conclusions.

## Verification
- Canonical verification doc: `VERIFICATION.md`
- Fastest relevant check: see `VERIFICATION.md`
- Full verification when needed: see `VERIFICATION.md`

## Project-Specific Docs
- Research index: `docs/research/index.zh.md`
- Source captures: `docs/research/sources/`
- Research notes: `docs/research/notes/`
- Managed Codex home mirror: `system/codex-home/`
- Managed shared skills mirror: `system/codex-home/skills/`
- Completed research plans: `docs/plans/completed/`

## Notes
- This project is markdown-first and research-first.
- Keep this file thin enough that reading it is cheap.
