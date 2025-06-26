# AI Agent：大型文件比較與分析服務

## 專案簡介
本專案是一個基於 Python 的 AI Agent，專為比較與分析兩份大型 PDF 文件而設計。Agent 採用 RAG（Retrieval-Augmented Generation）架構，能夠處理無法一次載入記憶體的超大 PDF，並提供高效、智能的內容比對與摘要分析服務。

## 專案概述
本系統利用分段檢索與語意分析技術，將大型 PDF 文件切分為可管理的區塊，並透過向量資料庫進行檢索。AI Agent 會針對兩份文件進行內容比對、差異分析、重點摘要，並以自然語言生成報告。適合用於法規、合約、技術文件等大檔案的自動化比對。

## 主要功能
- 支援超大 PDF 文件分段處理與內容擷取
- 兩份文件的語意比對、差異分析與摘要
- RAG 架構：結合檢索與生成，提升比對準確度
- 小型文件庫建置（可自訂文件）
- 結果以自然語言輸出，便於理解與後續應用

## 技術棧
- **程式語言**：Python 3.10+
- **PDF 處理**：PyPDF2、pdfplumber
- **向量資料庫**：FAISS
- **語言模型**：OpenAI GPT-3.5/4 API（可替換為本地 LLM）
- **檢索增強生成（RAG）**：自訂 Pipeline
- **文件分段**：NLTK、tiktoken
- **依賴管理**：requirements.txt

## 安裝與設定說明

1. **安裝依賴套件**
   ```bash
   pip install -r requirements.txt
   ```

2. **準備文件庫**
   - 將欲比較的 PDF 文件放入 `data/` 目錄（預設已附上範例 PDF）。

3. **設定 OpenAI API 金鑰**
   - 將 API 金鑰寫入 `.env` 檔案：
     ```
     OPENAI_API_KEY=你的API金鑰
     ```

4. **啟動服務**
   ```bash
   python main.py
   ```

## 使用範例

1. 將兩份 PDF 文件放入 `data/` 目錄，命名為 `file1.pdf` 與 `file2.pdf`。
2. 執行主程式，依照指示輸入檔名。
3. 系統將自動分段、建立向量索引，並進行比對與分析。
4. 結果將輸出於終端機或 `output/` 目錄下的報告檔。

## 目錄結構
```
AI_Agent-comparing_two_large_files/
│
├── data/                # 文件庫（放置 PDF 檔案）
├── output/              # 分析報告輸出
├── src/                 # 主要程式碼
│   ├── agent.py         # AI Agent 主體
│   ├── pdf_utils.py     # PDF 分段與處理工具
│   ├── rag_pipeline.py  # RAG 檢索與生成流程
│   └── vector_store.py  # 向量資料庫管理
├── requirements.txt     # 依賴套件清單
├── .env                 # API 金鑰設定
└── main.py              # 執行入口
```

## 貢獻指南
歡迎提交 PR 或 issue，協助功能優化與錯誤修正。

## 授權條款
本專案採用 MIT License。

This project is licensed under the [MIT License](./LICENSE).

---

## 最新變更
**2025-06-27**
- 專案初始化，完成基本 RAG 架構與 PDF 分段比對功能
- 新增範例 PDF 文件與測試流程

---

如需更多協助，請參閱 `src/` 內各模組註解或聯絡專案維護者。 