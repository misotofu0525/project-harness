# context-engineering Architecture

## Purpose
- This file is a concise architectural map for humans and agents.
- Keep it factual.
- Update it when structure or critical flows change.

## System Boundaries
- What this system owns:
  - project-level workflow docs
  - preserved research sources and synthesized notes
  - active and completed task planning bundles
- What this system does not own:
  - upstream source content beyond preserved copies
  - external documentation platforms
  - external agent products or frameworks themselves
- Main external dependencies:
  - public blog posts
  - official product documentation
  - arXiv and GitHub content used as research inputs

## Runtime Topology
- Main apps, services, or processes:
  - markdown-first research and curation
  - ad hoc command-line verification
  - project-local Codex configuration with one custom docs-sync subagent layered on top of built-in roles
  - managed shared Codex skills or scripts when workflows stabilize
- Entry points:
  - `AGENTS.md`
  - `handbook/PROJECT_CONTEXT.md`
  - `handbook/ARCHITECTURE.md`
  - `handbook/VERIFICATION.md`
  - `.codex/config.toml`
  - `docs/research/index.zh.md`
- Background jobs or async workers:
  - none

## Key Directories
- `.codex/`: project-local Codex runtime configuration for this repository
- `.codex/agents/`: custom role config layers used only when the built-in roles are not enough
- `handbook/`: project currentness docs kept separate from research outputs and the root entrypoint
- `docs/research/sources/`: preserved source captures with provenance
- `docs/research/notes/`: summaries, comparisons, and synthesized guidance
- `docs/plans/active/`: task-scoped planning bundles in progress
- `docs/plans/completed/`: completed planning bundles for audit and replay
- `memory/`: cross-session task registry
- `system/codex-home/`: version-controlled mirror of selected global Codex policy and scaffold files
- `system/codex-home/skills/`: version-controlled mirror of shared Codex skills intended for other projects

## Critical Flows
- Subagent policy layering:
  - starts at: stable delegation rules in the global AGENTS layer
  - passes through: project-specific custom-role rules in the repository `AGENTS.md`
  - writes to or affects: consistent subagent usage without overloading either layer
- Local multi-agent task execution:
  - starts at: user request or parent agent decision
  - passes through: built-in roles by default, and `.codex/config.toml` plus `.codex/agents/docs-syncer.toml` when a current-doc sync action is needed
  - writes to or affects: a single scoped documentation update under `handbook/` plus related indexes or task state when the custom role is used
- Source capture:
  - starts at: external article, paper, repo, or official documentation
  - passes through: `docs/research/sources/` and optionally `docs/research/notes/`
  - writes to or affects: synthesized guidance and project operating docs
- System asset curation:
  - starts at: shared policy, scaffold, or skill changes intended for future projects
  - passes through: `system/codex-home/`
  - writes to or affects: tracked global AGENTS, shared scaffold templates, mirrored shared skills, and the live `~/.codex/` copy
- Task execution:
  - starts at: user request
  - passes through: `docs/plans/active/<task>/`
  - writes to or affects: repository docs, then `docs/plans/completed/<task>/`

## Invariants
- Root should contain `AGENTS.md` and only intentionally high-signal top-level project files.
- Project currentness docs should live under `handbook/`, not in the root.
- The shared project scaffold should default to `AGENTS.md` in the root and the rest of the current docs under `handbook/`.
- Cross-project subagent delegation rules should live in the global AGENTS layer, while repository-specific custom subagent rules should live in the project AGENTS layer.
- Project-local custom subagent roles should stay rare and should only exist when they express cross-project value that built-in roles do not cover well.
- Preserved source captures must retain provenance metadata.
- Task planning must live under `docs/plans/`, not in the repository root.
- Project operating docs must reflect the actual directory structure and workflow.
- Shared Codex skills should live under `system/codex-home/skills/` and sync to the live `~/.codex/skills/` copy when intentionally changed.
- The managed `system/codex-home/` mirror must exclude runtime state and stay limited to policy, scaffold, and shared skill assets.

## Hotspots
- High-risk module: `AGENTS.md`, because it controls project routing
- High-change area: `.codex/`, `handbook/`, `system/codex-home/project-scaffolds/`, and `system/codex-home/skills/`
- Expensive or slow path: keeping references and directory structure synchronized after moves

## Useful Entry Points
- Read first for feature work: `handbook/PROJECT_CONTEXT.md`
- Read first for debugging: `handbook/VERIFICATION.md`
- Read first for verification: `handbook/VERIFICATION.md`

## Notes
- Prefer short maps over long prose.
- Link to deeper docs only when they already exist.
- Move transient task detail into plan artifacts, not this file.
