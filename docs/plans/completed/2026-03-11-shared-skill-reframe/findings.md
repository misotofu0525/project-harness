# Findings: shared skill reframe

## Boundary Correction
- This repository exists to explore and version workflows that help future projects run better, not to optimize this repository for its own sake.
- Skills produced here should therefore be treated as shared Codex assets for other projects.

## Repository Findings
- The repository currently mirrors global Codex assets under `system/codex-home/`.
- The live Codex home already has `~/.codex/skills/`, but only `.system` skills are present.
- The just-created `docs/skills/current-docs-sync/` copy is misplaced for the clarified goal.

## Working Hypothesis
- Store the tracked copy under `system/codex-home/skills/current-docs-sync/`.
- Sync the live runtime copy to `~/.codex/skills/current-docs-sync/` in the same turn.
- Update repo docs to describe shared skills as managed global assets, not repo-local project docs.

## Final Decisions
- `current-docs-sync` now belongs to the managed shared-skill lane, not the repo-local docs lane.
- The repository should version shared skills under `system/codex-home/skills/`.
- Any change to a managed shared skill should update both the mirror and the live `~/.codex/skills/` copy in the same turn unless explicitly deferred.
