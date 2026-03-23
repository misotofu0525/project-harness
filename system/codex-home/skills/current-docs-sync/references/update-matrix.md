# Current Docs Sync Matrix

Use this as the default target matrix for projects that follow the shared `AGENTS.md` plus `handbook/` current-doc scaffold.

## Always Evaluate

### `AGENTS.md`
- Update when adding, removing, renaming, or relocating skill references.
- Update when canonical paths, load order, or routing rules change.
- Keep it as a router, not a knowledge base.

### `handbook/PROJECT_CONTEXT.md`
- Update when current focus, key directories, current stage, risks, or next recommended step changes.
- Update the session handoff block after durable workflow changes.
- Keep it factual and current.

### `handbook/ARCHITECTURE.md`
- Update when system boundaries, runtime topology, key directories, invariants, or critical flows change.
- Add new flows only when they are durable enough to matter to future sessions.

### `handbook/VERIFICATION.md`
- Update when canonical checks, structural checks, or required completion gates change.
- Prefer simple commands that verify the actual repository layout and skill presence.

## Update Conditionally

### `handbook/GOLDEN_PRINCIPLES.md`
- Update only if workflow taste or repository design preferences changed.
- Do not edit it for one-off implementation details.

### Any project index
- Update only if the target project keeps a durable index and the referenced content moved or changed.

### Any task registry
- Update only if the target project keeps cross-session state and the task changes it.
- Do not duplicate detail already captured in a planning bundle or the project's equivalent.

## Minimal Sync Procedure

1. Inspect the concrete repository change.
2. List which entry docs are now stale.
3. Update only the stale docs.
4. Run the relevant checks from `handbook/VERIFICATION.md`.
5. Do not claim sync is complete without fresh verification evidence.

## Smells

- Editing `handbook/PROJECT_CONTEXT.md` without updating `handbook/ARCHITECTURE.md` or `handbook/VERIFICATION.md` after a structural change
- Adding a skill reference without routing to it from `AGENTS.md` when the project depends on that route
- Leaving placeholder text in a new `SKILL.md`
- Turning entry docs into verbose explanations instead of current operational state
