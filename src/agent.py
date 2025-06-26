"""
CompareAgent
-------------
AI Agent 主體，負責協調 PDF 分段、向量化、RAG 比對與報告生成。

初始化參數：
- file1_path: str，第一份 PDF 檔案路徑
- file2_path: str，第二份 PDF 檔案路徑

主要方法：
- compare_and_analyze(): 執行比對與分析，回傳自然語言報告

假設：
- PDF 檔案可能非常大，需分段處理
- 依賴 pdf_utils, vector_store, rag_pipeline
"""

from .pdf_utils import split_pdf_to_chunks
from .vector_store import VectorStore
from .rag_pipeline import RAGPipeline

class CompareAgent:
    def __init__(self, file1_path: str, file2_path: str):
        """
        初始化 CompareAgent，準備兩份文件的分段與向量化。
        """
        self.file1_path = file1_path
        self.file2_path = file2_path
        # 將 PDF 分段
        self.chunks1 = split_pdf_to_chunks(file1_path)
        self.chunks2 = split_pdf_to_chunks(file2_path)
        # 建立向量資料庫
        self.vs1 = VectorStore(self.chunks1)
        self.vs2 = VectorStore(self.chunks2)
        # 初始化 RAG Pipeline
        self.rag = RAGPipeline(self.vs1, self.vs2)

    def compare_and_analyze(self) -> str:
        """
        執行兩份文件的比對與分析，回傳自然語言報告。
        """
        # 進行語意比對與差異分析
        report = self.rag.compare_documents()
        return report
