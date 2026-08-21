"""最小 RAG 链（见第 19 章）。"""
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

docs = ["退款周期7天。", "会员享9折。"]
vs = Chroma.from_texts(docs, OpenAIEmbeddings())
prompt = ChatPromptTemplate.from_messages([("system", "只依据资料回答，无依据说不知道。"), ("human", "{input}")])
chain = create_retrieval_chain(vs.as_retriever(), create_stuff_documents_chain(ChatOpenAI(), prompt))
print(chain.invoke({"input": "退款多久？"})["answer"])
