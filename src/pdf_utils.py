"""
pdf_utils.py
------------
PDF 分段與處理工具。

主要功能：
- split_pdf_to_chunks(pdf_path): 將大型 PDF 分段為可管理的文字區塊。

設計考量：
- 支援超大 PDF，逐頁讀取，避免記憶體爆炸。
- 可調整每個 chunk 的最大字數。
- 回傳格式：List[dict]，每個 dict 包含 'text', 'page', 'chunk_id'。
"""

import pdfplumber
from typing import List, Dict

CHUNK_SIZE = 1000  # 每個 chunk 最多字元數，可依需求調整


def split_pdf_to_chunks(pdf_path: str, chunk_size: int = CHUNK_SIZE) -> List[Dict]:
    """
    將 PDF 逐頁分段為多個 chunk，避免一次載入整份大檔。
    參數：
        pdf_path: PDF 檔案路徑
        chunk_size: 每個 chunk 最大字元數
    回傳：
        List[dict]，每個 dict 包含 'text', 'page', 'chunk_id'
    """
    chunks = []
    chunk_id = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ""
            # 依 chunk_size 切分
            for i in range(0, len(text), chunk_size):
                chunk_text = text[i:i+chunk_size]
                if chunk_text.strip():
                    chunks.append({
                        'text': chunk_text,
                        'page': page_num,
                        'chunk_id': chunk_id
                    })
                    chunk_id += 1
    return chunks
