import sqlite3
from typing import List, Dict

DB_PATH = "memory.db"

def init_db():
    """初始化SQLite数据库"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # 创建记忆表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            role TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    # 为时间戳创建索引，提升查询性能
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON memories(timestamp)')
    conn.commit()
    return conn

def save_memory(role: str, content: str):
    """保存对话记忆到数据库"""
    conn = init_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO memories (role, content) VALUES (?, ?)",
            (role, content)
        )
        conn.commit()
    except Exception as e:
        print(f"写入失败: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_recent_memories(count: int = 10) -> List[Dict]:
    """获取最近N条记忆（利用索引高效查询）"""
    conn = init_db()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM memories ORDER BY timestamp DESC LIMIT ?",
        (count,)
    )
    rows = cursor.fetchall()
    conn.close()
    # 按时间正序返回，保持对话上下文顺序
    return [dict(row) for row in reversed(rows)]