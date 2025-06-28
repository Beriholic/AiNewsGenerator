import requests
import json
import config

def search_serper(query: str, num_results: int = 5) -> str:
    """
    使用 Serper API 进行网络搜索。
    
    Args:
        query: 搜索查询字符串。
        num_results: 需要返回的结果数量。

    Returns:
        格式化后的搜索结果字符串。
    """
    print(f"  - 正在搜索: {query}")
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query,
        "num": num_results
    })
    headers = {
        'X-API-KEY': config.SERPER_API_KEY,
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # 如果请求失败则抛出异常
        results = response.json()

        # 格式化输出，只取有价值的部分
        formatted_results = []
        if 'organic' in results:
            for item in results['organic'][:num_results]:
                formatted_results.append(
                    f"标题: {item.get('title', 'N/A')}\n"
                    f"链接: {item.get('link', 'N/A')}\n"
                    f"摘要: {item.get('snippet', 'N/A')}\n"
                )
        if not formatted_results:
            return "没有找到相关的搜索结果。"
            
        return "-----------------\n".join(formatted_results)
    
    except requests.exceptions.RequestException as e:
        print(f"  - 搜索失败: {e}")
        return f"搜索请求失败: {e}"
