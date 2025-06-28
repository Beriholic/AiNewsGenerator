class MarkdownAssemblyAgent:
    """
    Markdown 组装 Agent：将标题和所有段落拼接成一个完整的 Markdown 文本。
    """
    def run(self, headline: str, final_article_text: str) -> str:
        """
        将标题和文章正文组装成一个 Markdown 字符串。

        Args:
            headline: 文章标题。
            final_article_text: 最终确定的文章正文。

        Returns:
            完整的 Markdown 格式的文章字符串。
        """
        print("  [MarkdownAssemblyAgent] 正在组装最终的 Markdown 文本...")
        
        # 拼接文章
        full_markdown = f"# {headline}\n\n{final_article_text}"
        
        print("  [MarkdownAssemblyAgent] Markdown 文本组装完成。")
        return full_markdown