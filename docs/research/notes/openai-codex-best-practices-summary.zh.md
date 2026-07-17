# OpenAI Codex Best Practices 调研摘要

- 来源: [openai-codex-best-practices-2026-03-12.md](../sources/openai-codex-best-practices-2026-03-12.md)
- 官方页面: `https://developers.openai.com/codex/learn/best-practices`
- 调研日期: `2026-03-12`

## 一句话判断

这篇官方文档的核心不是“怎么写更花的 prompt”，而是把 Codex 当成一个可配置、可验证、可复用、可逐步工程化的 teammate 来使用。

## 官方最佳实践的主线

### 1. 先把任务上下文说对

官方给了一个非常直接的默认结构：

- `Goal`
- `Context`
- `Constraints`
- `Done when`

重点是：

- prompt 不必完美，但任务上下文越清楚，结果越稳定
- 大仓库和高风险任务里，明确完成条件尤其重要

### 2. 复杂任务先 plan，再实施

官方推荐对复杂、模糊、多步骤任务先做 planning，再开始改动。

推荐方式包括：

- 使用 plan mode
- 先让 Codex 反问、澄清需求
- 使用 `PLANS.md` 或 execution-plan 模板

### 3. durable guidance 应该进 `AGENTS.md`

官方把 `AGENTS.md` 定义成：

- 自动加载的 repo 级 agent README
- 记录构建、测试、目录、约束、done definition 的最佳位置

几个关键判断很重要：

- `AGENTS.md` 要短、准、可操作
- 不要把大量模糊规则堆进去
- 更具体、离当前目录更近的 `AGENTS.md` 优先生效
- 如果重复犯同样的错，就做 retrospective 并回写 `AGENTS.md`

### 4. consistency 靠 config，不靠每次重说

官方推荐：

- 个人默认放 `~/.codex/config.toml`
- 仓库特定行为放 `.codex/config.toml`
- 命令行 override 只用于一次性情况

同时强调：

- sandbox / approval 默认应该收紧
- 质量问题经常是 setup 问题，不只是模型问题

### 5. 生成不是终点，测试和 review 才是闭环

官方明确建议让 Codex：

- 写或更新测试
- 跑相关检查
- 确认行为结果
- review diff，找 bug / regression / risk

也就是：Codex 不只负责“写”，也负责“测、查、审”。

### 6. 外部上下文优先走 MCP

官方对 MCP 的定位很明确：

- 仓库外上下文
- 高频变化数据
- 需要稳定工具接入的工作流

并且强调：

- 不要一上来把所有工具都接进去
- 先接能明显减少手工循环的 1 到 2 个

### 7. 重复流程应该升级成 skill

官方建议把稳定重复的工作流沉淀成 skill，而不是长期靠超长 prompt 或反复纠正。

适合做 skill 的典型场景：

- triage
- review
- migration planning
- standard debugging
- summary

### 8. 更稳定之后，再 automation

官方的顺序是：

- 先手工跑顺
- 再做 skill
- 最后再做 automation

一句话可以概括成：

- `skills define the method`
- `automations define the schedule`

### 9. 会话要按任务切，不要按项目切

官方强调：

- 一个 thread 对应一个 coherent unit of work
- 不要把整个项目都塞进一条长期 thread
- multi-agent 适合把 bounded work 从主线程卸出去

## 对这个仓库最相关的结论

> 2026-07-17 更新：下面是 Project Harness 重构后的仓库映射；原先的 handbook、custom subagent 与 Home mirror 已退役。

### 已吸收进 Project Harness 的点

- 顶层 [AGENTS.md](../../../AGENTS.md) 是小型 Kernel 和 Router，而不是百科全书。
- 复杂任务使用 `docs/plans/active/<task-id>/` 下的三文件 Journal，并以 Done When 固化完成条件。
- [docs/agent/verification.md](../../agent/verification.md) 和 `.harness.toml` 把完成前验证拆成 scoped context 与机器命令。
- 重复流程已沉淀为 `setup-project`、`task-memory` 与 `finish-task` Skills。
- Context Routing、Task Continuity 与 Verified Completion 形成从上下文到恢复、再到交付验证的闭环。

### 仍然成立的边界

- subagent 必须基于明确任务边界和授权使用，不应被包装成 Harness 顶层抽象。
- automation 仍然应晚于已经手工跑顺并可验证的 Skill。
- 外部高频变化数据仍适合通过 MCP 或平台 Plugin 接入，而不是写入常驻项目上下文。

## 最终判断

如果把这篇官方文档和当前 Project Harness 放在一起看，核心方向仍然是：入口要小、任务要有明确完成条件、重复方法要变成 Skill、交付必须有测试和 diff review。当前实现把这些结论收敛成项目级 Harness，而不是继续扩展 Agent 概念。
