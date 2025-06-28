from .base_agent import BaseAgent

class ReviewAgent(BaseAgent):
    """
    评论 Agent：对整篇文章的文笔、流畅度等提出修改意见。
    """
    def run(self, article_draft: str) -> str:
        print("      - [ReviewAgent] 正在对整篇文章进行评论...")
        prompt = [
            {"role": "system", "content": "你是一位资深的新闻总编，眼光挑剔。请对以下**整篇新闻稿**进行评论，从整体结构、逻辑流、段落衔接、文笔风格和信息传达的准确性等方面提出具体的、可操作的修改意见。如果文章已经足够优秀，无需修改，请只回答'无需修改'。"},
            {"role": "user", "content": f"待评论文章：\n{article_draft}\n\n请给出你的修改意见。"}
        ]
        feedback = self._create_chat_completion(prompt)
        if "无需修改" in feedback:
            print("      - [ReviewAgent] 结果: 无需修改。")
            return "无需修改"
        else:
            print(f"      - [ReviewAgent] 结果: 提出修改意见 - {feedback}")
            return feedback