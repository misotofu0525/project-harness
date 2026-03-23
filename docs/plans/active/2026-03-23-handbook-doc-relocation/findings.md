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
- The shared project scaffold under `system/codex-home/project-scaffolds/` still describes the current default convention with root-level project docs.
- The shared `current-docs-sync` skill is written to handle projects that use either the default scaffold names or project-defined equivalents.
- Confirmed decision: this task stays repo-local, so shared scaffold and shared skill assets remain unchanged unless the goal expands from local structure to shared convention design.

## Files Synced For This Move
- `AGENTS.md`
- `handbook/PROJECT_CONTEXT.md`
- `handbook/ARCHITECTURE.md`
- `handbook/GOLDEN_PRINCIPLES.md`
- `handbook/VERIFICATION.md`
- `memory/active-tasks.json`
- `docs/research/notes/openai-codex-best-practices-summary.zh.md`
- `docs/research/notes/claude-code-workflow-comparison.zh.md`
