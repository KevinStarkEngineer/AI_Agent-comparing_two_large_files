"""
vector_store.py
---------------
向量資料庫管理，負責將 chunk 向量化並儲存於 FAISS。

主要功能：
- VectorStore: 將 chunk 轉為向量並建立索引，支援相似度查詢。

設計考量：
- 使用 OpenAI Embedding API 進行向量化（可替換為本地模型）
- 支援大規模 chunk，僅儲存必要資訊
"""

import faiss
import numpy as np
from openai import OpenAI
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

class VectorStore:
    def __init__(self, chunks: List[Dict]):
        """
        初始化 VectorStore，將 chunk 轉為向量並建立 FAISS 索引。
        參數：
            chunks: List[dict]，每個 dict 包含 'text', ...
        """
        self.chunks = chunks
        self.embeddings = self._embed_chunks([c['text'] for c in chunks])
        self.index = self._build_faiss_index(self.embeddings)

    def _embed_chunks(self, texts: List[str]) -> np.ndarray:
        """
        使用 OpenAI Embedding API 將文本轉為向量。
        """
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        # OpenAI API 限制每次最多 2048 條，分批處理
        all_embeds = []
        batch_size = 100
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i+batch_size]
            resp = client.embeddings.create(
                input=batch,
                model="text-embedding-3-small"
            )
            embeds = [e.embedding for e in resp.data]
            all_embeds.extend(embeds)
        return np.array(all_embeds).astype('float32')

    def _build_faiss_index(self, embeddings: np.ndarray):
        """
        建立 FAISS 向量索引。
        """
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        return index

    def search(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        查詢與 query 最相近的 chunk，回傳 chunk dict。
        """
        q_embed = self._embed_chunks([query])
        D, I = self.index.search(q_embed, top_k)
        return [self.chunks[i] for i in I[0]]
