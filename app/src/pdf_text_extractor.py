import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    print(f"[{pdf_path}] Extracting text from PDF...")
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    print(f"[{pdf_path}] Text extraction completed.")
    return text

