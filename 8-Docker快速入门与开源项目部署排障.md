# 8 Docker 快速入门与开源项目部署排障

Docker 是今天部署任何开源 AI 项目的标配。本章给你够用的 Docker 常识，以及部署 Dify 这类项目时最高频的排障清单。

## 一、三个核心概念

- **镜像（Image）**：一个打包好的“环境 + 程序”模板。
- **容器（Container）**：镜像跑起来的一次实例。
- **Compose**：用一个 `docker-compose.yml` 把多个容器（Web、数据库、向量库）一起编排起来。

## 二、最常用的几条命令

```bash
docker compose up -d        # 后台启动一组服务
docker compose ps           # 看哪些容器在跑
docker compose logs -f web  # 跟踪某个服务的日志
docker compose down         # 停止并删除容器
docker system prune         # 清理无用的镜像/容器（谨慎）
```

## 三、部署 Dify 时的高频坑

| 现象 | 可能原因 | 处理 |
| --- | --- | --- |
| 端口被占用 | 80 端口已有 Nginx | 改 `docker-compose.yml` 的端口映射 |
| 向量库连不上 | 容器间网络名写错 | 用 compose 服务名而非 localhost |
| 上传文件失败 | 卷没挂载或权限不足 | 检查 volumes 配置 |
| 启动后白屏 | 前端没编译/反向代理错 | 看 web 容器日志 |

## 四、一个排障心法

**先看日志，再猜原因**。90% 的部署问题在 `docker compose logs` 里都有明确报错。不要反复重启，先把报错贴出来定位。

## 下一步

环境标准了，开始用代码搭能力。下一章进入 [9 LangChain 概述与架构](9-LangChain概述与架构.md)。
