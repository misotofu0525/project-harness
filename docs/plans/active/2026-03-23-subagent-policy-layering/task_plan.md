# Task Plan: Layer subagent policy across global and project AGENTS

## Goal
Place stable cross-project subagent rules in the global AGENTS layer, place repository-specific subagent rules in the project AGENTS layer, and sync related current docs.

## Current Phase
Phase 4

## Phases

### Phase 1: Discovery
- [x] Confirm the requested layering
- [x] Read the current global and project AGENTS files
- [x] Identify which related current docs need syncing
- **Status:** complete

### Phase 2: Policy Update
- [x] Update the managed global AGENTS mirror
- [x] Update the live `~/.codex/AGENTS.md`
- [x] Update the project `AGENTS.md`
- **Status:** complete

### Phase 3: Current-Docs Sync
- [x] Update `PROJECT_CONTEXT.md`
- [x] Update `ARCHITECTURE.md`
- [x] Update `VERIFICATION.md`
- [x] Update task state if needed
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run structural and placeholder checks
- [x] Confirm mirror/live global AGENTS alignment
- [ ] Report results to the user
- **Status:** in_progress

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Keep the full theory in research notes and write only compressed executable rules into AGENTS files | Preserves context layering and keeps AGENTS practical |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| None | N/A |
