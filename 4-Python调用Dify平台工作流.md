# 4 Python 调用 Dify 平台工作流

平台做原型很快，但要嵌进你自己的系统，就得用 API 把它的工作流调起来。本章以 Dify 为例，讲清楚怎么用 Python 触发一个对话型/工作流型应用。

## 一、两种调用形态

- **对话型应用（Chat）**：你发消息、它回消息，适合问答 Bot。
- **工作流型应用（Workflow）**：你填一组输入变量、它跑完整条流水线返回结果，适合“批量处理/固定流程”。

## 二、拿到 API Key 与地址

在 Dify 应用页的“访问 API”里能拿到：
- `API_KEY`：应用的密钥
- `BASE_URL`：通常是 `https://api.dify.ai/v1` 或你私有部署的地址

## 三、调用对话型应用（示例）

```python
import requests

API_KEY = "app-xxxxxxxx"
BASE = "https://api.dify.ai/v1"

resp = requests.post(
    f"{BASE}/chat-messages",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "inputs": {},
        "query": "差旅报销上限是多少？",
        "user": "user-123",          # 用于会话隔离
        "response_mode": "blocking", # 或 streaming
    },
    timeout=60,
)
print(resp.json()["answer"])
```

## 四、调用工作流型应用（示例）

```python
resp = requests.post(
    f"{BASE}/workflows/run",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "inputs": {"topic": "人工智能代理", "length": 300},
        "user": "user-123",
    },
    timeout=120,
)
print(resp.json()["data"]["outputs"])
```

## 五、生产环境要注意

- **密钥别写死在代码里**：放环境变量或密钥管理（见 `.env-example`）。
- **用 streaming 处理长任务**：避免请求超时。
- **做好错误重试与降级**：平台抖动时返回友好提示，而不是把异常抛给用户。

## 下一步

Coze 的调用方式类似，见 [5 Python 调用 Coze 工作流](5-Python调用Coze平台工作流.md)。
