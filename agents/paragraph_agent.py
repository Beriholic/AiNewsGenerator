from .base_agent import BaseAgent

class ParagraphAgent(BaseAgent):
    """
    稿件撰写 Agent：负责撰写完整的文章初稿，并根据反馈进行修订。
    """
    def write_initial_draft(self, headline: str, outline: list[str], search_results: str) -> str:
        """根据大纲和资料，撰写完整的文章初稿。"""
        print("    - [ParagraphAgent] 正在撰写完整的文章初稿...")
        
        outline_str = "\n".join(f"- {point}" for point in outline)

        prompt = [
            {"role": "system", "content": "你是一名专业的新闻记者。你的任务是根据给定的新闻标题、大纲和背景资料，撰写一篇结构完整、内容连贯、文笔流畅的新闻稿。请严格遵循大纲的结构来组织文章内容。"},
            {"role": "user", "content": f"新闻标题：{headline}\n\n新闻大纲：\n{outline_str}\n\n背景资料：\n{search_results}\n\n请根据以上信息，撰写完整的新闻稿内容（不需要重复标题）。"}
        ]
        draft = self._create_chat_completion(prompt)
        return draft

    def revise_draft(self, original_draft: str, feedback: str) -> str:
        """根据反馈意见，修订整篇文章。"""
        print(f"    - [ParagraphAgent] 正在根据反馈修订稿件...")
        prompt = [
            {"role": "system", "content": "你是一名善于听取意见并精通修改的编辑。请根据以下提供的反馈和修改意见，对整篇新闻稿进行修订。请确保在采纳意见的同时，保持文章的整体性和连贯性。"},
            {"role": "user", "content": f"原始稿件：\n{original_draft}\n\n修改意见：\n{feedback}\n\n请输出修改后的完整新闻稿。"}
        ]
        revised_draft = self._create_chat_completion(prompt)
        return revised_draft