"""supervisor 多智能体骨架（见第 26 章）。"""
from langgraph.graph import StateGraph, START, END
from lib.model_client import get_chat_model


def supervisor(state):
    # 真实实现里用模型判断下一步该谁做
    return "worker"


def build():
    b = StateGraph(dict)
    b.add_node("supervisor", supervisor)
    b.add_node("worker", lambda s: {"done": True})
    b.add_edge(START, "supervisor")
    b.add_conditional_edges("supervisor", supervisor, {"worker": "worker", END: END})
    b.add_edge("worker", END)
    return b.compile()
