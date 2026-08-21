# 23 LangGraph API：图与状态

本章展开 LangGraph 的两个核心：State（状态）怎么定义与合并，Graph（图）怎么构建。

## 一、State 的合并机制

State 不是“覆盖”，而是“合并”。默认对列表类型做**追加**（适合消息历史），对字典做**覆盖**或自定义 reducer。

```python
from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]  # 自动追加消息
    step: int
```

`add_messages` 是内置 reducer，保证每轮新消息被追加而不是替换，这正是多轮对话需要的。

## 二、节点就是普通函数

```python
def call_model(state: State):
    res = llm.invoke(state["messages"])
    return {"messages": [res]}  # 返回增量，由 reducer 合并

def call_tool(state: State):
    # 执行上一步决定的工具
    ...
    return {"messages": [tool_result]}
```

## 三、构建图的完整流程

```python
from langgraph.graph import StateGraph, START, END

builder = StateGraph(State)
builder.add_node("model", call_model)
builder.add_node("tools", call_tool)
builder.add_edge(START, "model")
builder.add_conditional_edges(
    "model",
    should_continue,           # 函数：决定下一步
    {"tools": "tools", END: END},
)
builder.add_edge("tools", "model")  # 工具结果回到模型，形成循环
graph = builder.compile()
```

## 四、should_continue：条件分支

```python
def should_continue(state: State):
    last = state["messages"][-1]
    if last.tool_calls:   # 模型要调工具
        return "tools"
    return END            # 否则结束
```

这就是 ReAct 循环在 LangGraph 里的标准写法。

## 下一步

节点、边还有更多玩法——[24 LangGraph：节点、边与进阶](24-LangGraphAPI：节点、边与进阶.md)。
