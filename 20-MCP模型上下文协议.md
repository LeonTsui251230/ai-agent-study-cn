# 20 MCP 模型上下文协议

MCP（Model Context Protocol，模型上下文协议）是 2024 年后兴起的开放标准，用来统一“模型怎么连外部工具/数据”。本章讲它解决什么、长什么样。

## 一、它解决什么痛点

过去每个 Agent 框架都自己定义一套“工具接口”，A 框架写的工具 B 框架用不了。MCP 想做“USB 接口”：定义一套标准，任何模型客户端（Claude、自研 Agent）都能即插即用地连任何 MCP 服务（数据库、浏览器、文件系统…）。

## 二、三个角色

```
Host（宿主，如你的 Agent 程序）
  └─ Client（客户端，内嵌在 Host）
       └─ Server（服务端，提供能力：工具/资源/提示词）
```

Server 暴露三类能力：
- **Tools**：可被调用的函数（如“查订单”）。
- **Resources**：可被读取的数据（如“某文件内容”）。
- **Prompts**：预置的提示词模板。

## 三、一个 Server 长什么样（概念）

```python
# 用官方 SDK 声明一个工具
@mcp.tool()
def search_docs(query: str) -> str:
    """在内部知识库检索。"""
    return db.search(query)
```

Host 连上这个 Server 后，模型就知道有 `search_docs` 可用，无需改 Host 代码。

## 四、为什么对你重要

- **复用**：社区/公司写好的 MCP Server，你的 Agent 直接接。
- **解耦**：工具实现和模型客户端分离，换模型不重写工具。
- **生态**：越来越多产品原生支持 MCP，互连成本下降。

## 下一步

工具协议清楚了，正式进入 Agent——[21 Agent 智能体原理](21-Agent智能体.md)。
