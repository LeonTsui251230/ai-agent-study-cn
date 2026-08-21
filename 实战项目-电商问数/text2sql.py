"""问题转 SQL（示意）。"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lib.model_client import get_chat_model

PROMPT = ChatPromptTemplate.from_messages([
    ("system", "你是数据分析师。只输出一条 SELECT SQL，禁止写操作。表结构：orders(id, category, amount, created_at)"),
    ("human", "{question}"),
])


def question_to_sql(question: str) -> str:
    chain = PROMPT | get_chat_model() | StrOutputParser()
    return chain.invoke({"question": question}).strip()
