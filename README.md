# OpenClaw
智能体记忆存储模块改造（JSON→SQLite）作业

安装虚拟环境：python3.10
安装库：pip install langchain langchain-community openai python-dotenv -i https://pypi.tuna.tsinghua.edu.cn/simple

 配置环境和安装库好运行代码文件python agent_test.py
 
# OpenClaw 智能体记忆存储模块改造（JSON→SQLite）

## 📌 一、项目概述
本项目为课程作业，对开源智能体框架 OpenClaw 的记忆存储模块进行改造，将默认的 JSON 文件存储替换为 SQLite 数据库存储，解决了 JSON 存储在数据量增大时检索缓慢、并发不安全、无结构化查询能力等问题，实现了更高效、稳定的记忆读写功能。

---

## 🎯 二、任务目标与问题背景
### 1. 任务目标
调研并改造智能体的记忆存储策略，将 JSON 文件存储改为 SQLite 数据库存储，对比分析两种方案的优劣，验证改造效果。

### 2. 原方案（JSON存储）的痛点
- **检索效率低**：每次读取记忆需要全量加载文件，数据量超过1000条后性能急剧下降
- **并发不安全**：多线程写入时易出现数据冲突，需手动加锁
- **无结构化查询**：无法按时间、角色等条件高效筛选记忆
- **扩展性差**：单文件存储，数据量过大后文件膨胀，难以维护

---

## 🔍 三、技术方案设计
### 1. 改造思路
- 用 SQLite 数据库替代 JSON 文件作为记忆存储介质
- 设计结构化的 `memories` 表，存储对话角色、内容、时间戳
- 为时间戳字段建立索引，提升时间维度的查询性能
- 保留原智能体的调用接口，实现无缝替换

### 2. 数据库设计
```sql
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    role TEXT NOT NULL,
    content TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_timestamp ON memories(timestamp);
## 🔍 四、技术方案设计
### <img width="764" height="459" alt="image" src="https://github.com/user-attachments/assets/561a77b2-d088-4ee7-b99e-39573e6f7f41" />

