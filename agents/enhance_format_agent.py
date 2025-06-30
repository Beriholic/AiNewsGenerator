from agents.base_agent import BaseAgent


class EnhanceFormatAgent(BaseAgent):
    """
    内容格式增强 Agent：清理由大模型意外生成的冗余内容，并优化文章的 Markdown 格式。
    """
    def run(self, article_draft: str) -> str:
        print("      - [EnhanceFormatAgent] 正在对整篇文章格式进行增强...")
        prompt = [
            {"role": "system", "content":
        """
        你是一名经验丰富的格式优化人员，，任务是接收一篇文章草稿，对文章的格进行优化

         **优化排版格式**：
            - 确保段落之间有适当的空行。
            - 使用 Markdown 语法来增强可读性，例如：
              - 为各级标题添加 `#` 号 (如 `## 二级标题`)。
              - 对需要强调的关键词使用粗体 (`**关键词**`)。

        **输出要求**：
        - **直接返回**清理和排版优化后的**完整文章内容**。
        - **不要添加**任何额外的解释、前言或结尾（例如，不要说“这是我修改后的版本”）。
        - 如果文章格式已经很完美，无需任何修改，请**只返回**四个字：“无需修改”。
        """
            },
            {"role": "user", "content": f"待处理文章：\n\n---\n\n{article_draft}\n\n---\n"}
        ]
        feedback = self._create_chat_completion(prompt)
        if "无需修改" in feedback:
            print("      - [EnhanceFormatAgent] 结果: 无需修改。")
            return article_draft 
        else:
            print(f"      - [EnhanceFormatAgent] 结果: 格式已优化。")
            return feedback
