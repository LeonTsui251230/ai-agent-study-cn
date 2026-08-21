"""统一模型客户端封装：本地 Ollama 与云端 API 二选一。"""
import os


def get_chat_model(kind: str = "ollama", model: str = "qwen2.5:7b"):
    """返回 LangChain ChatModel 实例。

    kind="ollama" 走本机免费模型；kind="cloud" 走 .env 里的 API。
    """
    if kind == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=model, base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),
    )
