# 24 LangGraph API：节点、边与进阶

在基础图之上，LangGraph 还有几个能让生产级 Agent 更稳的特性。本章讲条件边、人工介入、子图。

## 一、更复杂的边

除了 `add_conditional_edges`，还能：
- **带权重的路由**：根据打分走不同分支。
- **并行边**：一个节点输出同时发给多个下游节点（`START → [a, b]`）。

```python
builder.add_edge(START, ["summarize", "translate"])  # 并行两路
```

## 二、人工介入（Human-in-the-loop）

敏感操作（发邮件、扣款）让人在环里确认：

```python
from langgraph.types import interrupt

def approve(state):
    decision = interrupt({"ask": "确认要发送吗？"})
    if decision == "no":
        return {"blocked": True}
    return {}
```

`interrupt` 会暂停图、把问题抛给外部，等人回复后从断点继续——这对生产安全很重要。

## 三、子图（Subgraph）

把“一个完整流程”封装成子图，当成一个节点嵌进大图：

```python
builder.add_node("research", research_subgraph)  # 子图作为节点
```

好处：复杂 Agent 可以分层，每层单独测试。

## 四、持久化与断点续跑

LangGraph 配合 checkpoint（如 Redis/Postgres）能把状态存下来：

```python
graph = builder.compile(checkpointer=memory)
graph.invoke(inputs, config={"configurable": {"thread_id": "u1"}})
```

`thread_id` 相同的调用共享状态，支持中途挂起、稍后恢复——多轮对话和长任务必备。

## 下一步

更进阶的玩法——[25 LangGraph 高级特性](25-LangGraph高级特性.md)。
