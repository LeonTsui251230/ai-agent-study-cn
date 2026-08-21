# 19 RAG 检索增强生成

把第 2 章的原理、第 18 章的向量库，用代码串成一条能跑的 RAG 链。本章给你一个端到端示例和常见优化。

## 一、端到端 RAG 链

```python
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = create_stuff_documents_chain(llm, prompt)
rag = create_retrieval_chain(retriever, qa_chain)

result = rag.invoke({"input": "退款多久到账？"})
print(result["answer"])
print(result["context"])  # 看看它检索到了哪些片段，便于核对
```

`create_retrieval_chain` 会自动：检索 → 把片段塞进 prompt → 调模型 → 返回答案和来源。

## 二、四类常见优化

1. **混合检索**：向量检索 + 关键词（BM25），召回更全。
2. **重排序（Rerank）**：先广召回、再用小模型把最相关的排前面。
3. **父子切片**：检索用小块、喂模型用大块，兼顾精度与上下文。
4. **来源返回**：把引用段落返回用户，建立信任也方便纠错。

## 三、评估 RAG 靠什么

别只看“答得顺不顺”，要看：
- **检索命中率**：相关问题有没有捞到正确片段。
- **答案忠实度**：回答是否真来自检索内容，而非模型编造。
- **无依据时表现**：知识库没有时，是否老实说“不知道”。

## 四、RAG 的边界

RAG 解决“知识”问题，不解决“办事”问题。当用户要“去查并下单”“跨系统编排”时，需要 Agent——下一章 [20 MCP](20-MCP模型上下文协议.md) 先铺垫一个关键协议。

## 下一步

[21 Agent 智能体原理](21-Agent智能体.md) 讲怎么让模型主动循环决策。
