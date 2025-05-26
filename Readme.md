# 📄 Local PDF Summarization Pipeline

A full-stack local pipeline to summarize PDF documents using various summarization techniques. The system includes:

- 🖥️ **React UI** for uploading files and triggering summarization
- 🐍 **Python (FastAPI)** backend for PDF processing
- ⚡ Parallel processing of documents
- 🧠 Multiple summarization methods: extractive and abstractive
- 📁 Folder-based workflow for easy file management

---

## 🔧 Backend Setup

1. **Go to backend folder:**
    ```bash
    cd app
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    
    | Endpoint            | Method | Description                        |
    | ------------------- | ------ | ---------------------------------- |
    | `/start-processing` | POST   | Triggers the summarization process |
    | `/get-summary`      | GET    | Fetches final summary results      |




python -m venv venv
.\venv\Scripts\activate.bat
-or-
.\venv\Scripts\Activate.ps1

pip install fastapi uvicorn python-multipart

uvicorn main:app --reload --host 0.0.0.0 --port 8000

