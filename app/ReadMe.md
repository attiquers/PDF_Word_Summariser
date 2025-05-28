# 📄 PDF Summarization Pipeline (CPU-Based)

This project is a CPU-optimized local pipeline that takes PDF files, extracts text, summarizes the content in chunks (if large), and generates both individual and combined summary files.

---

## 📁 Folder Structure

project/
├── pdfs/
│ ├── input/ # Place PDFs here
│ └── output/ # Summaries will be saved here
├── src/
│ ├── pdf_text_extractor.py
│ ├── chunker.py
│ ├── summarizer.py
│ ├── pipeline.py
│ └── utils.py
├── run_pipeline.py
├── requirements.txt
└── README.md


---

## 🚀 Features

- ✅ Extracts text from PDFs (using `PyMuPDF`)
- ✅ Splits large documents into manageable chunks
- ✅ Summarizes each chunk using Hugging Face Transformers (`distilbart-cnn-12-6`)
- ✅ Combines chunk summaries into one final file
- ✅ Optionally generates a meta-summary across all summaries
- ✅ Parallelized using `Dask` for fast CPU-only performance

---

## 🛠️ Setup

### 1. Create and activate a virtual environment

python -m venv venv
PS X:\Studies\PDC\project - 2\app> .\venv\Scripts\Activate.ps1

pip install -r requirements.txt

run: python run_pipeline.py