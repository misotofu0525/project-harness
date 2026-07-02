# Task Plan: Refresh docs_syncer to the current Codex subagent schema

## Goal
Refactor the repository-local `docs_syncer` custom subagent from the older split config format into the current official standalone agent-file format, then sync all affected project docs and verification commands.

## Current Phase
Complete

## Phases

### Phase 1: Discovery
- [x] Inspect the current `.codex/` agent config layout
- [x] Verify the current official Codex subagent docs and identify the schema mismatch
- [x] Identify all repo-local references that assume the old `config_file` layout
- **Status:** complete

### Phase 2: Config Refactor
- [x] Update `.codex/config.toml` to keep only global agent settings
- [x] Replace the old custom agent file with a current-schema standalone file
- [x] Align the agent filename with the agent name for clarity
- **Status:** complete

### Phase 3: Current Docs Sync
- [x] Update `AGENTS.md`
- [x] Update `handbook/PROJECT_CONTEXT.md`, `handbook/ARCHITECTURE.md`, and `handbook/VERIFICATION.md`
- [x] Update any task or note references that would otherwise describe the old layout inaccurately
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run structural and placeholder checks
- [x] Run a config-focused smoke check if feasible
- [x] Report the new layout and any remaining limits clearly
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Treat the current OpenAI Codex subagents doc as the source of truth for local agent file shape | This schema is volatile and should not be guessed from memory |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| `codex exec --full-auto ...` did not yield a usable runtime result because local Codex state initialization warned about a `~/.codex/state_5.sqlite` migration mismatch | Treated runtime validation as blocked by the local CLI state layer rather than by the repository config; relied on structural verification and documented the blocker |
