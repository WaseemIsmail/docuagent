from mcp.server.fastmcp import FastMCP

from tools.qa_tool import answer_question
from tools.summarize_tool import summarize_document
from tools.quiz_tool import generate_quiz

mcp = FastMCP("DocuAgent MCP Server")


@mcp.tool()
def summarize_document_tool(document_text: str) -> str:
    """
    Summarize uploaded lecture slide or PDF content.

    Args:
        document_text: Extracted text from a PDF or lecture slide.
    """

    if not document_text or not document_text.strip():
        return "No document content provided."

    return summarize_document(document_text)


@mcp.tool()
def answer_question_tool(document_text: str, question: str) -> str:
    """
    Answer a question using uploaded document content.

    Args:
        document_text: Extracted text from the document.
        question: User question.
    """

    if not document_text or not document_text.strip():
        return "No document content provided."

    if not question or not question.strip():
        return "No question provided."

    return answer_question(document_text, question)


@mcp.tool()
def generate_quiz_tool(document_text: str) -> str:
    """
    Generate quiz questions from uploaded document content.

    Args:
        document_text: Extracted text from a PDF or lecture slide.
    """

    if not document_text or not document_text.strip():
        return "No document content provided."

    return generate_quiz(document_text)


if __name__ == "__main__":
    mcp.run(transport="stdio")