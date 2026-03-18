# Findings & Decisions

## Requirements
- Research `https://developers.openai.com/codex/learn/best-practices`
- Use a multi-agent workflow
- Keep the result useful for the `context-engineering` repository

## Research Angles
- What the official page says at a high level
- Which recommendations are most actionable for repository workflow design
- Which recommendations overlap with or challenge current project conventions

## Findings
- The official best-practices page treats Codex as a configurable teammate and connects prompting, planning, `AGENTS.md`, config, testing, MCP, skills, automations, and session control into one workflow.
- The page's strongest practical prompt pattern is to specify `Goal`, `Context`, `Constraints`, and `Done when`.
- The page explicitly recommends plan-first behavior for complex tasks and durable repo guidance through short, practical `AGENTS.md` files.
- The page recommends keeping personal defaults in `~/.codex/config.toml` and repo-specific behavior in `.codex/config.toml`, which now matches this repository.
- The page frames testing and review as part of the agent loop, not optional follow-up work.
- The page recommends using multi-agent workflows to offload bounded work from the main thread and to keep one thread per coherent task.

## Repository Alignment
- Strong alignment:
  - thin routing-oriented `AGENTS.md`
  - file-based planning bundles for complex tasks
  - explicit `VERIFICATION.md`
  - repo-local `.codex/config.toml` for project-specific agent behavior
- Likely gaps:
  - no explicit task-brief or contract template for `Goal / Context / Constraints / Done when`
  - no real dogfood example yet for the local multi-agent setup
  - repo-shared skill layout still centers on `system/codex-home/skills/`, which differs from the runtime-oriented `.agents/skills/` convention described in the official page
  - no explicit repo-level review checklist file linked from `AGENTS.md`

## Sources
- `https://developers.openai.com/codex/learn/best-practices`
- `docs/research/sources/openai-codex-best-practices-2026-03-12.md`
