from .base_agent import BaseAgent

class HeadlineAgent(BaseAgent):
    """
    标题 Agent：根据话题和资料，生成新闻标题。
    """
    def run(self, topic: str, search_results: str) -> str:
        print("  [HeadlineAgent] 正在运行...")
        prompt = [
            {"role": "system", "content": "你是一位资深新闻主编。请根据用户提供的原始话题和背景资料，创作一个既准确又吸引人的新闻标题。"},
            {"role": "user", "content": f"原始话题：{topic}\n\n背景资料：\n{search_results}\n\n请直接输出你认为最佳的一个新闻标题。"}
        ]
        headline = self._create_chat_completion(prompt)
        print(f"  - 生成的标题: {headline}")
        print("  [HeadlineAgent] 标题制定完成。")
        return headline