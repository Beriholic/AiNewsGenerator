import markdown2
import datetime
import os
import config
import re

class HTMLAgent:
    """
    HTML Agent: 将 Markdown 文本转换为带有美观 CSS 样式的 HTML 文件。
    """
    def _get_default_css(self):
        """返回一个预设的、用于美化文章的 CSS 样式字符串。"""
        return """
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f8f9fa;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1, h2, h3, h4, h5, h6 {
                color: #212529;
                font-weight: 600;
                margin-top: 1.5em;
                margin-bottom: 0.8em;
            }
            h1 {
                font-size: 2.5em;
                border-bottom: 2px solid #dee2e6;
                padding-bottom: 0.3em;
            }
            h2 {
                font-size: 2em;
                border-bottom: 1px solid #dee2e6;
                padding-bottom: 0.3em;
            }
            p {
                margin-bottom: 1.2em;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            code {
                background-color: #e9ecef;
                padding: 0.2em 0.4em;
                margin: 0;
                font-size: 85%;
                border-radius: 3px;
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            }
            pre {
                background-color: #212529;
                color: #f8f9fa;
                padding: 1em;
                border-radius: 5px;
                overflow-x: auto;
            }
            pre code {
                background-color: transparent;
                padding: 0;
                font-size: 100%;
            }
            blockquote {
                border-left: 4px solid #007bff;
                padding-left: 1em;
                margin-left: 0;
                color: #6c757d;
            }
        </style>
        """

    def run(self, markdown_content: str, topic: str) -> str:
        """
        执行 Markdown 到 HTML 的转换和保存。

        Args:
            markdown_content: 完整的 Markdown 格式文章。
            topic: 文章主题，用于生成文件名。

        Returns:
            保存的 HTML 文件的路径。
        """
        print("  [HTMLAgent] 正在将 Markdown 转换为带样式的 HTML...")

        # 从 Markdown 中提取 H1作为 HTML 的 title
        title_match = re.search(r'^#\s*(.*)', markdown_content, re.MULTILINE)
        html_title = title_match.group(1) if title_match else topic

        # 转换 Markdown 到 HTML 片段
        # 使用 extras 来支持 GitHub Flavored Markdown 的特性，如代码块
        html_body = markdown2.markdown(
            markdown_content, 
            extras=["fenced-code-blocks", "tables", "spoiler"]
        )

        # 组合成完整的 HTML 文档
        full_html = f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{html_title}</title>
            {self._get_default_css()}
        </head>
        <body>
            <div class="container">
                {html_body}
            </div>
        </body>
        </html>
        """

        # 保存到文件
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_topic = "".join(x for x in topic if x.isalnum())[:20]
        filename = f"{timestamp}_{safe_topic}.html"
        filepath = os.path.join(config.OUTPUT_BASE, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"  [HTMLAgent] HTML 文件已生成并保存到: {filepath}")
        return filepath