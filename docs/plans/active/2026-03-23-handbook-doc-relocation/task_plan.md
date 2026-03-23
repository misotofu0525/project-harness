# Task Plan: Move project current docs into handbook

## Goal
Move the repository's project-currentness docs out of the root into `handbook/`, keep `AGENTS.md` as the root entrypoint, sync all affected repo-local references, and confirm whether the user-level AGENTS layer needs any related change.

## Current Phase
Phase 4

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
- [x] Decide whether shared scaffold or shared skill assets should change for this repo-local move
- [x] Record the user-level AGENTS impact decision
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run structural, placeholder, and diff checks
- [x] Confirm the new root layout and handbook paths
- [ ] Report results and compatibility notes to the user
- **Status:** in_progress

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use `handbook/` instead of `project/` | `handbook/` describes repository operating docs better and avoids the generic ambiguity of `project/` |
| Treat `handbook/` as a repo-local convention for now and leave shared scaffolds plus global AGENTS unchanged | This task changes only this repository's structure; shared assets should change only after a separate convention decision |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| None | N/A |
