import re


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200) -> list[str]:
    """
    Split long document text into smaller chunks.
    """

    if not text or not text.strip():
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

        if start < 0:
            start = 0

        if start >= text_length:
            break

    return chunks


def clean_query(query: str) -> list[str]:
    """
    Convert user question into searchable keywords.
    """

    if not query:
        return []

    query = query.lower()
    words = re.findall(r"\b\w+\b", query)

    stop_words = {
        "the", "is", "are", "a", "an", "of", "to", "in", "on", "for",
        "and", "or", "what", "why", "how", "when", "where", "who",
        "which", "can", "you", "me", "this", "that", "from", "with",
        "by", "as", "at", "it", "be", "do", "does"
    }

    return [word for word in words if word not in stop_words]


def score_chunk(chunk: str, keywords: list[str]) -> int:
    """
    Score a chunk based on keyword matches.
    """

    if not chunk or not keywords:
        return 0

    chunk_lower = chunk.lower()
    score = 0

    for keyword in keywords:
        score += chunk_lower.count(keyword)

    return score


def get_relevant_chunks(
    document_text: str,
    query: str,
    top_k: int = 3,
    chunk_size: int = 1200,
    overlap: int = 200
) -> str:
    """
    Return the most relevant document chunks for the user's question.
    """

    chunks = chunk_text(document_text, chunk_size=chunk_size, overlap=overlap)

    if not chunks:
        return ""

    keywords = clean_query(query)

    if not keywords:
        return "\n\n".join(chunks[:top_k])

    scored_chunks = []

    for chunk in chunks:
        score = score_chunk(chunk, keywords)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    relevant_chunks = [chunk for score, chunk in scored_chunks if score > 0]

    if not relevant_chunks:
        relevant_chunks = chunks[:top_k]

    return "\n\n--- Relevant Chunk ---\n\n".join(relevant_chunks[:top_k])