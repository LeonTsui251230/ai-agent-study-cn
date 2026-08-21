# 9 LangChain 概述与架构

前面用平台能快速出原型，但要做到精细控制，得上代码框架。LangChain 是目前最主流的 LLM 应用框架之一。本章讲它的设计思路和核心模块，帮你建立心智模型。

## 一、LangChain 解决什么

裸调大模型 API 时，你要自己管：提示词拼接、多轮记忆、工具调用、结果解析、把多个步骤串起来。LangChain 把这些“胶水代码”组件化，让你用统一的方式拼装。

## 二、核心模块（一张图）

```
Model I/O  ──►  Prompt(模板) → LLM(模型) → Output Parser(解析)
     │
Retrieval  ──►  Document Loaders → Text Splitters → Embeddings → VectorStore
     │
Agents     ──►  Tools → Agent(决策循环) → Executor
     │
Chains     ──►  把上面这些串成流水线（LCEL）
     │
Memory     ──►  对话历史（短期/长期）
```

后面几章就是逐个展开这些模块：模型接入（11）、本地模型（12）、模板（13）、解析（14）、链（15）、记忆（16）、工具（17）、向量库（18）、RAG（19）。

## 三、LCEL 是什么

LCEL（LangChain Expression Language）是用 `|` 把组件串起来的写法：

```python
chain = prompt | llm | parser
```

它取代了老式的 `LLMChain`，支持流式、并行、回退，是现在推荐的主力写法。第 15 章细讲。

## 四、什么时候该用 LangChain

- 需要把“检索 + 工具 + 多步逻辑”灵活组合。
- 要换模型/换向量库时不想重写整套代码（LangChain 抽象层帮你解耦）。

什么时候**不该用**：需求极简单（一个提示词就够），上框架反而是负担。先看第 10 章的最小例子体会一下。

## 下一步

理论够了，[10 LangChain 快速上手](10-LangChain快速上手与HelloWorld.md) 跑通第一个程序。
