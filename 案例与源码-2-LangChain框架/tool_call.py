"""工具调用示例（见第 17 章）。"""
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from lib.model_client import get_chat_model


@tool
def get_weather(city: str) -> str:
    """查询城市天气。"""
    return f"{city} 晴 25℃"


def main():
    agent = create_tool_calling_agent(get_chat_model(), [get_weather], ChatPromptTemplate.from_messages([("system", "你有用天气工具。"), ("human", "{input}")]))
    print(AgentExecutor(agent=agent, tools=[get_weather], verbose=True).invoke({"input": "上海天气？"}))
