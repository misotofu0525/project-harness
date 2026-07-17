---
name: setup-project
description: Install or migrate the minimal Project Harness project layer in a code repository. Use when a user asks to set up Project Harness, add AGENTS.md and CLAUDE.md routing, configure task Journals, or adopt the harness in an existing project without copying user-Home configuration.
---

# Setup Project Harness

1. Inspect the repository before writing. Identify existing `AGENTS.md`, `CLAUDE.md`, project commands, stable context documents, and any planning convention.
2. Resolve `<plugin-root>` as the parent of this Skill's `skills/` directory, identified by its `.claude-plugin/` manifest.
3. For a new project layer with no conflicting files, run `python3 <plugin-root>/lib/setup-project.py --project-root <target-repository>` with one `--fast` argument per verified fast command and one `--full` argument per verified full command.
4. For an existing project, do not overwrite entry files. Use `<plugin-root>/templates/` as merge references and make the smallest compatible edits.
5. Keep `AGENTS.md` as a kernel/router, keep `CLAUDE.md` as an `@AGENTS.md` import, and create only the scoped context modules the project needs.
6. Add `.claude/rules/` only for real path-specific conventions. Every rule must include `paths` frontmatter.
7. Create the active/completed plan roots, but do not create a Journal during setup.
8. Confirm `.harness.toml` contains real commands and run the configured fast verification.
