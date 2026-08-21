"""入口：读问题、跑图、打印报告。"""
from agent import build

if __name__ == "__main__":
    graph = build()
    q = input("请输入研究问题：")
    result = graph.invoke({"question": q, "messages": [], "report": ""})
    print("\n==== 综述报告 ====\n")
    print(result["report"])
