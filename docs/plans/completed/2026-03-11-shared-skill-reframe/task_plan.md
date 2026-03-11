# Task Plan: Reframe current-docs-sync as a shared skill

## Goal
Correct the placement and framing of `current-docs-sync` so it becomes a shared cross-project Codex skill mirrored in the repository and synced to the live `~/.codex/skills/` directory.

## Current Phase
Phase 5

## Phases

### Phase 1: Requirements & Discovery
- [x] Confirm the correct boundary between this research repo and shared runtime assets
- [x] Inspect the managed mirror and live `~/.codex/skills/` layout
- [x] Document the correction in findings.md
- **Status:** complete

### Phase 2: Planning & Migration
- [x] Choose the managed mirror path for shared skills
- [x] Define which docs must be corrected
- [x] Define how to keep mirror and live copies aligned
- **Status:** complete

### Phase 3: Implementation
- [x] Generalize the skill content for cross-project use
- [x] Move the skill into the managed mirror
- [x] Sync the live `~/.codex/skills/` copy
- [x] Remove the misplaced repo-local copy
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Validate the shared skill structure
- [x] Verify mirror and live copies exist
- [x] Verify project docs no longer describe the skill as repo-local
- **Status:** complete

### Phase 5: Delivery
- [x] Review outputs
- [x] Deliver to user
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Start a corrective task bundle instead of rewriting the previous completed bundle | Preserves audit history and makes the boundary correction explicit |
| Store shared skills under `system/codex-home/skills/` and sync them to `~/.codex/skills/` | Matches the clarified cross-project goal and keeps runtime assets usable outside this repo |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| The earlier implementation treated `current-docs-sync` as a repo-local skill | Reframed it as a shared skill, moved it into the managed mirror, and synced the live copy |
