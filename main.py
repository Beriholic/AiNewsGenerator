from orchestrator import NewsOrchestrator
import config

def main():
    # 加载配置
    config.load()

    # 用户输入话题
    topic = input("请输入您想生成新闻稿的话题: ")
    
    # 创建并运行协调器
    orchestrator = NewsOrchestrator(topic=topic)
    orchestrator.run()

if __name__ == "__main__":
    main()