# 11 Model I/O 与模型接入

“Model I/O”是 LangChain 里负责“和大模型打交道”的那一层：输入（提示词）、模型（调谁）、输出（怎么解析）。本章讲怎么把各种模型接进来，并保持代码可替换。

## 一、三类模型接口

- **Chat Model**：对话模型，输入输出是“消息列表”。最常用。
- **LLM**：传统补全模型，输入输出是纯文本。老接口，新项目用 Chat Model。
- **Embedding Model**：把文本变向量，用于 RAG（第 18 章）。

## 二、统一接口的好处

LangChain 让不同家的模型共用一套调用方式，换模型只改一行：

```python
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
# from langchain_anthropic import ChatAnthropic

llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatOllama(model="qwen2.5:7b")
```

业务代码（prompt、chain）完全不用动。这在“今天用 A 家、明天换 B 家”的场景里价值很大。

## 三、常用参数

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3,   # 0 最稳，1 最发散
    max_tokens=1024,   # 上限，控制成本
    timeout=30,
)
```

- `temperature`：越低越确定，写代码/抽取用 0，写文案用高一点。
- `max_tokens`：防止模型啰嗦烧钱。

## 四、多模态接入（图片）

```python
from langchain_core.messages import HumanMessage
msg = HumanMessage(content=[
    {"type": "text", "text": "这张图里有什么？"},
    {"type": "image_url", "image_url": {"url": "https://.../x.png"}},
])
print(llm.invoke([msg]).content)
```

## 下一步

模型想跑在本地不花钱？[12 Ollama 本地模型部署](12-Ollama本地部署与调用.md)。
