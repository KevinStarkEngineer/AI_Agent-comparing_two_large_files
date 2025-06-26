"""
test_pipeline.py
----------------
簡易測試腳本，驗證 PDF 分段、向量化與比對流程。
請將兩份小型 PDF 放於 data/ 目錄，命名為 test1.pdf, test2.pdf。
"""

import os
from src.agent import CompareAgent

def test_compare_agent():
    file1 = os.path.join("data", "test1.pdf")
    file2 = os.path.join("data", "test2.pdf")
    agent = CompareAgent(file1, file2)
    report = agent.compare_and_analyze()
    assert isinstance(report, str)
    assert "文件比對報告" in report
    print("[測試通過] 比對報告產生成功！")

if __name__ == "__main__":
    test_compare_agent() 