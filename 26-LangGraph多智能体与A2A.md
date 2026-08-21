# 26 LangGraph 多智能体与 A2A 协作

复杂任务交给一个“全能 Agent”容易顾此失彼。多智能体（Multi-Agent）让多个专长 Agent 分工协作，像一个小团队。本章讲模式与 A2A 概念。

## 一、两种组织方式

**1.  supervisor（主管）模式**：一个主管 Agent 负责派活，多个工人 Agent 干活。

```
        ┌──────────┐
        │ supervisor│
        └────┬─────┘
     ┌──────┼──────┐
  研究员   写手    审查
```

**2.  peer-to-peer（平级）模式**：Agent 之间直接对话交接，适合没有明确上下级的场景。

## 二、supervisor 示例（概念）

```python
def supervisor(state):
    # 判断下一步该谁做
    return "researcher"  # 或 "writer" / "reviewer" / END

builder.add_conditional_edges("supervisor",
    supervisor,
    {"researcher": "researcher", "writer": "writer",
     "reviewer": "reviewer", END: END})
```

每个工人 Agent 本身又是一个小图（或 LangChain chain），只负责自己那块。

## 三、A2A（Agent-to-Agent）

A2A 是让**不同框架/不同厂商**的 Agent 能互相通信的协议思路（类似 MCP 但面向 Agent 间）。它的价值在于：你的“研究员”可以是 LangGraph 写的，对方的“执行器”是另一个系统，两者能对话协作。

## 四、多智能体的坑

- **沟通成本**：Agent 间传太多中间结果，慢且易错。定义清楚“交接什么”。
- **责任不清**：谁该兜底？要有明确的终止与上报机制。
- **成本翻倍**：每多一个 Agent 就多一排模型调用，先确认“单 Agent 真做不了”再拆分。

## 下一步

给 Agent 加上“可复用技能包”——[27 Skills 技能与 AI 编程工具](27-Skills技能与AI编程工具实践.md)。
