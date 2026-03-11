# [project-name] Golden Principles

## Purpose
- This file captures a small number of code taste and architecture preferences for this project.
- Keep it short.
- Prefer rules that can later be enforced by checks, lint rules, or scripts.

## Golden Principles
- Reuse existing utilities, abstractions, and patterns before creating new ones.
- Validate data at boundaries. Do not rely on optimistic shape assumptions.
- Keep module boundaries clear. Avoid cross-layer shortcuts.
- Prefer structured logging and explicit error handling over ad-hoc prints and silent failure.
- Keep changes local. Do not widen scope unless the task requires it.

## Smells To Resist
- Duplicated helpers that drift over time
- Hidden coupling across directories or layers
- Weakly typed or unchecked boundary data
- Large mixed-responsibility modules
- Temporary debug code left in production paths

## Mechanical Follow-Through
- Promote repeated taste issues into lint rules, structural checks, or scripts.
- Prefer checks that produce actionable remediation hints.
- Remove rules that are vague, stale, or not actually enforced.

## Notes
- Keep this file opinionated but small.
- Delete principles that are not genuinely useful for this project.
- If this file grows too much, move specifics into repo-local checks or focused docs.
