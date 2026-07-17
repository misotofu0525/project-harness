# Distribution

## Read when

- changing manifests, skills, lifecycle hooks, or plugin packaging
- changing canonical-to-packaged asset synchronization
- validating or releasing either adapter

## Stable context

- The Codex plugin root is `plugins/codex/project-harness/` and requires `.codex-plugin/plugin.json`.
- The Claude Code plugin root is `plugins/claude-code/project-harness/` and uses `.claude-plugin/plugin.json`.
- Both platforms discover skills and `hooks/hooks.json` at plugin root.
- Codex hook commands use `${PLUGIN_ROOT}`; Claude Code hook commands use `${CLAUDE_PLUGIN_ROOT}`.
- Codex PreCompact ignores plain stdout, so the shared adapter emits supported JSON.
- V1 packages SessionStart and PreCompact only. Stop is intentionally absent.
- Run `shared/scripts/sync-plugin-runtime.py` after changing canonical shared scripts or templates.

## Update when

- an official manifest or hook contract changes
- plugin roots or synchronized asset sets change
- a new platform adapter is added
