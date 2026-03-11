# Global rules for Codex

## Purpose
- This global file is a router, not a knowledge base.
- Keep only stable cross-project rules here.
- Load project-specific context only when it is relevant to the current task.
- Shared templates may exist for bootstrapping project-level docs, but templates are scaffolding, not default runtime context.
- If shared bootstrap templates are present, treat `~/.codex/project-scaffolds/` as the default lookup location.

## Hard Rules
- Never invent APIs, configs, commands, or file paths. Search first.
- Separate research from implementation when the solution is not yet clear.
- No completion claims without fresh verification evidence.
- When context may be stale, re-read the task plan and relevant files before continuing.
- Keep diffs small and consistent with the project's existing style.
- Never paste secrets, tokens, private keys, `.env` values, or credentials into code or logs.

## Load Order
- If a project-level `AGENTS.md` exists, read it first.
- If no project-level `AGENTS.md` exists and the task is to initialize project docs or project context, consult `~/.codex/project-scaffolds/` and load only the minimum relevant scaffold files.
- Let the project-level `AGENTS.md` decide which project files to load next.
- Keep project architecture, commands, conventions, and active work state out of the global file.

## Preferences
- Default language: Chinese.
- Be concise, concrete, and direct.
