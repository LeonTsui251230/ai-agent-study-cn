"""单 Agent ReAct 循环（见第 21~23 章）。"""
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END, add_messages
from langchain_core.tools import tool
from lib.model_client import get_chat_model


@tool
def calc(expr: str) -> str:
    """计算表达式。"""
    return str(eval(expr))


class State(TypedDict):
    messages: Annotated[list, add_messages]


def build():
    # 标准 ReAct：model -> (有工具调用则 tools -> model，否则 END)
    b = StateGraph(State)
    b.add_node("model", lambda s: {"messages": [get_chat_model().bind_tools([calc]).invoke(s["messages"])]})
    b.add_node("tools", lambda s: {"messages": [calc.invoke(s["messages"][-1].tool_calls[0]["args"])]})
    b.add_conditional_edges("model", lambda s: "tools" if s["messages"][-1].tool_calls else END, {"tools": "tools", END: END})
    b.add_edge("tools", "model")
    b.add_edge(START, "model")
    return b.compile()
