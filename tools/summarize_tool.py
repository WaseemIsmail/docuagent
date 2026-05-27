from services.openai_service import call_openai


def summarize_document(document_text: str) -> str:
    """
    Summarize uploaded PDF content.
    """

    prompt = f"""
You are DocuAgent, a helpful AI study assistant.

Summarize the document below in a simple and student-friendly way.

Include:
1. Main topic
2. Key points
3. Important definitions
4. Simple final summary

Document Content:
{document_text}
"""

    return call_openai(prompt, max_tokens=1500)