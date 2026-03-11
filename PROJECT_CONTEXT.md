# context-engineering Context

## Overview
- What this project is: a research repository for exploring harness engineering, context engineering, and durable Codex workflows.
- Primary users or consumers: the repository owner and future Codex sessions working on workflow design.
- Current stage: initial project bootstrap with collected source material and synthesized research notes.

## Canonical Docs
- Architecture: `ARCHITECTURE.md`
- Golden principles: `GOLDEN_PRINCIPLES.md`
- Verification: `VERIFICATION.md`
- Research index: `docs/research/index.zh.md`

## Success Criteria
- Root stays thin and predictable.
- Research materials are preserved with clear provenance and structure.
- Project-level docs reflect the actual repository layout and workflow.
- Temporary planning files are kept under `docs/plans/`, not in the repository root.

## Architecture
- Main entry points: `AGENTS.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `VERIFICATION.md`, `docs/research/index.zh.md`
- Key directories: `docs/research/sources/`, `docs/research/notes/`, `docs/plans/active/`, `docs/plans/completed/`, `memory/`, `system/codex-home/`
- External services or dependencies: official OpenAI and Anthropic docs, arXiv, public blog posts, and selected public repositories used as research inputs
- Important data flows:
  - source capture -> summary or comparison -> synthesized guidance
  - task planning -> repository edits -> completed plan archive

## Commands
- Setup: `none`
- Dev: `none`
- Fast verify: `find . -maxdepth 2 -type f | sort`
- Full verify: `rg -n '\\[project-name\\]|\\[path-or-none\\]|\\[command|\\[task-name\\]' AGENTS.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md docs`
- Build: `none`
- Lint: `none`

## Current Focus
- Current priority: turn this directory into a durable research project rather than a loose pile of notes.
- In-scope work:
  - project-level bootstrap docs
  - research directory structure
  - planning bundle cleanup
  - version-controlled mirror of global Codex policy and scaffolds
  - future workflow and skill design grounded in collected material
- Out-of-scope work:
  - application code
  - production automation
  - CI until local workflows stabilize

## Risks and Constraints
- Known risk: advice about external tools and products can go stale quickly.
- Performance or reliability constraint: repository structure should remain cheap to read and easy for Codex to navigate.
- Security or compliance constraint: no secrets or private credentials should ever be stored in this repository.

## Decisions
| Decision | Rationale | Date |
|----------|-----------|------|
| Keep global rules thin and push project specifics into repo-local docs | Reduces cross-project context pollution | 2026-03-11 |
| Store research sources under `docs/research/sources/` and syntheses under `docs/research/notes/` | Separates raw material from interpretation | 2026-03-11 |
| Store planning files as task bundles under `docs/plans/` | Keeps root uncluttered and preserves task traceability | 2026-03-11 |
| Mirror selected `~/.codex` policy and scaffold files under `system/codex-home/` | Allows the research project to version system-level prompt and scaffold assets without storing runtime state | 2026-03-11 |

## Session Handoff
- Last updated: 2026-03-11
- Current task: bootstrap the repository as a harness-engineering research project and clean up root-level temporary files.
- What changed recently:
  - created project-level entry docs
  - created `docs/research/` and `docs/plans/` structure
  - moved previous research and planning artifacts out of the root
  - mirrored selected `~/.codex` files into `system/codex-home/`
- Next recommended step: turn the current research conclusions into repo-local workflows or skills only when they become repetitive enough.
- Known blocker: repo-local skills for verification and current-docs do not exist yet.

## Notes
- Keep this file factual, current, and short.
- This is project state, not a long knowledge base.
- Move transient planning into `docs/plans/active/<task>/` when needed.
