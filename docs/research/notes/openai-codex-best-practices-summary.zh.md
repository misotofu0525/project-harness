# OpenAI Codex Best Practices 调研摘要

- 来源: [openai-codex-best-practices-2026-03-12.md](/Users/misotofu/Documents/workspace/context-engineering/docs/research/sources/openai-codex-best-practices-2026-03-12.md)
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

### 已经和官方思路高度一致的点

- 顶层 [AGENTS.md](/Users/misotofu/Documents/workspace/context-engineering/AGENTS.md) 已经是路由器，而不是百科全书
- 复杂任务已经使用 `docs/plans/active/<task>/` 做文件化 planning
- [handbook/VERIFICATION.md](/Users/misotofu/Documents/workspace/context-engineering/handbook/VERIFICATION.md) 已经把“完成前验证”写成显式流程
- 项目已经把 repo-specific agent behavior 放进 [`.codex/config.toml`](/Users/misotofu/Documents/workspace/context-engineering/.codex/config.toml) 和 [`.codex/agents/docs_syncer.toml`](/Users/misotofu/Documents/workspace/context-engineering/.codex/agents/docs_syncer.toml)
- 本地 multi-agent 角色已经做成“主 agent 决策 + 窄职责子 agent + 单一写入角色”的收口设计

### 还存在的差距或可加强点

- 还缺一个更显式的 task brief / contract 模板，把 `Goal / Context / Constraints / Done when` 固化下来
- 当前官方 subagent 行为还要求显式 delegation trigger，因此 task brief 不只是“把任务说清楚”，也承担“明确授权并行委派”的作用
- 还没有本仓库自己的 multi-agent dogfood 样例，缺少真实任务层面的 smoke test
- 当前共享 skill 的 repo 内版本化路径是 `system/codex-home/skills/`，这更像“受管镜像”，和官方文档提到的 repo 级 `.agents/skills/` 运行时路径并不完全一致
- 本仓库的 `.codex/config.toml` 目前只保留全局 agent 边界，角色细节已经下沉到 [`.codex/agents/docs_syncer.toml`](/Users/misotofu/Documents/workspace/context-engineering/.codex/agents/docs_syncer.toml)，但仍然没有把顶层 sandbox / approval 默认策略显式写进项目配置
- 还没有类似 `code_review.md` 这种可被 `AGENTS.md` 引用的稳定 review checklist

## 对后续工作的建议优先级

### P1

- 加一个轻量 task brief 模板，专门承载 `Goal / Context / Constraints / Done when / Delegation`
- 选一个真实仓库任务 dogfood 当前 multi-agent 配置

### P2

- 决定这个仓库是否要增加 repo 级 `.agents/skills/` 入口，还是继续坚持 `system/codex-home/skills/` 作为研究型镜像
- 给 review 流程补一个可复用 checklist 文档

### P3

- 等这些流程稳定之后，再考虑 automation，而不是提前自动化

## 最终判断

如果把这篇官方文档和当前仓库放在一起看，方向基本是对的。

最需要补的，不是更多规则，而是三件事：

- 把任务 contract 再写清楚一点
- 把 multi-agent workflow 真跑起来并复盘
- 把 skill/runtime 布局和官方路径约定再对齐一次
