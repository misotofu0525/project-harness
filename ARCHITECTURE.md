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
  - managed shared Codex skills or scripts when workflows stabilize
- Entry points:
  - `AGENTS.md`
  - `PROJECT_CONTEXT.md`
  - `docs/research/index.zh.md`
- Background jobs or async workers:
  - none

## Key Directories
- `docs/research/sources/`: preserved source captures with provenance
- `docs/research/notes/`: summaries, comparisons, and synthesized guidance
- `docs/plans/active/`: task-scoped planning bundles in progress
- `docs/plans/completed/`: completed planning bundles for audit and replay
- `memory/`: cross-session task registry
- `system/codex-home/`: version-controlled mirror of selected global Codex policy and scaffold files
- `system/codex-home/skills/`: version-controlled mirror of shared Codex skills intended for other projects

## Critical Flows
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
- Root should contain only entry docs and intentionally high-signal project files.
- Preserved source captures must retain provenance metadata.
- Task planning must live under `docs/plans/`, not in the repository root.
- Project operating docs must reflect the actual directory structure and workflow.
- Shared Codex skills should live under `system/codex-home/skills/` and sync to the live `~/.codex/skills/` copy when intentionally changed.
- The managed `system/codex-home/` mirror must exclude runtime state and stay limited to policy, scaffold, and shared skill assets.

## Hotspots
- High-risk module: `AGENTS.md`, because it controls project routing
- High-change area: `PROJECT_CONTEXT.md`, `VERIFICATION.md`, and `system/codex-home/`
- Expensive or slow path: keeping references and directory structure synchronized after moves

## Useful Entry Points
- Read first for feature work: `PROJECT_CONTEXT.md`
- Read first for debugging: `VERIFICATION.md`
- Read first for verification: `VERIFICATION.md`

## Notes
- Prefer short maps over long prose.
- Link to deeper docs only when they already exist.
- Move transient task detail into plan artifacts, not this file.
