# Source Capture: OpenAI Codex Best Practices

## Provenance
- Title: `Best practices`
- URL: `https://developers.openai.com/codex/learn/best-practices`
- Publisher: `OpenAI Developers`
- Accessed: `2026-03-12`
- Capture type: `manual paraphrased source capture`
- Scope: official guidance for prompting, planning, `AGENTS.md`, configuration, testing and review, MCP, skills, automations, session controls, and common mistakes

## Section Outline
- Strong first use: context and prompts
- Plan first for difficult tasks
- Make guidance reusable with `AGENTS.md`
- Configure Codex for consistency
- Improve reliability with testing and review
- Use MCPs for external context
- Turn repeatable work into skills
- Use automations for repeated work
- Organize long-running work with session controls
- Common mistakes

## Key Takeaways
- Codex should be treated like a teammate that gets configured and improved over time, not a one-off assistant.
- Better results come from giving the right task context, durable repo guidance, working configuration, external context via MCP when needed, and turning stable repeated workflows into skills or automations.
- For task prompts, the page recommends being explicit about the goal, relevant context, constraints, and what completion means.
- For difficult work, planning should happen before implementation.
- Durable instructions belong in `AGENTS.md`, and the file should stay short, accurate, and practical.
- Personal defaults should live in `~/.codex/config.toml`, repo-specific behavior should live in `.codex/config.toml`, and permissions should stay tight by default.
- Codex should be asked to test, validate, and review changes rather than only generate code.
- MCPs are best when the needed context lives outside the repo or changes frequently.
- Skills are for repeatable workflows with clear inputs and outputs; automations are for stable workflows that no longer need much steering.
- Sessions should stay scoped to one coherent task, and multi-agent workflows should offload bounded work from the main thread.
