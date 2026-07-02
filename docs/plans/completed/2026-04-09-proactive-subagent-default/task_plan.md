# Task Plan: Reframe proactive subagent usage under current Codex constraints

## Goal
Diagnose why the current repository guidance does not lead to proactive subagent use, align the guidance with current official Codex behavior, and update the repo so future sessions use the best available workaround instead of assuming automatic delegation exists.

## Current Phase
Phase 4

## Phases

### Phase 1: Discovery
- [x] Read the project routing docs and current multi-agent config
- [x] Inspect existing subagent research notes and active plan history
- [x] Verify current official Codex behavior around subagent triggering
- **Status:** complete

### Phase 2: Diagnosis
- [x] Identify the gap between repository expectations and product behavior
- [x] Decide which parts are a product constraint vs a repo-policy problem
- [x] Define the smallest durable remediation
- **Status:** complete

### Phase 3: Repo Update
- [x] Update the relevant policy, research, or current-doc files
- [x] Sync any managed-vs-live global policy files if global rules change
- [x] Update task memory or active research indexes if needed
- **Status:** complete

### Phase 4: Verification & Delivery
- [x] Run the relevant structural and placeholder checks
- [x] Summarize the new operating model and remaining limitations
- **Status:** complete

## Decisions Made
| Decision | Rationale |
|----------|-----------|
| Treat this as a workflow reframing task, not a prompt-strengthening task | Official Codex docs currently state that subagents are not spawned automatically |

## Errors Encountered
| Error | Resolution |
|-------|------------|
| The placeholder scan command in `handbook/VERIFICATION.md` failed under JSON-plus-shell escaping during this session | Re-ran the same PCRE pattern with a safer shell form; the check completed with no matches |
