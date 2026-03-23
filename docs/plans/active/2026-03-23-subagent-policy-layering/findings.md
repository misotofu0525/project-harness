# Findings & Decisions

## Requirements
- Put cross-project subagent rules in the global AGENTS layer
- Put project-specific subagent rules in the repo AGENTS layer
- Keep the full reasoning in research notes rather than bloating AGENTS

## Planned Split
- Global AGENTS:
  - when subagents help
  - when subagents hurt
  - default preference for built-in roles
  - the `benefit > cost` rule
  - the higher bar for custom roles
- Project AGENTS:
  - this repository prefers built-in roles for general work
  - `docs_syncer` is the only custom project-local subagent
  - when `docs_syncer` should run
  - what `docs_syncer` may update
  - required verification after `docs_syncer`

## Outcome
- The managed global mirror at `system/codex-home/AGENTS.md` and the live `~/.codex/AGENTS.md` now include a compressed cross-project `Subagent Policy` section.
- The repository `AGENTS.md` now includes a compressed `Project Subagent Rules` section centered on `docs_syncer`.
- `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `VERIFICATION.md`, and `memory/active-tasks.json` were synced in the same turn because the repository's operating conventions changed.
