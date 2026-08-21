# 17 Tools 工具调用

工具调用（Function Calling / Tool Use）是 Agent 的发动机：让模型决定“调哪个函数、传什么参数”，从而突破“只能说话”的限制。

## 一、原理

```
模型看到一组工具定义（名字+参数schema）
  → 模型判断该调哪个、填什么参数
  → 你的代码执行该函数，拿到结果
  → 结果回传给模型
  → 模型继续（或直接回答）
```

模型本身不执行函数，它只“决定调用”，真正执行的是你的代码。

## 二、定义一个工具

```python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """查询指定城市的天气。"""
    # 这里实际调用天气 API
    return f"{city} 今天晴，25℃"

# 模型现在知道有 get_weather 这个工具可用
```

## 三、让模型自动选工具

```python
from langchain.agents import create_tool_calling_agent, AgentExecutor

tools = [get_weather]
agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

executor.invoke({"input": "上海天气怎么样？"})
```

`verbose=True` 会打印模型的“思考—调用—观察”过程，非常适合学习 Agent 内部在干嘛。

## 四、工具设计的三个要点

1. **描述要清楚**：模型的 `"""docstring"""` 就是它理解工具的依据，写清“干什么、参数含义”。
2. **参数要收敛**：让模型填的字段越少越准，复杂对象让工具内部处理。
3. **执行要安全**：工具可能写数据库、发请求，生产环境必须加权限和白名单。

## 下一步

RAG 的“检索”本质也是一个工具。先补向量库基础——[18 向量数据库与 Embedding](18-向量数据库与Embedding实战.md)。
