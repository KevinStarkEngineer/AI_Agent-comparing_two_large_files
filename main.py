# main.py
# 專案主程式入口，負責載入 PDF、初始化 AI Agent、執行比對與輸出結果。
# 執行流程：
# 1. 載入 PDF 檔案
# 2. 初始化向量資料庫與 RAG Pipeline
# 3. 執行文件比對與分析
# 4. 輸出結果

import os
from src.agent import CompareAgent
from rich import print

def main():
    print("[bold green]AI Agent 大型文件比對服務 啟動中...[/bold green]")
    file1 = input("請輸入第一份 PDF 檔案名稱（放於 data/ 目錄）: ")
    file2 = input("請輸入第二份 PDF 檔案名稱（放於 data/ 目錄）: ")
    path1 = os.path.join("data", file1)
    path2 = os.path.join("data", file2)
    if not os.path.exists(path1) or not os.path.exists(path2):
        print(f"[red]找不到檔案：{file1} 或 {file2}，請確認檔案已放入 data/ 目錄。[/red]")
        return
    agent = CompareAgent(path1, path2)
    report = agent.compare_and_analyze()
    output_path = os.path.join("output", f"compare_{file1}_vs_{file2}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[bold blue]比對報告已輸出至 {output_path}[/bold blue]")

if __name__ == "__main__":
    main()
