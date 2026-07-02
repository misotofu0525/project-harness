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

## Subagent Policy
- Use subagents to isolate noisy exploration, local skill or MCP loads, independent verification, or low-coupling parallel work.
- Current Codex behavior requires an explicit delegation trigger. Do not assume subagents will spawn automatically from generic task wording alone.
- Do not spawn subagents when the task is too small, cannot be summarized cleanly, depends on tightly shared intermediate state, or is likely to create write conflicts.
- Delegate only when `subagent benefit > delegation cost`.
- If a task strongly benefits from delegation but permission is missing, ask a short opt-in question early or point the user to a task contract that explicitly allows delegated or parallel agent work.
- If a task contract explicitly allows delegation, treat that as permission to use built-in subagents when `subagent benefit > delegation cost`.
- Prefer built-in roles by default.
- Define custom roles only when a pattern repeats across projects, has stable boundaries, needs a fixed context package, and built-in roles are not enough.
- Subagents should return compressed conclusions, evidence, and next-step recommendations rather than raw exploration trails unless the user asks for the raw trail.

## Load Order
- If a project-level `AGENTS.md` exists, read it first.
- If no project-level `AGENTS.md` exists and the task is to initialize project docs or project context, consult `~/.codex/project-scaffolds/` and load only the minimum relevant scaffold files.
- Let the project-level `AGENTS.md` decide which project files to load next.
- Keep project architecture, commands, conventions, and active work state out of the global file.

## Preferences
- Default language: Chinese.
- Be concise, concrete, and direct.
