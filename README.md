# WEMIX 链分析工具

该项目提供一个基础示例，用于抓取 WEMIX 链的区块数据并通过
Web 页面展示。

## 依赖

- Python 3.11
- `web3`
- `sqlalchemy`
- `flask`
- `python-dotenv`（可选，用于读取环境变量）

由于环境可能无法访问网络，请提前准备好依赖安装包。

## 使用方法

1. 设置环境变量 `WEMIX_RPC_URL`，指向可访问的 WEMIX RPC 端点。
2. 运行 `python monitor.py` 抓取最新区块数据并存入本地数据库
   （默认为 `data.sqlite`）。
3. 运行 `python app.py` 启动 Web 服务，在浏览器中查看区块信息。

## 测试

项目包含简单的单元测试，可通过 `pytest` 执行：

```bash
pytest
```
