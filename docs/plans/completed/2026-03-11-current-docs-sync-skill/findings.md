# Findings: current-docs-sync skill

## Repository Findings
- The repository currently has no repo-local `SKILL.md`.
- `PROJECT_CONTEXT.md` already identifies repo-local skills for verification and current-docs as the main next gap.
- `AGENTS.md` does not yet define a local skill directory or route tasks into repo-local skills.

## External Behavior Findings
- Current OpenAI Codex guidance confirms that `AGENTS.md` is the persistent project instruction entrypoint.
- Official guidance does not prescribe a fixed repository path for repo-local skills.
- Inference: the repository can choose its own skill directory as long as `AGENTS.md` routes relevant tasks to the skill.

## Source Provenance
- OpenAI, "Introducing Codex": <https://openai.com/index/introducing-codex/>
- OpenAI, "How OpenAI uses Codex": <https://openai.com/index/how-openai-uses-codex/>

## Working Hypothesis
- Place repo-local skills under `docs/skills/` to preserve a thin root.
- Add a narrow `current-docs-sync` skill that handles only document-sync work after structure or workflow changes.

## Final Decisions
- The repository convention for repo-local skills is now `docs/skills/`.
- `AGENTS.md` should route structure, workflow, and entry-doc sync work to `docs/skills/current-docs-sync/SKILL.md`.
- `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, and `VERIFICATION.md` should move together whenever repository structure or operating conventions change.
