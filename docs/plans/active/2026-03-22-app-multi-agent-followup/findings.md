# Findings & Decisions

## Requirements
- Re-check current official Codex documentation
- Focus on whether Codex App support for multi-agent changes the repository's earlier conclusions
- Prefer official OpenAI sources over inference

## Comparison Surface
- Official docs: `codex/multi-agent`, `codex/app`, and directly related official pages only
- Local repo: `.codex/`, `AGENTS.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `VERIFICATION.md`, and relevant research notes

## Findings
- As of `2026-03-22`, the current official documentation is internally inconsistent about surface support:
  - `https://developers.openai.com/codex/multi-agent#enable-multi-agent` still says multi-agent activity is currently surfaced in the CLI and that visibility in the Codex app and IDE Extension is coming soon.
  - `https://developers.openai.com/codex/app#codex-app` and `https://developers.openai.com/codex/app/features#multitask-across-projects` describe the Codex app as a desktop experience for working on threads in parallel, with worktrees, automations, Git tools, skills, MCP, and shared configuration.
- The current repository's core changes remain valid despite that surface change:
  - project-local `.codex/config.toml`
  - narrow custom agent roles under `.codex/agents/`
  - routing and verification updates in `AGENTS.md`, `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, and `VERIFICATION.md`
- No core repository document currently hardcodes the claim that multi-agent is CLI-only, so no structural rollback is needed.
- The main stale risk is in dated research interpretation, not in the actual repo configuration.
- The most likely optional follow-up is to add a dated note that official docs and product behavior may diverge temporarily across surfaces, especially for fast-moving Codex features.

## Required vs Optional Changes
- Required now:
  - none
- Optional but worthwhile:
  - append a dated addendum to the March 12 best-practices research note noting the March 22 doc inconsistency and App support update
  - append a dated addendum to the custom-role runtime test noting that a later resumed session successfully invoked custom roles through `spawn_agent`
  - if the Codex App becomes a primary workflow surface for this repo, add one app-oriented smoke-check note to future verification research rather than to `VERIFICATION.md`
