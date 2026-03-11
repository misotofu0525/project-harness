# Managed Codex Home Mirror

## Purpose

This directory is a version-controlled mirror of selected files from `~/.codex/`.

It exists so the project can track:

- the current global `AGENTS.md`
- the shared `project-scaffolds/` templates

without versioning runtime state from the real Codex home directory.

## Scope

Tracked here:

- `AGENTS.md`
- `project-scaffolds/`

Not tracked here:

- auth, sessions, sqlite, caches, logs, or other runtime state

## Notes

- This is a managed copy, not the live runtime directory.
- Changes made here do not automatically update `~/.codex/`.
- Changes made in `~/.codex/` do not automatically update this mirror.
- Sync intentionally stays manual until the workflow becomes stable enough to justify automation.
