# Task Plan: Generalize custom subagents for cross-project reuse

## Goal
Refactor the repository's project-local custom subagent setup so it keeps only the cross-project-distinct `docs_syncer` role, while relying on official built-in roles for overlapping capabilities.

## Current Phase
Phase 4

## Phases

### Phase 1: Discovery
- [x] Confirm the target direction
- [x] Inspect the current `.codex` agent setup
- [x] Identify all docs that depend on the previous four-role framing
- **Status:** complete

### Phase 2: Configuration Update
- [x] Reduce `.codex/config.toml` to the intended minimal custom role set
- [x] Remove superseded role config files
- **Status:** complete

### Phase 3: Current-Docs Sync
- [x] Update `AGENTS.md`
- [x] Update `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, and `VERIFICATION.md`
- [x] Update any task state or research notes that would otherwise become misleading
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run relevant structural and placeholder checks
- [ ] Commit the result
- [ ] Push if a remote is configured
- **Status:** in_progress

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Keep `docs_syncer` as the only custom role | It expresses a cross-project workflow that is not well-covered by a built-in role |
| Drop custom `explorer`, `docs_researcher`, and `reviewer` roles | They overlap too much with built-in roles or are better expressed via docs, skills, or task strategy |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| No git remote is currently configured | Commit locally first; push requires a remote to exist |
