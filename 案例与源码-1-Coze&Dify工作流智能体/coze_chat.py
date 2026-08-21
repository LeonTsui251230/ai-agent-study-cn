"""调用 Coze 对话 Bot（见第 5 章）。"""
import os
import requests


def chat_coze(query: str, user_id: str = "user-123"):
    pat = os.getenv("COZE_PAT")
    bot_id = os.getenv("COZE_BOT_ID")
    resp = requests.post(
        "https://api.coze.cn/v3/chat",
        headers={"Authorization": f"Bearer {pat}", "Content-Type": "application/json"},
        json={
            "bot_id": bot_id,
            "user_id": user_id,
            "stream": False,
            "additional_messages": [{"role": "user", "content": query, "content_type": "text"}],
        },
        timeout=60,
    )
    return resp.json()
