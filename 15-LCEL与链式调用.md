# 15 LCEL 与链式调用

LCEL 是 LangChain 推荐的“把组件串成流水线”的写法。本章讲它怎么用，以及为什么比老式 Chain 好。

## 一、基本写法：`|`

```python
from langchain_core.runnables import RunnablePassthrough

chain = (
    {"context": lambda d: retrieve(d["q"]), "q": RunnablePassthrough()}
    | prompt
    | llm
    | parser
)

print(chain.invoke({"q": "退款多久到账"}))
```

`|` 表示“上一个的输出喂给下一个”，和 Unix 管道一个思路。

## 二、为什么用 LCEL 而非 LLMChain

| 能力 | LCEL | 老 LLMChain |
| --- | --- | --- |
| 流式输出 | ✅ | ❌ |
| 并行分支 | ✅ | ❌ |
| 失败回退 | ✅ | ❌ |
| 异步 | ✅ | 有限 |

## 三、并行与分支

```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel({
    "summary": summary_chain,
    "sentiment": sentiment_chain,
})
# 两个子链并行跑，合并结果
```

## 四、回退（容错）

```python
from langchain_core.runnables import RunnableLambda

primary = llm_expensive.with_fallbacks([llm_cheap])
# 主模型失败自动用廉价模型兜底
```

## 下一步

多轮对话要记住历史——[16 记忆与对话历史](16-记忆与对话历史（含Redis基础）.md)。
