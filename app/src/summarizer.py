import os
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

MODEL_DIR = "/home/sahito/models/bart-large-cnn"

print("** Loading summarization model **")
tokenizer = BartTokenizer.from_pretrained(MODEL_DIR)
model = BartForConditionalGeneration.from_pretrained(MODEL_DIR)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
print(f"Model loaded. Device set to {device}\n")

MAX_TOKEN_LENGTH = 1024

def summarize_text(text: str, filename="unknown.txt", max_length=150, min_length=30) -> str:
    print(f"\n** [{filename}] Summarization chunk **")
    print(f"[{filename}] Chunk text length: {len(text)} characters")

    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=MAX_TOKEN_LENGTH)
    inputs = inputs.to(device)

    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print(f"[{filename}] chunk summary done")
    return summary

