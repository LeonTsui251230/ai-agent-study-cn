"""深度研搜 Agent 的 LangGraph 骨架（示意）。"""
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END, add_messages
from lib.model_client import get_chat_model


class State(TypedDict):
    question: str
    messages: Annotated[list, add_messages]
    report: str


def plan(state: State):
    llm = get_chat_model()
    sub = llm.invoke(f"把问题拆成3个子问题：{state['question']}")
    return {"messages": [sub]}


def research(state: State):
    # 这里调用搜索工具检索每个子问题
    return {"messages": [type("M", (), {"content": "（检索结果）"})()]}


def write(state: State):
    llm = get_chat_model()
    report = llm.invoke(f"基于讨论写综述：{state['question']}")
    return {"report": report.content}


def build():
    b = StateGraph(State)
    b.add_node("plan", plan)
    b.add_node("research", research)
    b.add_node("write", write)
    b.add_edge(START, "plan")
    b.add_edge("plan", "research")
    b.add_edge("research", "write")
    b.add_edge("write", END)
    return b.compile()
