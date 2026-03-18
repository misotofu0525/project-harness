# Task Plan: Test runtime support for custom project-local agent roles

## Goal
Verify whether this repository's project-local custom agent roles in `.codex/config.toml` can be used at runtime, especially `docs_researcher` and `docs_syncer`.

## Current Phase
Phase 4

## Phases

### Phase 1: Setup
- [x] Confirm the user wants a real runtime test
- [x] Create a task-scoped planning bundle
- [x] Define the exact runtime checks
- **Status:** complete

### Phase 2: Environment Verification
- [x] Check whether the local Codex CLI is installed and usable
- [x] Confirm the repository-local `.codex/config.toml` is present
- **Status:** complete

### Phase 3: Runtime Role Tests
- [x] Test whether a custom read-only role such as `docs_researcher` can be invoked
- [x] Test whether a custom write-capable role such as `docs_syncer` can be invoked
- [x] Distinguish tool-layer limits from repo-config limits
- **Status:** complete

### Phase 4: Delivery
- [x] Record evidence and results
- [ ] Explain what worked, what did not, and why
- **Status:** in_progress

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use real runtime checks instead of inferring from tool docs alone | The user explicitly asked for a test, not a theoretical answer |
| Use temporary marker role config files for the CLI tests | A unique marker in the child agent's raw output is stronger evidence than trusting the parent agent's summary |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| A chained shell command using `rm -f ... && codex exec ...` was blocked by policy | Split cleanup and execution into separate steps |
