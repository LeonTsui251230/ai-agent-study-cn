# 10 LangChain 快速上手与 Hello World

先跑通，再理解。本章带你用最少代码调通 LangChain，建立“它能干活”的体感。

## 一、安装

```bash
pip install langchain langchain-openai
```

> 国内网络拉包慢时，可换镜像源；模型调用需要能访问对应 API 或本地服务（第 12 章 Ollama）。

## 二、最小示例：模板 + 模型 + 解析

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("用一句话解释：{topic}")
llm = ChatOpenAI(model="gpt-4o-mini")  # 换成你可用的模型
parser = StrOutputParser()

chain = prompt | llm | parser
print(chain.invoke({"topic": "什么是人工智能代理"}))
```

跑起来，你会看到模型用一句话回答了问题。这就是 LCEL 的 `prompt | llm | parser` 三件套。

## 三、把模型换成 Ollama（本地、免费）

```python
from langchain_ollama import ChatOllama
llm = ChatOllama(model="qwen2.5:7b")  # 需先装好 Ollama 并拉模型
```

这样整条链不用花一分钱、数据不出本机。第 12 章专门讲。

## 四、你刚刚经历了什么

1. `prompt` 把 `{topic}` 填成完整提示词。
2. `llm` 调用模型拿到回复。
3. `parser` 把模型输出整理成字符串。
4. `chain.invoke` 一次性跑完三步。

这三步的组合，就是后面所有复杂应用的积木。

## 下一步

想换模型、传多模态、控制参数？[11 模型接入 Model I/O](11-Model-I-O与模型接入.md)。
