# Findings & Decisions

## Requirements
- Implement multi-agent support for this repository first.
- Base the design on current official Codex multi-agent documentation.
- Keep the role design narrow and practical for a markdown-first research repository.
- Update project-current docs that become stale because of the workflow change.

## Research Findings
- Official Codex guidance recommends moving noisy exploration and verification off the main thread to reduce context pollution and context rot.
- Official Codex guidance recommends narrow, opinionated agent roles with clear tool surfaces and explicit boundaries.
- The repository currently has no project-local `.codex/config.toml`, so agent definitions are not versioned with the project.
- The repository already documents a coordinator-plus-worker pattern in `docs/research/notes/context-engineering-experience-map.zh.md`, which aligns with the official guidance.
- This repository is research-first and document-first, so multiple write-capable agents would add coordination overhead without much benefit.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Use read-only roles for `explorer`, `docs_researcher`, and `reviewer` | These tasks are parallelizable and benefit most from isolation |
| Use a single write-capable role, `docs_syncer` | Keeps edits deliberate and reduces conflict risk |
| Set `agents.max_threads = 4` and `agents.max_depth = 1` | Fits a small team of specialized helpers without encouraging deep agent nesting |

## Sources
- `https://developers.openai.com/codex/multi-agent`
- `https://developers.openai.com/codex/concepts/multi-agents`
- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `ARCHITECTURE.md`
- `VERIFICATION.md`
- `docs/research/notes/context-engineering-experience-map.zh.md`
