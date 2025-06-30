import config
from agents import (
    InfoAgent, HeadlineAgent, OutlineAgent, ParagraphAgent,
    FactCheckAgent, EnhanceFormatAgent, ReviewAgent, MarkdownAssemblyAgent,
    HTMLAgent
)
import webbrowser
import os

class NewsOrchestrator:
    def __init__(self, topic: str):
        self.topic = topic
        self.search_results = ""
        self.headline = ""
        self.outline = []
        self.final_article = ""

        # 初始化所有 agents
        self.info_agent = InfoAgent()
        self.headline_agent = HeadlineAgent()
        self.outline_agent = OutlineAgent()
        self.paragraph_agent = ParagraphAgent()
        self.fact_check_agent = FactCheckAgent()
        self.enhance_format_agent = EnhanceFormatAgent()
        self.review_agent = ReviewAgent()
        self.markdown_assembly_agent = MarkdownAssemblyAgent()
        self.html_agent = HTMLAgent()

    def run(self):
        """
        执行完整的新闻稿生成流程，最终输出 HTML 文件，并询问是否打开。
        """
        # --- 步骤 1: 信息收集中 ---
        print("--- 步骤 1: 信息收集中 ---")
        self.search_results = self.info_agent.run(self.topic)

        # --- 步骤 2: 标题制定中 ---
        print("\n--- 步骤 2: 标题制定中 ---")
        self.headline = self.headline_agent.run(self.topic, self.search_results)

        # --- 步骤 3: 大纲生成中 ---
        print("\n--- 步骤 3: 大纲生成中 ---")
        self.outline = self.outline_agent.run(self.headline, self.search_results)

        # --- 步骤 4: 撰写文章初稿 ---
        print("\n--- 步骤 4: 撰写文章初稿 ---")
        current_draft = self.paragraph_agent.write_initial_draft(
            self.headline, self.outline, self.search_results
        )
        print("    - 初稿撰写完成。")

        # --- 步骤 5: 文章修订循环 ---
        print("\n--- 步骤 5: 文章修订循环 ---")
        revision_cycles = 0
        while revision_cycles < config.MAX_REVIEW_CYCLES:
            print(f"\n--- 开始第 {revision_cycles + 1} 轮修订 ---")
            
            is_fact_valid, fact_feedback = self.fact_check_agent.run(current_draft, self.search_results)
            if not is_fact_valid:
                print("    - 事实校对未通过，要求修订...")
                current_draft = self.paragraph_agent.revise_draft(current_draft, fact_feedback)
                revision_cycles += 1
                continue

            review_feedback = self.review_agent.run(current_draft)
            if "无需修改" in review_feedback:
                print("    - 评论审查通过，文章最终确定！")
                self.final_article = current_draft
                break
            
            print("    - 收到评论意见，要求修订...")
            current_draft = self.paragraph_agent.revise_draft(current_draft, review_feedback)


            revision_cycles += 1
        
        if not self.final_article:
            print(f"    - 已达到最大修订次数 ({config.MAX_REVIEW_CYCLES})，接受当前最终版本。")
            print("    - 格式增强中...")
            current_draft = self.enhance_format_agent.run(current_draft)
            self.final_article = current_draft

        # --- 步骤 6: 组装最终 Markdown 文本 ---
        print("\n--- 步骤 6: 组装 Markdown 文本 ---")
        final_markdown = self.markdown_assembly_agent.run(
            self.headline, self.final_article
        )

        # --- 步骤 7: 转换为 HTML 并保存 ---
        print("\n--- 步骤 7: 转换为 HTML 并保存 ---")
        html_filepath = self.html_agent.run(final_markdown, self.topic)
        
        # --- 步骤 8: 最终输出并询问是否打开 --- (这是修改的部分)
        print("\n\n==================== 新闻稿生成完毕 ====================")
        print(f"最终的 HTML 文件已保存在: {html_filepath}")
        print("==========================================================")

        try:
            user_choice = input("是否立即在浏览器中打开? (y/n): ")
            if user_choice.strip().lower() == 'y':
                # 获取文件的绝对路径并格式化为 file URI
                absolute_path = os.path.abspath(html_filepath)
                # webbrowser.open() 在大多数情况下可以直接处理路径，但使用 'file://' 更为稳妥
                webbrowser.open(f'file://{absolute_path}')
                print(f"已请求浏览器打开文件。")
            else:
                print("好的，请手动打开文件查看。")
        except Exception as e:
            print(f"尝试自动打开浏览器时发生错误: {e}")
            print("请手动打开文件查看。")

        print("程序执行完毕。")
        
        return html_filepath
