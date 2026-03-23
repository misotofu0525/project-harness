# Task Plan: Make handbook the shared current-doc default

## Goal
Move the repository's project-currentness docs out of the root into `handbook/`, then promote that layout into the shared scaffold and shared docs-sync defaults while keeping managed and live copies synchronized.

## Current Phase
Complete

## Phases

### Phase 1: Discovery
- [x] Confirm the desired target directory name
- [x] Inspect current root docs, project routing, and verification commands
- [x] Check whether the user-level `~/.codex/AGENTS.md` is coupled to the current project-local paths
- **Status:** complete

### Phase 2: Path Migration
- [x] Move `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `GOLDEN_PRINCIPLES.md`, and `VERIFICATION.md` into `handbook/`
- [x] Update `AGENTS.md` canonical paths and load order
- [x] Update repo-local direct references that would become stale after the move
- **Status:** complete

### Phase 3: Currentness Sync
- [x] Sync any affected repository-state docs, research notes, and task state
- [x] Promote the `handbook/` layout into the shared scaffold defaults
- [x] Update the shared `current-docs-sync` skill to match the new default
- [x] Record the user-level AGENTS impact decision
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run structural, placeholder, and diff checks
- [x] Confirm the new root layout and handbook paths
- [x] Confirm managed and live scaffold plus shared-skill alignment
- [x] Report results and compatibility notes to the user
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use `handbook/` instead of `project/` | `handbook/` describes repository operating docs better and avoids the generic ambiguity of `project/` |
| Promote `handbook/` into the shared scaffold and shared docs-sync defaults | The user explicitly wants the scaffold updated, and the new layout is now the intended cross-project default |
| Leave the global AGENTS layer unchanged | Global AGENTS only points to the scaffold lookup location; it does not encode these project-local file paths |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| None | N/A |
