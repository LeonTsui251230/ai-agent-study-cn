# 18 向量数据库与 Embedding 实战

RAG 的“记忆”靠向量数据库。本章讲 Embedding 是什么、向量库怎么用、选型看什么。

## 一、Embedding 是什么

Embedding 模型把一段文字变成一串浮点数（向量）。语义相近的文字，向量在空间中距离也近。这样“找相似文字”就变成了“算向量距离”。

```
"退款政策"  ──embed──► [0.12, -0.03, ..., 0.88]
"怎么退钱"  ──embed──► [0.11, -0.04, ..., 0.85]  # 距离很近 → 语义相似
```

## 二、常见向量库

| 库 | 特点 | 适用 |
| --- | --- | --- |
| FAISS | 本地、轻量、快 | 原型、小数据 |
| Chroma | 易上手、嵌入式 | 学习、单机 |
| Qdrant | 性能好、可部署 | 生产 |
| Milvus | 分布式、大规模 | 企业级 |

## 三、最小实战（Chroma）

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

docs = ["退款周期7天", "会员享9折", "发票可在线开具"]
vectorstore = Chroma.from_texts(docs, OpenAIEmbeddings())

hits = vectorstore.similarity_search("怎么退款", k=1)
print(hits[0].page_content)  # 退款周期7天
```

## 四、选型的三个维度

- **规模**：几百条用 FAISS/Chroma；上亿条得上 Milvus/Qdrant 集群。
- **部署**：要不要独立服务、能不能嵌进应用。
- **检索质量**：是否支持混合检索（向量 + 关键词），混合通常比纯向量准。

## 下一步

把向量库接进生成流程，就是完整 RAG——[19 RAG 检索增强生成](19-RAG检索增强生成.md)。
