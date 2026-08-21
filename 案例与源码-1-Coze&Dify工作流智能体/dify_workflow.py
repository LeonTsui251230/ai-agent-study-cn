"""调用 Dify 工作流型应用（见第 4 章）。"""
import os
import requests


def run_dify_workflow(inputs: dict, user: str = "user-123"):
    api_key = os.getenv("DIFY_API_KEY")
    base = os.getenv("DIFY_BASE_URL", "https://api.dify.ai/v1")
    resp = requests.post(
        f"{base}/workflows/run",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"inputs": inputs, "user": user},
        timeout=120,
    )
    return resp.json()["data"]["outputs"]
