# 25 LangGraph 高级特性

本章补充几个把 Agent 做到“生产可用”的关键能力：流式、回溯、观测、容错。

## 一、流式输出（Streaming）

长任务用户等得心焦，要边跑边吐：

```python
for chunk in graph.stream(inputs, stream_mode="messages"):
    print(chunk, end="", flush=True)
```

`stream_mode` 支持输出 token、节点状态、完整事件，按你需要选。

## 二、时光回溯（Time Travel）

出错时回到某个历史节点重跑，而不是从头来：

```python
states = graph.get_state_history(config)
graph.invoke(None, config_with_target=states[-2].config)  # 回到倒数第二步
```

调试复杂流程时极好用。

## 三、观测（Observability）

把每个节点的输入输出、耗时、token 记录下来，接 LangSmith 或自建日志，定位“为什么这步慢/错”。

## 四、容错与预算

- **最大步数**：防止 Agent 死循环（`recursion_limit`）。
- **工具超时**：单个工具卡住不能拖垮整体。
- **降级**：关键工具失败，给模型一个“替代路径”提示而非崩溃。

## 五、何时上这些高级特性

原型阶段都用不上。一旦你要把它交给真实用户、跑真实任务，流式、回溯、观测、预算这四项几乎一个都少不了。

## 下一步

一个 Agent 不够，要多个协作——[26 多智能体与 A2A](26-LangGraph多智能体与A2A.md)。
