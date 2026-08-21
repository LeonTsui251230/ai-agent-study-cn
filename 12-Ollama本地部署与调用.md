# 12 Ollama 本地模型部署与调用

Ollama 让你在笔记本上“一行命令”跑开源大模型。数据不出本机、零调用费，是学习和做原型的最佳选择。

## 一、安装与拉模型

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# 拉一个模型（以 Qwen2.5 7B 为例）
ollama pull qwen2.5:7b

# 直接对话测试
ollama run qwen2.5:7b
```

## 二、作为本地服务调用

Ollama 默认起在 `http://localhost:11434`，支持 OpenAI 兼容接口。在 LangChain 里：

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
    temperature=0,
)
print(llm.invoke("用一句话解释向量数据库").content)
```

## 三、在 Dify / 其他框架里接 Ollama

把模型类型选“Ollama”，填 `http://localhost:11434` 和模型名即可。这样你之前在第 3 章搭的 Bot 立刻变成“全本地、免费”。

## 四、本地部署的取舍

| 优点 | 注意 |
| --- | --- |
| 免费、隐私好 | 小模型能力弱于云端大模型 |
| 离线可用 | 需要本机有够用的内存/显存 |
| 改提示词零成本试错 | 7B 模型复杂推理会掉链子 |

经验：学习与原型阶段用 Ollama，生产要质量时再接云端大模型，代码几乎不用改（第 11 章的统一接口）。

## 下一步

要把提示词写得更稳，用模板而非拼接字符串——[13 提示词与消息模板](13-提示词与消息模板.md)。
