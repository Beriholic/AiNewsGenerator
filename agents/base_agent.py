from zhipuai import ZhipuAI
import config

class BaseAgent:
    """
    所有 Agent 的基类，负责初始化 ZhipuAI 客户端和提供通用的聊天完成方法。
    """
    def __init__(self, model: str = config.ZHIPU_MODEL, temperature: float = 0.7):
        self.client = ZhipuAI(api_key=config.ZHIPU_API_KEY)
        self.model = model
        self.temperature = temperature

    def _create_chat_completion(self, messages: list[dict]) -> str:
        """
        调用 Zhipu AI 的 chat completion 接口。

        Args:
            messages: 发送给模型的消息列表。

        Returns:
            模型生成的回复内容。
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"调用AI模型时出错: {e}")
            return f"AI模型调用失败: {e}"