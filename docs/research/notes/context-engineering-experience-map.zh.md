# Context Engineering 统一经验地图

- 来源 1: [how-to-be-a-world-class-agentic-engineer.md](../sources/how-to-be-a-world-class-agentic-engineer.md)
- 来源 2: [2512.05470-summary.zh.md](2512.05470-summary.zh.md)
- 来源 3: [claude-code-workflow-comparison.zh.md](claude-code-workflow-comparison.zh.md)

## 如何读这份文档

这三份材料其实分别站在三个层次上：

- `文章`
  更偏战术经验，讲怎么让 agent 当下更好用。
- `项目`
  更偏工作流工程，讲怎么把经验沉淀成 rules / skills / memory / commands。
- `论文`
  更偏架构设计，讲怎么把 context engineering 做成基础设施。

这份文档不再按来源讲，而是按：

- 抽象层级
- 作用范围
- 时间维度
- 工程类别

重新整理。

## 一、四个总维度

### 1. 抽象层级

| 层级 | 关注点 | 代表来源 | 核心问题 |
|------|--------|----------|----------|
| 战术层 | 单次任务怎么做得更准 | 文章 | 如何减少噪音、避免跑偏、提高成功率 |
| 工作流层 | 如何让经验可重复执行 | 项目 | 如何把规则、记忆、验证、handoff 变成闭环 |
| 架构层 | 如何让上下文成为基础设施 | 论文 | 如何治理 context 的生命周期、可审计性和可演化性 |

### 2. 作用范围

| 范围 | 主要对象 | 典型内容 |
|------|----------|----------|
| 用户维度 | 个人长期工作方式 | 全局规则、偏好、常驻行为标准 |
| 项目维度 | 单个代码库/产品 | 架构、命令、项目状态、handoff、项目记忆 |
| 系统维度 | 多项目、多会话、多 agent 系统 | 持久上下文仓库、治理、访问控制、审计 |

### 3. 时间维度

| 阶段 | 关注点 | 典型机制 |
|------|--------|----------|
| 任务前 | 如何进入任务 | 任务路由、上下文选择、planning、研究与实现拆分 |
| 任务中 | 如何保持上下文干净 | 按需加载、最小上下文、调试协议、增量刷新 |
| 任务后 | 如何确认完成 | verification、test、screenshot、contract、session-end |
| 跨会话 | 如何不丢失状态 | hot memory、task registry、history、memory evolution |

### 4. 状态/持久化维度

| 状态层 | 特征 | 更接近哪份来源 |
|--------|------|----------------|
| 即时上下文 | 只为当前推理存在 | 文章 |
| 热数据层 | 跨会话保存近期工作状态 | 项目 |
| 持久上下文层 | 结构化 memory / history / scratchpad | 论文 |
| 治理与审计层 | provenance / lineage / access control | 论文 |

## 二、基础原则类经验

### 1. 少即是多

- 不要默认需要更多 harness、plugin、memory 系统。
- 基础 CLI 往往已经足够强，额外层会增加上下文膨胀和锁定成本。
- 真正高价值、通用的能力，最终会被基础产品吸收。

来源倾向：

- `文章` 最强
- `项目` 局部支持

### 2. Prompt 不是全部，上下文才是核心

- prompt engineering 只是上下文投递的一部分。
- 真正影响输出质量的是你给 agent 的整体信息环境。
- 所以要管理：
  - 读什么
  - 什么时候读
  - 读多少
  - 从哪里读
  - 谁能写回

来源倾向：

- `文章` 讲上下文重要性
- `论文` 把它上升到系统设计
- `项目` 把它落成加载分层

### 3. 人对结果负责

- agent 可以承担大量研究和实现工作。
- 但最终 outcome 仍应由人类签字式负责。
- 人不是旁观者，而是 curator / verifier / co-reasoner。

来源倾向：

- `文章`
- `论文`

## 三、上下文设计类经验

### 1. 顶层入口文件应该做路由，不应做百科全书

- 顶层 `AGENTS.md / CLAUDE.md` 的职责应是：
  - 定义入口规则
  - 指定什么时候读什么
  - 指出 SSOT 在哪里
  - 指明哪些文件是常驻，哪些是按需加载
- 不适合把所有偏好和全部知识都塞进去。

来源倾向：

- `文章` 明确提出“顶层文件是 IF-ELSE 目录”
- `项目` 真实落地成 entrypoint router

### 2. 上下文要分层加载

推荐的分层思路：

- `Always-loaded rules`
  最少量、最高优先级、始终有效的行为约束。
- `On-demand docs`
  只有在场景触发时才读取的说明文档。
- `Hot data`
  当前工作真正需要的最新状态。

这能降低 `context bloat`，也更利于 agent 在长任务中保持方向。

来源倾向：

- `项目` 最强
- `文章` 在原则上支持

### 3. 把“上下文选择”当成正式动作

- 不要默认“把更多资料都喂进去”是安全的。
- 上下文应该被显式选择、排序、压缩、注入。
- 最好为一次任务生成可解释的 `manifest` 或等价物。

来源倾向：

- `论文` 最强
- `文章` 在实践上支持“最小且精确”

### 4. 不同时间尺度的上下文不要混放

至少应区分：

- 当前任务上下文
- 当天热状态
- 跨 session 任务状态
- 长期项目知识
- 历史原始记录

来源倾向：

- `项目` 提供了 `today.md / goals.md / projects.md / active-tasks.json`
- `论文` 提供了更完整的 `history / memory / scratchpad`

## 四、规则、技能、命令类经验

### 1. Rule 用来约束，Skill 用来固化 recipe

- 不希望 agent 再犯同类错误，就加 `rule`。
- 希望 agent 以后按一种确定过程做事，就沉淀成 `skill`。
- 技能不是偏好，而是“执行配方”。

来源倾向：

- `文章` 明确提出
- `项目` 具体落地

### 2. Skill 最适合承载重复出现的高价值闭环

典型适合做 skill 的场景：

- 验证后才能宣称完成
- 系统化调试
- 复杂任务的文件化 planning
- session-end 收尾

来源倾向：

- `项目`

### 3. 命令化可以减少每次重复组织话术

- 把 `review`、`debug`、`deploy`、`exploration` 这类高频流程包装成命令。
- 命令的价值不在“方便”，而在“稳定地调用正确流程”。

来源倾向：

- `项目`

## 五、任务生命周期类经验

### 1. 研究与实现必须拆开

- 研究阶段负责比较方案、收集证据、选型。
- 实现阶段只负责按已确定方案落地。
- 不要让同一上下文先发散、再收敛、再改代码。

来源倾向：

- `文章` 最强
- `论文` 从 constructor 角度提供架构依据

### 2. 每个复杂任务都应该被写成 contract

contract 至少应包含：

- goal
- in scope
- out of scope
- files
- implementation spec
- checks
- done when

来源倾向：

- `文章`
- `项目` 的 verification/session-end 机制支持这一思想

### 3. 新 session 优于超长单 session

- 长时间单会话容易堆积无关上下文。
- 更好的做法是：
  - 一份 task contract
  - 一个相对干净的 session
  - 做完后回写持久状态

来源倾向：

- `文章`

### 4. 任务收尾应该是流程，不是临时想到

收尾应该包括：

- 更新热状态
- 更新任务注册表
- 更新项目 handoff
- 记录经验
- commit / verify / handoff

来源倾向：

- `项目`

## 六、记忆与持久化类经验

### 1. 工作记忆应该落盘

上下文窗口是易失的，重要内容要写入文件或持久存储。

最基本的落盘对象：

- 今日进展
- 活跃任务
- 项目状态
- 关键经验

来源倾向：

- `项目`
- `planning-with-files` 工作法

### 2. `History / Memory / Scratchpad` 最值得作为长期模型

推荐分工：

- `History`
  原始不可变事实和交互轨迹。
- `Memory`
  可检索、可复用的结构化知识。
- `Scratchpad`
  临时草稿和中间推理痕迹。

来源倾向：

- `论文`

### 3. 热状态与长期知识应该分开

- `today.md` 这种文件不适合承担长期知识库职责。
- 长期事实、规律、坑点、项目经验应逐步沉淀到更稳定层。

来源倾向：

- `项目`
- `论文`

### 4. Memory 不是“越多越好”

- 记忆增长会带来冗余、污染、检索精度下降。
- 必须定期做：
  - deduplication
  - consolidation
  - contradiction cleanup
  - aging / retention policy

来源倾向：

- `文章` 讲 context bloat
- `论文` 明确提出治理需求

## 七、验证与完成类经验

### 1. 无验证不宣称完成

这是三份材料里最值得上升为硬规则的一条。

- 不能靠“应该可以”
- 不能靠“我改了代码”
- 不能靠“agent 说成功了”
- 必须有新鲜验证证据

来源倾向：

- `项目` 最明确
- `文章` 也把 tests / screenshots / contracts 作为完成边界

### 2. 完成条件最好是确定性的

优先级通常是：

- tests
- build
- lint
- reproducer passes
- screenshot / behavior verification

来源倾向：

- `文章`
- `项目`

### 3. 验证是 evaluator 的一部分，不只是 QA

- 验证通过后，结果才应进入长期记忆或被标记为完成。
- 验证失败时，应阻止“完成”状态扩散到记忆和项目状态。

来源倾向：

- `论文`
- `项目`

## 八、调试类经验

### 1. 先回忆，再定位根因，再修

调试推荐序列：

1. recall past similar cases
2. read the error carefully
3. reproduce
4. trace the data flow
5. compare with working example
6. form one hypothesis
7. make one minimal change
8. verify

来源倾向：

- `项目` 的 systematic-debugging
- `文章` 的“不要让 agent 乱猜、乱补空白”

### 2. 不允许 blind fixes

- 不要先改代码再找原因。
- 不要同时改多个变量。
- 不要三次失败后还重复原路。

来源倾向：

- `项目`

## 九、多模型 / 多 agent 协作类经验

### 1. 多 agent 不是越多越好，关键在边界清晰

更适合拆开的角色：

- explorer
- reviewer
- docs researcher
- worker
- adversarial verifier
- referee

来源倾向：

- `文章` 提出了 bug-finder / adversarial / referee
- `项目` 提出了 coordinator + external model + reviewer role
- `论文` 从架构层支持 multi-actor context system

### 2. coordinator 负责判断，worker 负责执行

- 主 agent 更适合做：
  - 理解需求
  - 分解任务
  - 决策
  - 审核外部结果
- 执行型 agent 更适合：
  - 小范围实现
  - 独立分析
  - 独立验证

来源倾向：

- `项目`

### 3. 外部 agent 必须有写入边界

推荐约束：

- 只能改哪些文件
- 哪些文件只能读不能写
- 项目状态文件只能写指定 block
- 不能写全局知识库

来源倾向：

- `项目`
- `论文`

### 4. 多模型交叉验证比单点自信更可靠

适合交叉验证的场景：

- 架构方案
- 安全分析
- 风险评估
- 复杂 bug diagnosis
- critical business logic

来源倾向：

- `文章` 的 neutral + adversarial thinking
- `项目` 的 multi-model cross-verification

## 十、治理、安全、审计类经验

### 1. SSOT 非常重要

每类信息应只有一个 canonical location。

例如：

- 项目状态
- 技术坑点
- 活跃任务
- 长期目标
- 基础设施信息

来源倾向：

- `项目`

### 2. 上下文写回必须有治理

写回时至少要问：

- 谁写的
- 写到哪
- 为什么写
- 是否验证过
- 将来如何回放 / 回滚

来源倾向：

- `论文`
- `项目`

### 3. 外部内容和第三方 skill 要做安全检查

- 不要把外部 prompt/skill/mcp 当成可信配置。
- 要检查：
  - 网络调用
  - 数据外传
  - destructive ops
  - 动态执行
  - 伪装成“合规需求”的高风险指令

来源倾向：

- `项目`

## 十一、人类在环类经验

### 1. 人不是最后兜底，而是架构节点

人类应该负责：

- 决策边界
- 关键方案选择
- 低置信度结果复核
- 长期知识校准
- 价值判断和伦理判断

来源倾向：

- `论文`
- `文章`

### 2. 需要确认的点应该前置定义

不是所有事都要问人，但这些通常应该停下来确认：

- 技术栈变化
- 数据模型变化
- 关键架构取舍
- 生产影响操作
- 资金、权限、凭据、删除类操作

来源倾向：

- `项目`

## 十二、系统演化类经验

### 1. 规则和技能要持续增长，但也必须定期收缩

- 新规则、新 skill 会让 agent 更像你。
- 但积累到一定程度，一定会出现：
  - 冲突
  - 重复
  - 失效
  - 上下文污染
- 所以必须定期 consolidation。

来源倾向：

- `文章`
- `项目`

### 2. 工作流优化应和产出分时段

- 不要在日常执行时不停优化工作流本身。
- 把 workflow/system optimization 放到专门时间段更合理。

来源倾向：

- `项目` 的 Sunday Rule

## 十三、哪些经验最适合直接落地

如果只保留最值得执行的 12 条：

1. 顶层入口文件只做路由。
2. 上下文必须分层加载。
3. 研究和实现分开。
4. 每个复杂任务都写 contract。
5. 无验证不宣称完成。
6. 调试必须先找根因。
7. 关键状态必须落盘。
8. 热状态和长期知识分开。
9. 外部 agent 必须有写入边界。
10. 关键问题做多模型交叉验证。
11. 人类是正式治理节点。
12. 规则和技能定期收缩整理。

## 十四、最终统一判断

把三份材料合起来，可以得到一个非常清晰的统一结论：

- `文章` 告诉你怎样避免 agent 在单次任务里变笨。
- `项目` 告诉你怎样把这些经验做成稳定工作流。
- `论文` 告诉你怎样把工作流进一步升级成上下文基础设施。

一句话收束：

`短期要管好单次上下文，长期要设计好上下文系统。`
