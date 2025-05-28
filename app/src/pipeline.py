import os
from dask import delayed, compute
from src.pdf_text_extractor import extract_text_from_pdf
from src.chunker import chunk_text
from src.summarizer import summarize_text
from tqdm import tqdm

INPUT_FOLDER = "pdfs/input"
OUTPUT_FOLDER = "pdfs/output"

def process_single_pdf(pdf_path: str):
    file_name = os.path.basename(pdf_path)
    base_name = os.path.splitext(file_name)[0]
    summary_file_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_summary.txt")

    if os.path.exists(summary_file_path):
        print(f"Summary already exists for {file_name}, skipping.")
        return

    text = extract_text_from_pdf(pdf_path)
    if len(text.strip()) == 0:
        print(f"No text found in {file_name}. Skipping.")
        return

    chunks = chunk_text(text, max_words=1000, filename=file_name)

    delayed_summaries = []
    for i, chunk in enumerate(chunks):
        print(f"[{file_name}] Summarising chunk {i + 1}/{len(chunks)}")
        delayed_summary = delayed(summarize_text)(chunk, filename=f"{file_name}_chunk{i + 1}")
        delayed_summaries.append(delayed_summary)

    chunk_summaries = compute(*delayed_summaries)

    print(f"[{file_name}] Summarising all chunks")
    combined_text = " ".join(chunk_summaries)
    final_summary = summarize_text(combined_text, filename=f"{file_name}_final_summary", max_length=250, min_length=80)

    with open(summary_file_path, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print(f"[{file_name}] Summary saved to {summary_file_path}")
    print(f"[{file_name}] Summarised done\n")

def run_all():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_files = [os.path.join(INPUT_FOLDER, f) for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

    for pdf_path in tqdm(pdf_files):
        process_single_pdf(pdf_path)

if __name__ == "__main__":
    run_all()

