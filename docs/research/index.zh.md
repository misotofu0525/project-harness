# Harness Engineering 研究索引

## 目的

这个目录用于沉淀 `harness engineering`、`context engineering` 和 Codex 工作流设计相关的研究材料。

结构上分成两层：

- `sources/`
  - 保存原始材料或本地保存的全文
- `notes/`
  - 保存摘要、对照分析、统一经验整理和后续研究结论

## Sources

- [how-to-be-a-world-class-agentic-engineer.md](sources/how-to-be-a-world-class-agentic-engineer.md)
- [2512.05470-everything-is-context.md](sources/2512.05470-everything-is-context.md)
- [openai-codex-best-practices-2026-03-12.md](sources/openai-codex-best-practices-2026-03-12.md)

## Notes

- [2512.05470-summary.zh.md](notes/2512.05470-summary.zh.md)
- [claude-code-workflow-comparison.zh.md](notes/claude-code-workflow-comparison.zh.md)
- [context-engineering-experience-map.zh.md](notes/context-engineering-experience-map.zh.md)
- [openai-codex-best-practices-summary.zh.md](notes/openai-codex-best-practices-summary.zh.md)

## Reading Order

1. 先看 `sources/` 里的原始材料，理解每份材料的立场。
2. 再看 `notes/` 里的摘要和对照分析。
3. 最后以 `context-engineering-experience-map.zh.md` 作为统一入口，回收成可执行经验。

## 当前结论

- 文章提供战术级经验，强调 `less is more`、上下文控制、研究与实现分离、完成条件写死。
- 论文提供架构级抽象，强调 `history / memory / scratchpad / governance`。
- 工作流项目提供工程化闭环，强调路由、验证、session-end 和热状态管理。
- OpenAI 官方 Codex best practices 明确把 `AGENTS.md`、`.codex/config.toml`、planning、verification、MCP、skills、automations 和 multi-agent 连接成一条完整演进路径。
- 这个仓库当前的目标，不是复制某一个现成体系，而是把这些经验收成适合 Codex 的最小、可演进研究项目。
