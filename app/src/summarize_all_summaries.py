import os
from src.summarizer import summarize_text

OUTPUT_FOLDER = "pdfs/output"

def summarize_all_summaries():
    summary_files = [os.path.join(OUTPUT_FOLDER, f) for f in os.listdir(OUTPUT_FOLDER) if f.endswith("_summary.txt")]
    all_summaries = []

    print(f"[mega_summary] Found {len(summary_files)} summary files to combine.")

    for sf in summary_files:
        print(f"[mega_summary] Adding summary from {sf}")
        with open(sf, "r", encoding="utf-8") as f:
            all_summaries.append(f.read())

    combined = " ".join(all_summaries)
    print("[mega_summary] Summarising all chunks:")
    mega_summary = summarize_text(combined, filename="mega_summary.txt", max_length=300, min_length=100)

    with open(os.path.join(OUTPUT_FOLDER, "mega_summary.txt"), "w", encoding="utf-8") as f:
        f.write(mega_summary)

    print("[mega_summary.txt] summary completed.")

