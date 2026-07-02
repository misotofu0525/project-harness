# Findings & Decisions

## Official Guidance
- The current official Codex subagents docs describe custom agents as standalone TOML files under `.codex/agents/` or `~/.codex/agents/`.
- The docs present `name`, `description`, and `prompt` or `instructions`-style fields inside the agent file itself, while global settings stay under `[agents]`.
- Inference from the docs: a repo-local `[agents.<name>]` table with `config_file = "agents/..."` is no longer the primary documented pattern.

## Current Repo Mismatch
- `.codex/config.toml` currently mixes global agent settings with a repo-local `[agents.docs_syncer]` table.
- `.codex/agents/docs-syncer.toml` currently contains only behavioral fields and no self-describing metadata.
- The filename uses `docs-syncer.toml` while the agent identifier used elsewhere is `docs_syncer`.

## Scope To Sync
- `.codex/config.toml`
- `.codex/agents/docs-syncer.toml` or its replacement
- `AGENTS.md`
- `handbook/PROJECT_CONTEXT.md`
- `handbook/ARCHITECTURE.md`
- `handbook/VERIFICATION.md`

## Config Refactor Outcome
- `.codex/config.toml` now keeps only global `[agents]` settings.
- The custom role now lives in `.codex/agents/docs_syncer.toml` as a self-describing standalone agent file.
- Repo-local docs and checks now reference `docs_syncer.toml` directly instead of assuming a `config_file` pointer from `.codex/config.toml`.

## Runtime Validation Limit
- A minimal `codex exec --full-auto` smoke check was attempted after the refactor.
- The CLI emitted warnings about `~/.codex/state_5.sqlite` having a migration mismatch and did not produce a usable success/failure result for the agent call.
- Inference: the repository config refactor is structurally sound, but end-to-end runtime validation is currently blocked by the local Codex state runtime rather than by an obvious repo-local schema error.
