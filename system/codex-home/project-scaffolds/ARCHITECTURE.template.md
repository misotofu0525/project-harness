# [project-name] Architecture

## Purpose
- This file is a concise architectural map for humans and agents.
- Keep it factual.
- Update it when structure or critical flows change.

## System Boundaries
- What this system owns:
- What this system does not own:
- Main external dependencies:

## Runtime Topology
- Main apps, services, or processes:
- Entry points:
- Background jobs or async workers:

## Key Directories
- `path/`: purpose
- `path/`: purpose
- `path/`: purpose

## Critical Flows
- Flow name:
  - starts at:
  - passes through:
  - writes to or affects:
- Flow name:
  - starts at:
  - passes through:
  - writes to or affects:

## Invariants
- What must always be true:
- What must never happen:
- What is especially easy to break:

## Hotspots
- High-risk module:
- High-change area:
- Expensive or slow path:

## Useful Entry Points
- Read first for feature work: `[path-or-none]`
- Read first for debugging: `[path-or-none]`
- Read first for verification: `[path-or-none]`

## Notes
- Prefer short maps over long prose.
- Link to deeper docs only when they already exist.
- Move transient task detail into plan artifacts, not this file.
