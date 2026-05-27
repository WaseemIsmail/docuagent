from services.openai_service import call_openai
from services.vector_service import get_relevant_chunks


def answer_question(document_text: str, question: str) -> str:
    """
    Answer a question using relevant PDF content.
    """

    relevant_context = get_relevant_chunks(document_text, question)

    prompt = f"""
You are DocuAgent, a helpful AI assistant.

Use only the relevant document content below to answer the user's question.
If the answer is not available in the document content, say:
"I couldn't find that information in the uploaded document."

Relevant Document Content:
{relevant_context}

User Question:
{question}

Give a clear, simple, and useful answer.
"""

    return call_openai(prompt)