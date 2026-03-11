# Findings & Decisions

## Requirements
- Sync the system-level project templates into the current directory.
- Treat this repository as a harness-engineering research project.
- Organize previously collected articles and synthesis notes.
- Remove temporary files from the root.

## Research Findings
- Current root files were a mix of preserved source material and temporary planning files.
- The repository benefits from the same thin-root structure advocated in the collected materials.
- Previous planning artifacts are useful for traceability, so moving them into `docs/plans/completed/` is better than deleting them.
- Research outputs naturally separate into preserved sources and synthesized notes.
- System-level Codex assets can be versioned inside the repository without colliding with runtime behavior if they are mirrored under a non-runtime path.
- A managed mirror is safer than putting a live `.codex/` directory inside the repo, because it avoids confusion with real runtime config.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Create root-level entry docs from the system scaffold, but fill them with project-specific research context | Keeps the repository navigable for future Codex sessions |
| Introduce `docs/research/index.zh.md` as the first research entrypoint | Avoids forcing future sessions to scan individual note files blindly |
| Mirror selected `~/.codex` files under `system/codex-home/` instead of a project-local `.codex/` directory | Keeps the mirror version-controlled without making it look like the live runtime home |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| Old absolute links pointed to pre-move root paths | Update moved notes and archived findings after relocation |

## Resources
- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `ARCHITECTURE.md`
- `GOLDEN_PRINCIPLES.md`
- `VERIFICATION.md`
- `docs/research/index.zh.md`
- `system/codex-home/`
