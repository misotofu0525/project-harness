# Claude Code Workflow 对照分析

- 目标仓库: <https://github.com/runesleo/claude-code-workflow>
- 对照材料 1: [how-to-be-a-world-class-agentic-engineer.md](../sources/how-to-be-a-world-class-agentic-engineer.md)
- 对照材料 2: [2512.05470-summary.zh.md](2512.05470-summary.zh.md)

## 结论先行

这个仓库最有价值的地方，不是它用了 `CLAUDE.md`，而是它把 agent 工作流拆成了几个明确闭环：

- 入口路由
- 事件触发 skill
- 热数据记忆层
- 结束时自动 flush
- 完成前强制验证
- 多模型协作边界

如果只从工程实用性看，它和前面那篇文章是高度一致的；如果从架构完整性看，它又只是那篇论文的轻量化工作流实现，而不是完整的 context infrastructure。

## 它和文章一致的部分

前面那篇文章的核心是：

- 少即是多
- 顶层文件只做路由
- 上下文要最小、精确、按需加载
- 研究和实现要拆开
- 任务完成条件要明确
- 规则和技能要逐步沉淀、定期清理

这个仓库里真正和这些观点对齐的点有：

### 1. 顶层入口文件只做路由

`CLAUDE.md` 不是巨型说明书，而是：

- 用户信息
- 协作偏好
- SSOT 映射
- Memory write routing
- On-demand loading index

这和文章里“把顶层文件当成 IF-ELSE 目录”几乎是同一路线。

### 2. 分层加载，控制上下文膨胀

仓库明确分三层：

- Layer 0: always loaded rules
- Layer 1: on-demand docs
- Layer 2: hot data

这本质上就是在做上下文分层和按需加载，正面回应了文章里说的 `context bloat`。

### 3. 用 skill 把行为固化

几个关键 skill：

- `verification-before-completion`
- `systematic-debugging`
- `session-end`
- `planning-with-files`

这正对应文章里说的：

- 不希望 agent 乱来，就写规则
- 希望 agent 按固定 recipe 做事，就写 skill

### 4. 明确任务结束条件

`verification-before-completion` 的核心规则就是：

`没有新鲜验证证据，就不能宣称完成`

这和文章里“agent 知道如何开始，但不知道如何结束，所以你要把完成条件写死”完全一致。

### 5. 通过自动 flush 减少上下文丢失

`memory-flush.md` 和 `session-end` skill 强制在任务结束、commit、退出信号时写回：

- `today.md`
- `projects.md`
- `goals.md`
- `active-tasks.json`

这等于把“长会话中的关键状态”从易失上下文里拿出来，做成轻量持久层。

## 它和论文一致的部分

论文强调的是：`context engineering` 应该被设计成基础设施，而不是 prompt 技巧。

这个仓库和论文一致的点：

### 1. 它已经把上下文当成 artefact，而不是聊天内容

这里的上下文不是一句 prompt，而是一组文件：

- `today.md`
- `projects.md`
- `goals.md`
- `active-tasks.json`
- `handbook/PROJECT_CONTEXT.md`

这和论文“上下文应该是持久、可治理资源”的方向一致。

### 2. 它开始做上下文生命周期分层

虽然没有论文那么完整，但至少已经有：

- 当日热数据
- 跨项目汇总
- 长期目标
- 跨 session 任务注册

这说明作者已经意识到：不同时间尺度的上下文，不应该混在一个文件里。

### 3. 它有治理意识

尤其体现在：

- `SSOT Ownership`
- 外部模型只允许写 `handbook/PROJECT_CONTEXT.md` 指定 handoff block
- `.claude/` 和知识库不允许外部模型乱写

这和论文里的 `governance / access control / traceability` 方向相当接近。

## 它没有达到论文层次的地方

这是最关键的边界。

这个仓库虽然有“上下文文件化”的意识，但它还不是完整的 context engineering architecture。

### 1. 没有完整的 `history / memory / scratchpad` 明确分层

现在更接近：

- `today.md` = hot log
- `active-tasks.json` = in-flight registry
- `projects.md` = overview index
- `goals.md` = planning layer

但没有真正定义：

- immutable history
- structured memory with lineage
- scratchpad lifecycle

### 2. 没有显式的 constructor / updater / evaluator 管线

论文的关键是：

- Constructor: 选上下文
- Updater: 装入和刷新上下文
- Evaluator: 校验结果并回写

这个仓库里有一些影子：

- skill trigger 类似 constructor 的触发前置
- memory flush 类似 updater 的持久化
- verification-before-completion 类似 evaluator 的一部分

但它们还不是一个统一、可审计、可复放的 pipeline。

### 3. provenance / lineage 还很弱

它有状态文件，但还没有真正做到：

- 每次上下文选择为何发生
- 每次写回基于哪次输入/哪次输出
- 哪次模型产出被验证通过后进入长期记忆

也就是说，workflow 有了，但 audit trail 还不够强。

## 对 Codex 的真实启发

如果把这个仓库直接搬进 Codex，不应该原样照抄。

### 值得抄的

- 顶层入口文件做路由，不做巨型说明书
- 分三层处理上下文：常驻规则 / 按需文档 / 热数据
- 强制 `verification before completion`
- 用 `planning-with-files` 管复杂任务
- 用 `session-end` 思路做收尾和 handoff
- 给外部 agent / reviewer / verifier 明确写入边界

### 需要改写的

- `memory_add` / `memory_search` 这些 Claude 专用能力，Codex 里不能直接照搬
- Sonnet / Opus / Haiku 的路由表要换成 Codex 当前真实可用模型和工具
- 外部模型协作方式要改成更贴近 Codex 的 multi-agent / review / skills / MCP 机制

### 不建议原样抄的

- 过多的人设化规则
- 过细的模型路由表
- 大量只在 Claude 生态成立的命令式约束

这些东西一旦迁移到 Codex，容易变成噪音上下文。

## 最终判断

这个仓库适合把它看成：

- `战术层` 的优秀 workflow 模板
- 不是 `战略层` 的完整 context architecture

它和文章的关系是：

- 它基本把文章里的很多“经验法则”变成了可执行的 rules/skills/workflows

它和论文的关系是：

- 它朝论文的方向走了一步，但还停在“工作流工程”阶段，没到“上下文基础设施”阶段

## 对我们最有用的落地建议

如果只挑 5 个最值得迁移到 Codex 的点：

1. 顶层 `AGENTS.md` 改成入口路由器，不堆满细则。
2. 建立轻量热数据层，至少有 `today.md` 和 `active-tasks.json` 级别的跨 session 状态。
3. 把 “无验证不宣称完成” 升级为硬规则。
4. 把复杂任务统一走文件化 planning。
5. 给 reviewer / verifier / external agent 定义明确写入边界。

如果再往论文方向走一步：

6. 把 `history / memory / scratchpad / manifest / evaluation` 做成显式层，而不只是若干记事文件。
