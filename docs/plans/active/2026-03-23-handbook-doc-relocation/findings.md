# Findings & Decisions

## Confirmed Impact Surface
- Root docs to move:
  - `PROJECT_CONTEXT.md`
  - `ARCHITECTURE.md`
  - `GOLDEN_PRINCIPLES.md`
  - `VERIFICATION.md`
- Root doc to keep:
  - `AGENTS.md`
- Repo-local references that must be updated:
  - project `AGENTS.md`
  - the moved docs themselves
  - `memory/active-tasks.json`
  - research notes with absolute or factual references to the moved files
  - verification commands that enumerate root files directly

## User-Level AGENTS Relevance
- The live user-level file at `~/.codex/AGENTS.md` does not hardcode this repository's project-local file paths.
- The managed mirror at `system/codex-home/AGENTS.md` matches the live file and is likewise path-agnostic for this move.
- Current expectation: no change needed in either global AGENTS file unless we decide to generalize `handbook/` as a shared scaffold convention.

## Shared Asset Scope
- The shared project scaffold under `system/codex-home/project-scaffolds/` is now part of the change surface.
- The shared `current-docs-sync` skill must move with the scaffold default, otherwise the bootstrap default and the docs-sync workflow would disagree.
- Confirmed decision: the new shared default keeps `AGENTS.md` in the root and places the rest of the current docs under `handbook/`.

## Files Synced For This Move
- `AGENTS.md`
- `handbook/PROJECT_CONTEXT.md`
- `handbook/ARCHITECTURE.md`
- `handbook/GOLDEN_PRINCIPLES.md`
- `handbook/VERIFICATION.md`
- `memory/active-tasks.json`
- `docs/research/notes/openai-codex-best-practices-summary.zh.md`
- `docs/research/notes/claude-code-workflow-comparison.zh.md`
- `system/codex-home/project-scaffolds/HOW-TO-BOOTSTRAP.md`
- `system/codex-home/project-scaffolds/project-AGENTS.template.md`
- `system/codex-home/project-scaffolds/PROJECT_CONTEXT.template.md`
- `system/codex-home/project-scaffolds/active-tasks.template.json`
- `system/codex-home/skills/current-docs-sync/SKILL.md`
- `system/codex-home/skills/current-docs-sync/references/update-matrix.md`
- `~/.codex/project-scaffolds/HOW-TO-BOOTSTRAP.md`
- `~/.codex/project-scaffolds/project-AGENTS.template.md`
- `~/.codex/project-scaffolds/PROJECT_CONTEXT.template.md`
- `~/.codex/project-scaffolds/active-tasks.template.json`
- `~/.codex/skills/current-docs-sync/SKILL.md`
- `~/.codex/skills/current-docs-sync/references/update-matrix.md`

## User-Level AGENTS Relevance
- No change needed in `~/.codex/AGENTS.md` or `system/codex-home/AGENTS.md`.
- Reason: the global layer routes to the scaffold directory but does not define the scaffold's internal file layout.
