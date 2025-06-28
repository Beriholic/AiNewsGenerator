from .base_agent import BaseAgent

class FactCheckAgent(BaseAgent):
    """
    校对 Agent：校对整篇文章的事实性。
    """
    def run(self, article_draft: str, search_results: str) -> tuple[bool, str]:
        print("      - [FactCheckAgent] 正在对整篇文章进行事实校对...")
        prompt = [
            {"role": "system", "content": "你是一名严谨的事实核查员。请仔细比对以下**整篇新闻稿**和参考资料，判断稿件中是否存在与资料不符的事实性错误。如果内容与资料一致或资料中未提及，则视为通过。如果存在明确的不符之处，请指出。"},
            {"role": "user", "content": f"待核查文章：\n{article_draft}\n\n参考资料：\n{search_results}\n\n请进行判断。如果事实一致，请只回答'事实一致'。如果不一致，请指出不符之处并提供修改建议。"}
        ]
        response = self._create_chat_completion(prompt)
        if "事实一致" in response:
            print("      - [FactCheckAgent] 结果: 事实一致。")
            return True, "事实一致"
        else:
            print(f"      - [FactCheckAgent] 结果: 发现事实不符 - {response}")
            return False, response