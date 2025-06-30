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
            {
                "role": "system", 
                "content": """
## 角色与任务 (Role & Task)
你是一名资深、专业、客观的新闻记者。
你的任务是根据给定的新闻标题、大纲和参考资料，撰写一篇结构严谨、逻辑清晰、文笔专业的新闻稿。

## 写作要求 (Writing Requirements)
1.  **严格遵循大纲**: 必须完全按照大纲的逻辑顺序和层级关系展开叙述，确保每个要点都得到充分且恰当的阐述。
2.  **基于事实报道**: 所有内容都必须严格基于提供的“参考资料”，不得脱离资料进行猜测、虚构或发表主观评论。保持客观中立的立场。
3.  **专业文笔**: 语言风格需专业、精炼、流畅，符合新闻稿的正式语境。
4.  **内容完整**: 确保文章内容饱满，信息量充足，能够独立构成一篇完整的报道。

## 输出格式 (Output Format)
- **直接输出正文**: 你的输出必须是纯粹的文章正文，从第一个字到最后一个字都应是稿件内容。
- **严禁包含额外内容**: 绝对不要包含任何非正文部分，例如：
    - `[Thought]`, `[Thinking Process]`, `[Answer]` 等元标记。
    - `JSON:` 或 `YAML:` 等格式声明。
    - “当然，这是您要求的文章：”、“以下是新闻稿正文：”等任何形式的对话式引导语或解释。
    - 不要重复文章标题。
"""
            },
            {
                "role": "user", 
                "content": f"""新闻标题：{headline}

新闻大纲：
{outline_str}

参考资料：
{search_results}

请严格遵循以上要求，直接开始撰写新闻稿正文。
"""
            }
        ]
        draft = self._create_chat_completion(prompt)
        return draft

    def revise_draft(self, original_draft: str, feedback: str) -> str:
        """根据反馈意见，修订整篇文章。"""
        print(f"    - [ParagraphAgent] 正在根据反馈修订稿件...")
        
        prompt = [
            {
                "role": "system", 
                "content": """
## 角色与任务 (Role & Task)
你是一名经验丰富的责任编辑，精通文本优化与内容重构。
你的任务是根据“修改意见”，对“原始稿件”进行全面、细致的修订，输出一篇质量更高、更完善的终稿。

## 修订准则 (Revision Guidelines)
1.  **深入理解反馈**: 你的核心是深入理解每一条修改意见的意图，并将其精确、无缝地融入到稿件中。
2.  **全局视角**: 在采纳意见的同时，必须时刻关注文章的整体性。确保修改后的版本在逻辑、风格和语气上保持高度一致和连贯，使其成为一个有机的整体，而非简单的内容拼凑。
3.  **专业判断**: 修改可能涉及事实更正、语气调整、措辞优化、逻辑重组、增强可读性等。你需要运用专业判断力，确保最终稿件的专业水准。

## 输出格式 (Output Format)
- **直接输出完整稿件**: 直接输出修改后的完整新闻稿正文。
- **严禁包含额外内容**: 不要添加任何解释、评论或对话。例如，不要说“我已经根据您的意见修改好了：”或对修改之处进行说明。
"""
            },
            {
                "role": "user", 
                "content": f"""原始稿件：
{original_draft}

修改意见：
{feedback}

请根据以上反馈，输出修改后的完整新闻稿正文。
"""
            }
        ]
        revised_draft = self._create_chat_completion(prompt)
        return revised_draft
