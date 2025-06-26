"""
rag_pipeline.py
---------------
RAG（Retrieval-Augmented Generation）流程，負責兩份文件的語意比對與差異分析。

主要功能：
- RAGPipeline: 結合兩份 VectorStore，進行 chunk 對 chunk 的語意比對與摘要生成。

設計考量：
- 針對每個 chunk，檢索對方文件最相近內容，並用 LLM 生成差異摘要。
- 支援大檔案，分批處理。
"""

from typing import List
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class RAGPipeline:
    def __init__(self, vs1, vs2):
        """
        初始化 RAGPipeline，需傳入兩份 VectorStore。
        """
        self.vs1 = vs1
        self.vs2 = vs2
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def compare_documents(self) -> str:
        """
        針對文件1的每個 chunk，檢索文件2最相近 chunk，並用 LLM 生成差異摘要。
        回傳完整自然語言報告。
        """
        report_lines = ["# 文件比對報告\n"]
        for chunk in self.vs1.chunks:
            query = chunk['text']
            matches = self.vs2.search(query, top_k=1)
            match_text = matches[0]['text'] if matches else ""
            summary = self._summarize_diff(query, match_text)
            report_lines.append(f"[第{chunk['page']}頁 chunk {chunk['chunk_id']}]\n{summary}\n")
        return "\n".join(report_lines)

    def _summarize_diff(self, text1: str, text2: str) -> str:
        """
        使用 LLM 生成兩段文字的差異摘要。
        """
        prompt = (
            "請比較以下兩段文件內容，列出主要差異與重點：\n"
            f"文件A：{text1}\n\n文件B：{text2}\n\n請以條列式摘要。"
        )
        resp = self.llm.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=256
        )
        return resp.choices[0].message.content.strip()
