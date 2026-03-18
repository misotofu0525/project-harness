# Findings & Decisions

## Requirements
- Test whether custom roles defined in `.codex/config.toml` are usable at runtime
- Focus on `docs_researcher` and `docs_syncer`
- Prefer direct evidence over assumptions

## Planned Checks
- Tool-layer evidence from the currently available `spawn_agent` interface
- Local CLI evidence from the installed `codex` command if available
- Cross-check against the repository-local `.codex/config.toml`

## Findings
- The local `codex` CLI is installed at `/opt/homebrew/bin/codex` and the `multi_agent` feature is enabled.
- The repository-local `.codex/config.toml` is present and defines the custom roles `docs_researcher` and `docs_syncer`.
- The current developer-tool `spawn_agent` interface in this session does not accept `docs_researcher` as an `agent_type`; a direct call returned `unknown agent_type 'docs_researcher'`.
- The local `codex exec` runtime does support these project-local custom roles:
  - With a temporary marker config override for `docs_researcher`, the raw child-agent message began with `ROLE_MARKER_DOCS_RESEARCHER`, which came only from the role-specific config file.
  - With a temporary marker config override for `docs_syncer`, the raw child-agent message began with `ROLE_MARKER_DOCS_SYNCER`, and the child also created `docs_syncer_marker.txt` containing `SYNCER_OK` exactly as required by the role-specific config file.
- Therefore the earlier non-use of `docs_researcher` and `docs_syncer` in this chat was a tool-layer limitation of the available `spawn_agent` interface here, not a failure of the repository's `.codex/config.toml`.

## Evidence Paths
- `docs/plans/active/2026-03-12-custom-agent-role-runtime-test/docs-researcher-marker.toml`
- `docs/plans/active/2026-03-12-custom-agent-role-runtime-test/docs-syncer-marker.toml`
- `docs/plans/active/2026-03-12-custom-agent-role-runtime-test/docs_syncer_marker.txt`
