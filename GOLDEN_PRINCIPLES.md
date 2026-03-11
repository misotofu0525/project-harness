# context-engineering Golden Principles

## Purpose
- This file captures a small number of workflow and repository design preferences for this project.
- Keep it short.
- Prefer rules that can later be enforced by checks, scripts, or skills.

## Golden Principles
- Keep the repository root thin; entry docs belong in root, durable research belongs under `docs/`.
- Preserve provenance. Raw source captures and synthesized notes should remain clearly separated.
- Update project-level docs when repository structure or operating conventions change.
- Prefer explicit file paths and small, reviewable edits over broad rewrites.
- Keep transient work in task bundles under `docs/plans/`, not in the root or chat history.

## Smells To Resist
- Root directory clutter
- Duplicate summaries of the same source in multiple places
- Stale absolute links after file moves
- Mixing raw source text with downstream interpretation
- Temporary planning files left in visible top-level locations

## Mechanical Follow-Through
- Promote repeated repository-structure checks into verification commands.
- Prefer checks that catch placeholder text, stale paths, and root-level planning drift.
- Remove stale notes or duplicate artifacts instead of letting them accumulate.

## Notes
- Keep this file opinionated but small.
- If this file grows too much, move specifics into verification scripts or focused docs.
