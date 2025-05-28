def chunk_text(text: str, max_words: int = 1000, filename: str = "unknown.txt") -> list[str]:
    words = text.split()
    chunks = []
    total_chunks = (len(words) + max_words - 1) // max_words
    print(f"[{filename}] Chunks created: {total_chunks}")

    for i in range(0, len(words), max_words):
        chunk_index = i // max_words + 1
        print(f"[{filename}] Preparing chunk {chunk_index}/{total_chunks}")
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks

