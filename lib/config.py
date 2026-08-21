"""从环境变量读取配置，集中管理。"""
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "ollama_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    "redis_url": os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    "top_k": int(os.getenv("TOP_K", "3")),
}
