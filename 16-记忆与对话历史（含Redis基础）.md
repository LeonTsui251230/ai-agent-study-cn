# 16 记忆与对话历史（含 Redis 基础）

没有记忆的 Bot 是“金鱼”：每轮都忘。本章讲怎么给对话加记忆，以及当对话多了怎么用 Redis 存。

## 一、记忆的两种形态

- **短期记忆**：单次会话内的上下文（最近几轮消息）。
- **长期记忆**：跨会话保留的用户偏好、历史摘要。

## 二、最简单的内存记忆

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

store = {}  # 会话ID -> 历史

def get_history(session_id):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# 在 chain 里用 RunnableWithMessageHistory 注入
```

## 三、为什么需要 Redis

内存字典 `store` 进程一关就没，且多实例部署时各进程不共享。生产环境用 Redis 这类外部存储：

```python
import redis
r = redis.Redis(host="localhost", port=6379, db=0)
r.set("session:123", history_json)
```

好处：重启不丢、多台机器共享同一份会话、可设过期时间自动清理。

## 四、记忆的注意事项

- **别无限堆积**：上下文越来越长，成本和延迟都涨。常用“只保留最近 N 轮”或“摘要压缩旧对话”。
- **隐私**：对话历史可能含敏感信息，Redis 要设访问控制和过期。
- **隔离**：不同用户/会话的历史必须分开存，不能串。

## 下一步

要让模型“能办事”，得给它工具——[17 Tools 工具调用](17-Tools工具调用.md)。
