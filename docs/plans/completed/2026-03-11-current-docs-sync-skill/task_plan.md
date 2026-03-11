# Task Plan: Add repo-local current-docs-sync skill

## Goal
Add the first repo-local skill for syncing current project docs after repository structure or operating-convention changes, and wire it into the repository routing docs.

## Current Phase
Phase 5

## Phases

### Phase 1: Requirements & Discovery
- [x] Confirm current repo conventions and skill placement
- [x] Verify current Codex skill guidance that affects repository integration
- [x] Document findings in findings.md
- **Status:** complete

### Phase 2: Planning & Structure
- [x] Choose the repo-local skill directory
- [x] Define the skill trigger and resource structure
- [x] Define which project docs must be updated together
- **Status:** complete

### Phase 3: Implementation
- [x] Create the skill files
- [x] Update routing and entry docs
- [x] Keep planning files current
- **Status:** complete

### Phase 4: Testing & Verification
- [x] Run skill validation
- [x] Run repository verification checks
- [x] Record results in progress.md
- **Status:** complete

### Phase 5: Delivery
- [x] Review outputs
- [x] Deliver to user
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Use a task-scoped planning bundle under `docs/plans/active/` | Required by the project workflow for multi-step design work |
| Store repo-local skills under `docs/skills/` | Keeps the repository root thin while giving `AGENTS.md` one stable local skill directory |
| Start with `current-docs-sync` instead of a broader meta-skill | The repo needed a narrow, repeatable recipe for keeping current docs synchronized |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| `quick_validate.py` failed because `yaml` was missing in the environment | Installed `PyYAML` into a temporary `/tmp` target and reran the validator with `PYTHONPATH` |
