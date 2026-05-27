from services.openai_service import call_openai


def generate_quiz(document_text: str) -> str:
    """
    Generate quiz questions from uploaded PDF content.
    """

    prompt = f"""
You are DocuAgent, a helpful AI quiz generator.

Create 5 quiz questions from the document below.

For each question, include:
- Question
- 4 answer options
- Correct answer
- Short explanation

Document Content:
{document_text}
"""

    return call_openai(prompt, max_tokens=1500)