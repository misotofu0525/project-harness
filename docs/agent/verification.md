# Verification

## Read when

- changing shared scripts, templates, plugin adapters, or tests
- preparing explicit task completion

## Stable context

- `.harness.toml` is the machine-readable source for fast and full commands.
- Fast feedback: `python3 -m unittest discover -s tests -p 'test_harness_core.py' -v`.
- Full behavior: `python3 -m unittest discover -s tests -v`.
- Packaged parity: `python3 shared/scripts/sync-plugin-runtime.py --check`.
- Diff hygiene: `git diff --check`.
- Validate the Codex plugin with the current `plugin-creator` validator.
- Validate each Codex skill with the current `skill-creator` `quick_validate.py`.
- Validate the Claude Code plugin with `claude plugin validate plugins/claude-code/project-harness` when the local CLI provides that command.
- Scan distributable and current-context files for placeholders, retired paths, and local absolute links.

## Update when

- `.harness.toml`, test entrypoints, validator commands, or required delivery gates change
