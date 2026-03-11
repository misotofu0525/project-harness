# Progress: shared skill reframe

## 2026-03-11

### Started
- Read the managed mirror under `system/codex-home/`.
- Read the live `~/.codex/skills/` layout.
- Confirmed the user clarification changes the intended asset boundary.

### Initial Findings
- `current-docs-sync` should move out of `docs/skills/` and become a shared skill mirrored under `system/codex-home/` and synced into `~/.codex/skills/`.

### Implementation
- Moved `current-docs-sync` from `docs/skills/` into `system/codex-home/skills/current-docs-sync/`.
- Synced the live runtime copy into `~/.codex/skills/current-docs-sync/`.
- Generalized the skill content so it targets scaffolded projects rather than this research repository specifically.
- Rewrote project docs to describe shared skills as managed cross-project assets.

### Verification
- `PYTHONPATH=/tmp/current-docs-sync-validate-deps python3 /Users/misotofu/.codex/skills/.system/skill-creator/scripts/quick_validate.py system/codex-home/skills/current-docs-sync` -> passed
- `rg -n -P '^((?!rg -n).)*(\\[project-name\\]|\\[path-or-none\\]|\\[task-name\\]|\\[TODO:)' AGENTS.md PROJECT_CONTEXT.md ARCHITECTURE.md GOLDEN_PRINCIPLES.md VERIFICATION.md docs system/codex-home --glob '!system/codex-home/project-scaffolds/**'` -> no matches
- `find system/codex-home/skills -maxdepth 3 -type f | sort` -> showed the expected tracked skill files
- `find ~/.codex/skills/current-docs-sync -maxdepth 3 -type f | sort` -> showed the expected live skill files
- `find . -maxdepth 1 -type f | sort` -> confirmed no root-level planning files
