---
name: current-docs-sync
description: Sync scaffolded project docs after changes to repository structure, canonical paths, operating conventions, skill wiring, or verification commands. Use when a target project follows the AGENTS.md plus handbook current-doc convention and Codex needs to bring those files back into sync after structural or workflow changes.
---

# Current Docs Sync

Re-read the target project state and update only the current docs that became stale.

Assume the target project follows the shared scaffold centered on `AGENTS.md`, `handbook/PROJECT_CONTEXT.md`, `handbook/ARCHITECTURE.md`, and `handbook/VERIFICATION.md`. If the project uses different file names or locations, map the local equivalents first.

Use this skill for project-currentness work, not for general writing or research synthesis.

## Workflow

### 1. Confirm the change surface

- Inspect the concrete repository change before editing docs.
- Prefer `git diff --stat`, `find`, and targeted reads over broad rewrites.
- Distinguish between:
  - structural changes
  - operating-convention changes
  - project-specific content changes
  - one-off note edits that do not require current-doc sync

### 2. Read the stale targets

- Always evaluate `AGENTS.md`, `handbook/PROJECT_CONTEXT.md`, `handbook/ARCHITECTURE.md`, and `handbook/VERIFICATION.md`.
- Read `handbook/GOLDEN_PRINCIPLES.md`, any project index, or any task registry only if the target project uses them and the change touches their scope.
- Use [`references/update-matrix.md`](references/update-matrix.md) to map the change to the minimum required docs.

### 3. Sync the docs together

- If the repository structure or operating conventions changed, update `handbook/PROJECT_CONTEXT.md`, `handbook/ARCHITECTURE.md`, and `handbook/VERIFICATION.md` in the same turn.
- If the change adds or renames a skill reference, update `AGENTS.md` routing in the same turn.
- Preserve the target project's documented directory rules. If it uses the shared scaffold defaults, keep `AGENTS.md` in the root and keep current docs explicit under `handbook/`.
- Preserve the difference between:
  - current project state
  - architecture facts
  - verification commands
  - workflow taste

### 4. Keep the edits narrow

- Do not rewrite unaffected sections.
- Do not add speculative future structure.
- Do not duplicate the same rule in multiple files when one router reference is enough.
- Prefer explicit file paths over vague references.

### 5. Verify before declaring completion

- Run the relevant checks from `handbook/VERIFICATION.md`.
- If a new skill was added, validate it with `quick_validate.py`.
- Record fresh verification evidence in the active task bundle or reply.
- Do not claim the docs are synced based on intent alone.

## Trigger Examples

- "We moved planning files and need the entry docs brought up to date."
- "Add a shared or local skill and wire the project docs to it."
- "We changed verification commands; sync the current docs."
- "The architecture map and project context no longer match the repo."

## Exit Criteria

- The changed repository facts are reflected in the minimum required docs.
- `AGENTS.md` routes to any new or renamed skill reference when applicable.
- No placeholder text remains in the skill or entry docs.
- Relevant verification commands have been run successfully.

## Reference

- Use [`references/update-matrix.md`](references/update-matrix.md) when deciding which docs must move together.
