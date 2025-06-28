from .base_agent import BaseAgent

class OutlineAgent(BaseAgent):
    """
    大纲生成 Agent：根据标题和资料制定新闻大纲。
    """
    def run(self, headline: str, search_results: str) -> list[str]:
        print("  [OutlineAgent] 正在运行...")
        prompt = [
            {"role": "system", "content": "你是一名专业的新闻撰稿人。请根据给定的新闻标题和背景资料，设计一个清晰、有逻辑的新闻稿大纲。大纲应包含引言、主体段落要点和结论。请以无序列表（- ）的形式返回，每个要点占一行。"},
            {"role": "user", "content": f"新闻标题：{headline}\n\n背景资料：\n{search_results}\n\n请输出新闻大纲。"}
        ]
        outline_str = self._create_chat_completion(prompt)
        outline_points = [point.strip().lstrip('- ').strip() for point in outline_str.split('\n') if point.strip()]
        print("  - 生成的大纲:")
        for point in outline_points:
            print(f"    - {point}")
        print("  [OutlineAgent] 大纲生成完成。")
        return outline_points