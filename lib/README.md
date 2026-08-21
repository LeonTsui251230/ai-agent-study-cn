# lib —— 公共工具

各案例共用的小工具，避免重复代码。

- `model_client.py`：统一封装模型客户端（云端 API / 本地 Ollama），换模型只改一处。
- `config.py`：从环境变量读取配置（见根目录 `.env-example`）。
