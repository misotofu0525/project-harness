# context-engineering Context

## Overview
- What this project is: a research repository for exploring harness engineering, context engineering, and durable Codex workflows.
- Primary users or consumers: the repository owner and future Codex sessions working on reusable workflows, scaffolds, and shared Codex assets for other projects.
- Current stage: early workflow codification on top of the initial project bootstrap and collected research notes.

## Canonical Docs
- Architecture: `handbook/ARCHITECTURE.md`
- Golden principles: `handbook/GOLDEN_PRINCIPLES.md`
- Verification: `handbook/VERIFICATION.md`
- Project-local Codex config: `.codex/config.toml`
- Project-local custom subagent config: `.codex/agents/docs-syncer.toml`
- Subagent design note: `docs/research/notes/subagent-definition-principles.zh.md`
- Managed shared skills mirror: `system/codex-home/skills/`
- Research index: `docs/research/index.zh.md`

## Success Criteria
- Root stays thin and predictable, with `AGENTS.md` as the project entrypoint and current docs under `handbook/`.
- Research materials are preserved with clear provenance and structure.
- Project-level docs reflect the actual repository layout and workflow.
- Temporary planning files are kept under `docs/plans/`, not in the repository root.

## Architecture
- Main entry points: `AGENTS.md`, `handbook/PROJECT_CONTEXT.md`, `handbook/ARCHITECTURE.md`, `handbook/VERIFICATION.md`, `.codex/config.toml`, `docs/research/index.zh.md`
- Key directories: `.codex/`, `.codex/agents/`, `handbook/`, `docs/research/sources/`, `docs/research/notes/`, `docs/plans/active/`, `docs/plans/completed/`, `memory/`, `system/codex-home/`, `system/codex-home/skills/`
- External services or dependencies: official OpenAI and Anthropic docs, arXiv, public blog posts, and selected public repositories used as research inputs
- Important data flows:
  - source capture -> summary or comparison -> synthesized guidance
  - task planning -> repository edits -> completed plan archive

## Commands
- Setup: `none`
- Dev: `none`
- Fast verify: `find . -maxdepth 2 -type f | sort`
- Full verify: `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md handbook .codex docs memory system/codex-home --glob '!system/codex-home/project-scaffolds/**'`
- Build: `none`
- Lint: `none`

## Current Focus
- Current priority: codify durable Codex workflow patterns in-repo, including a minimal cross-project custom subagent pattern.
- In-scope work:
  - project-level bootstrap docs
  - research directory structure
  - planning bundle cleanup
  - project-local multi-agent config
  - minimal custom subagent design for cross-project reuse
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
| Keep only `docs_syncer` as a custom cross-project subagent role and rely on built-in roles for overlapping capabilities | Minimizes custom surface area while preserving the repository's durable docs-sync workflow | 2026-03-22 |
| Keep generic subagent delegation rules in the global AGENTS layer and repository-specific custom subagent rules in the project AGENTS layer | Preserves context layering and keeps the project router practical | 2026-03-23 |
| Keep only `AGENTS.md` at the root as the project router and move project current-doc files into `handbook/` | Separates repository operating docs from research outputs while preserving a standard root entrypoint | 2026-03-23 |

## Session Handoff
- Last updated: 2026-03-23
- Current task: move project current-doc files into `handbook/` while keeping `AGENTS.md` as the root router and preserving repo-local currentness.
- What changed recently:
  - created project-level entry docs
  - created `docs/research/` and `docs/plans/` structure
  - moved previous research and planning artifacts out of the root
  - mirrored selected `~/.codex` files into `system/codex-home/`
  - added the first shared skill at `system/codex-home/skills/current-docs-sync/` and synced it to `~/.codex/skills/current-docs-sync/`
  - added a project-local `.codex/config.toml` and then reduced the custom role set to a single cross-project `docs_syncer` role under `.codex/agents/`
  - added a stable global subagent policy to the managed and live global AGENTS layer, and kept only repository-specific `docs_syncer` rules in the project AGENTS layer
  - moved `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `GOLDEN_PRINCIPLES.md`, and `VERIFICATION.md` from the root into `handbook/`, and updated repo-local routing and verification paths accordingly
- Next recommended step: decide whether the `handbook/` layout should stay repo-local or be generalized into the shared scaffold.
- Known blocker: none currently.

## Notes
- Keep this file factual, current, and short.
- This is project state, not a long knowledge base.
- Move transient planning into `docs/plans/active/<task>/` when needed.
