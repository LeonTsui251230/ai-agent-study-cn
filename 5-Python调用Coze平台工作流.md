# 5 Python 调用 Coze 工作流

Coze（扣子）的 Bot 同样能通过 API 接入你自己的程序。本章讲怎么用 Python 调用一个已发布的 Coze Bot / 工作流。

## 一、发布与取凭证

1. 在 Coze 里把 Bot **发布**，并勾选“API”渠道（或在工作流里发布为 API）。
2. 在“API 管理”里创建凭证，拿到 `Personal Access Token`（PAT）。
3. 拿到 Bot 的 `bot_id`（或工作流的 `workflow_id`）。

## 二、调用对话 Bot（示例）

```python
import requests

PAT = "pat_xxxxxxxx"
BOT_ID = "739xxxxxxxx"

resp = requests.post(
    "https://api.coze.cn/v3/chat",
    headers={
        "Authorization": f"Bearer {PAT}",
        "Content-Type": "application/json",
    },
    json={
        "bot_id": BOT_ID,
        "user_id": "user-123",
        "stream": False,
        "auto_save_history": True,
        "additional_messages": [
            {"role": "user", "content": "帮我把这段话改成正式邮件", "content_type": "text"}
        ],
    },
    timeout=60,
)
data = resp.json()
print(data)
```

## 三、轮询拿结果

Coze 的异步接口通常先返回一个 `conversation_id` / `chat_id`，再用另一个接口轮询消息。生产代码要处理这个两步流程，并加上超时与重试。

## 四、和 Dify 的差异小结

| 维度 | Dify | Coze |
| --- | --- | --- |
| 对话接口 | `/chat-messages` | `/v3/chat` + 轮询 |
| 工作流接口 | `/workflows/run` | 工作流 API |
| 私有部署 | 支持 | 主要是云端 |

## 五、何时该自己写

当调用逻辑里出现“调完 Coze 还要调内部系统、再回来判断”的环路时，说明你已经超出平台边界，应该考虑用 LangChain/LangGraph 在代码里编排（第 9 章起）。

## 下一步

想把 Bot 跑在本地或内网？[6 Coze 与 Dify 的部署](6-Coze与Dify的部署.md) 讲私有化与本地化选项。
