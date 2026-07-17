---
name: setup-project
description: Install or migrate the minimal Project Harness project layer in a code repository. Use when a user asks to set up Project Harness, add AGENTS.md and CLAUDE.md routing, configure task Journals, or adopt the harness in an existing project without copying user-Home configuration.
---

# Setup Project Harness

1. Inspect the repository before writing. Identify existing `AGENTS.md`, `CLAUDE.md`, project commands, stable context documents, and any planning convention.
2. Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.codex-plugin/` manifest.
3. For a new project layer with no conflicting files, run:

   ```bash
   python3 <plugin-root>/lib/setup-project.py \
     --project-root <target-repository> \
     --fast "<verified-fast-command>" \
     --full "<verified-full-command>"
   ```

4. For an existing project, do not overwrite entry files. Use the packaged files under `<plugin-root>/templates/` as merge references and make the smallest compatible edits.
5. Keep the root `AGENTS.md` as a kernel/router. Put stable, decision-relevant project knowledge under `docs/agent/` and list only existing modules in `docs/agent/index.md`.
6. Keep `CLAUDE.md` thin and import `@AGENTS.md`. Create `.claude/rules/` files only for real path-specific conventions, and include `paths` frontmatter in every rule.
7. Create `docs/plans/active/` and `docs/plans/completed/`, but do not create a Journal for a simple task or merely because setup ran.
8. Confirm `.harness.toml` contains real project commands. Do not invent commands or leave placeholders.
9. Verify the installed paths and run the configured fast check before reporting success.
