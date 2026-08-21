# 22 LangGraph 概述与快速入门

当流程不再是“一条直线”，而是有分支、循环、多角色，LCEL 的线性链就不够了。LangGraph 用“图”来编排 Agent，本章讲它是什么、为什么需要它。

## 一、LangChain 和 LangGraph 的关系

- **LangChain（LCEL）**：适合线性流水线（A→B→C）。
- **LangGraph**：适合有状态、有分支、可循环的流程，把每一步画成图上的“节点”，流转画成“边”。

很多 Agent 框架本质是“隐式图”，LangGraph 把它显式画出来，便于控制和调试。

## 二、核心概念

- **State（状态）**：在节点间传递的共享数据（如消息列表、中间结果）。
- **Node（节点）**：一个处理函数，读 State、写 State。
- **Edge（边）**：节点间的流转规则，可条件分支。
- **END**：终止节点。

## 三、最小示例：两个节点

```python
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    text: str
    length: int

def count(s: State):
    return {"length": len(s["text"])}

builder = StateGraph(State)
builder.add_node("count", count)
builder.add_edge(START, "count")
builder.add_edge("count", END)

graph = builder.compile()
print(graph.invoke({"text": "你好世界", "length": 0}))
```

虽然简单，但已经体现了“状态在节点间流动”的思想。

## 四、为什么用它做 Agent

- **可控**：哪步能循环、什么条件走哪条边，你写死，不会乱跑。
- **可持久化**：状态能存库，流程可暂停/恢复。
- **可观测**：每个节点的输入输出都能打印，调试友好。

## 下一步

深入 State 与图 API——[23 LangGraph：图与状态](23-LangGraphAPI：图与状态.md)。
