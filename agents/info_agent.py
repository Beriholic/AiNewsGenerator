from .base_agent import BaseAgent
from tools.search import search_serper

class InfoAgent(BaseAgent):
    """
    信息收集 Agent：根据话题拆分关键字并搜索资料。
    """
    def run(self, topic: str) -> str:
        print("  [InfoAgent] 正在运行...")
        # 1. 生成搜索关键字
        keywords_prompt = [
            {"role": "system", "content": "你是一个信息检索专家。你的任务是根据用户给出的新闻话题，提炼出3-5个最核心、最有效的搜索关键词，并用逗号分隔。"},
            {"role": "user", "content": f"新闻话题：{topic}"}
        ]
        keywords_str = self._create_chat_completion(keywords_prompt)
        keywords = [k.strip() for k in keywords_str.split(',')]
        print(f"  - 生成的关键词: {keywords}")

        # 2. 搜索资料
        all_search_results = []
        for keyword in keywords:
            search_result = search_serper(keyword)
            all_search_results.append(f"--- 关于 '{keyword}' 的搜索结果 ---\n{search_result}")

        # 3. 整合资料
        combined_results = "\n\n".join(all_search_results)
        print("  [InfoAgent] 资料收集完成。")
        return combined_results