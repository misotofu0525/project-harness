# context-engineering Context

## Overview
- What this project is: a research repository for exploring harness engineering, context engineering, and durable Codex workflows.
- Primary users or consumers: the repository owner and future Codex sessions working on reusable workflows, scaffolds, and shared Codex assets for other projects.
- Current stage: early workflow codification on top of the initial project bootstrap and collected research notes.

## Canonical Docs
- Architecture: `ARCHITECTURE.md`
- Golden principles: `GOLDEN_PRINCIPLES.md`
- Verification: `VERIFICATION.md`
- Project-local Codex config: `.codex/config.toml`
- Managed shared skills mirror: `system/codex-home/skills/`
- Research index: `docs/research/index.zh.md`

## Success Criteria
- Root stays thin and predictable.
- Research materials are preserved with clear provenance and structure.
- Project-level docs reflect the actual repository layout and workflow.
- Temporary planning files are kept under `docs/plans/`, not in the repository root.

## Architecture
- Main entry points: `AGENTS.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `VERIFICATION.md`, `.codex/config.toml`, `docs/research/index.zh.md`
- Key directories: `.codex/`, `.codex/agents/`, `docs/research/sources/`, `docs/research/notes/`, `docs/plans/active/`, `docs/plans/completed/`, `memory/`, `system/codex-home/`, `system/codex-home/skills/`
- External services or dependencies: official OpenAI and Anthropic docs, arXiv, public blog posts, and selected public repositories used as research inputs
- Important data flows:
  - source capture -> summary or comparison -> synthesized guidance
  - task planning -> repository edits -> completed plan archive

## Commands
- Setup: `none`
- Dev: `none`
- Fast verify: `find . -maxdepth 2 -type f | sort`
- Full verify: `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md PROJECT_CONTEXT.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md VERIFICATION.md .codex docs system/codex-home --glob '!system/codex-home/project-scaffolds/**'`
- Build: `none`
- Lint: `none`

## Current Focus
- Current priority: codify durable Codex workflow patterns in-repo, including project-local multi-agent conventions.
- In-scope work:
  - project-level bootstrap docs
  - research directory structure
  - planning bundle cleanup
  - project-local multi-agent config
  - version-controlled mirror of global Codex policy and scaffolds
  - shared workflow and skill design grounded in collected material
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
| Store shared Codex skills under `system/codex-home/skills/` and sync them to `~/.codex/skills/` | Keeps reusable cross-project workflow assets versioned in the research repo and usable in future projects | 2026-03-11 |
| Store repository-specific multi-agent role definitions under project-local `.codex/` files | Keeps agent behavior versioned with the repository while leaving the global config thin | 2026-03-12 |

## Session Handoff
- Last updated: 2026-03-12
- Current task: add project-local multi-agent configuration for the repository and sync the affected current docs.
- What changed recently:
  - created project-level entry docs
  - created `docs/research/` and `docs/plans/` structure
  - moved previous research and planning artifacts out of the root
  - mirrored selected `~/.codex` files into `system/codex-home/`
  - added the first shared skill at `system/codex-home/skills/current-docs-sync/` and synced it to `~/.codex/skills/current-docs-sync/`
  - added a project-local `.codex/config.toml` with narrow multi-agent role definitions under `.codex/agents/`
- Next recommended step: dogfood the local agent roles on a real repository task and decide whether to extract a reusable scaffold pattern.
- Known blocker: no repository-local smoke test exists yet for validating agent role config beyond structural checks.

## Notes
- Keep this file factual, current, and short.
- This is project state, not a long knowledge base.
- Move transient planning into `docs/plans/active/<task>/` when needed.
