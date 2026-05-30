from storage_sqlite import save_memory, get_recent_memories, init_db

class SimpleAgent:
    def __init__(self):
        # 初始化数据库
        init_db()
        print("✅ 智能体初始化完成，使用SQLite存储记忆")

    def chat(self, user_input: str) -> str:
        # 保存用户输入
        save_memory("user", user_input)
        # 获取最近5条对话历史
        history = get_recent_memories(5)
        # 模拟回复
        response = f"已收到消息：{user_input}（已读取{len(history)}条历史对话）"
        # 保存助手回复
        save_memory("assistant", response)
        return response

if __name__ == "__main__":
    agent = SimpleAgent()
    while True:
        user_msg = input("你：")
        if user_msg.lower() == "exit":
            break
        reply = agent.chat(user_msg)
        print(f"助手：{reply}")