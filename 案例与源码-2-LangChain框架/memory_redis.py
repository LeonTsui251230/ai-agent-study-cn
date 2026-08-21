"""用 Redis 存对话历史（见第 16 章）。"""
import redis
from langchain_community.chat_message_histories import RedisChatMessageHistory

history = RedisChatMessageHistory(session_id="u1", url="redis://localhost:6379/0")
history.add_user_message("你好")
history.add_ai_message("你好，有什么可以帮您？")
print([m.content for m in history.messages])
