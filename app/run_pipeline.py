import os
from dask import delayed, compute
from src.pdf_text_extractor import extract_text_from_pdf
from src.chunker import chunk_text
from src.summarizer import summarize_text

INPUT_FOLDER = "pdfs/input"
OUTPUT_FOLDER = "pdfs/output"

def run_pipeline():
    # Ask user for summary length
    try:
        max_length = int(input("Enter the maximum number of words for the final summary: "))
        min_length = int(input("Enter the minimum number of words for the final summary: "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_FOLDER, pdf_file)
        try:
            print(f"\n[{pdf_file}] Starting processing...")
            text = extract_text_from_pdf(pdf_path)
            chunks = chunk_text(text, filename=pdf_file)

            print(f"[{pdf_file}] Creating parallel tasks for {len(chunks)} chunks...")

            # Parallelize chunk summarization
            delayed_tasks = [
                delayed(summarize_text)(chunk, filename=f"{pdf_file}_chunk{i + 1}")
                for i, chunk in enumerate(chunks)
            ]

            chunk_summaries = compute(*delayed_tasks)

            print(f"[{pdf_file}] All chunks summarized. Creating final summary...")
            combined_text = " ".join(chunk_summaries)
            final_summary = summarize_text(
                combined_text, filename=f"{pdf_file}_final_summary",
                max_length=max_length, min_length=min_length
            )

            output_path = os.path.join(OUTPUT_FOLDER, pdf_file.replace(".pdf", "_summary.txt"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(final_summary)

            print(f"[{pdf_file}] Summary saved to {output_path}")
            print(f"[{pdf_file}] Summarised done\n")

        except Exception as e:
            print(f"[{pdf_file}] Error: {e}")

if __name__ == "__main__":
    run_pipeline()

