from tools.qa_tool import answer_question
from tools.summarize_tool import summarize_document
from tools.quiz_tool import generate_quiz


def detect_intent(user_input: str) -> str:
    """
    Detect what the user wants to do.
    """

    text = user_input.lower()

    quiz_keywords = [
        "quiz",
        "question paper",
        "mcq",
        "test me",
        "exam question",
        "generate questions"
    ]

    summary_keywords = [
        "summarize",
        "summary",
        "short note",
        "key points",
        "main points",
        "explain shortly"
    ]

    if any(keyword in text for keyword in quiz_keywords):
        return "quiz"

    if any(keyword in text for keyword in summary_keywords):
        return "summary"

    return "qa"


def run_agent(document_text: str, user_input: str) -> str:
    """
    Route the user request to the correct tool.
    """

    if not document_text or not document_text.strip():
        return "Please upload a readable PDF document first."

    if not user_input or not user_input.strip():
        return "Please enter a question or instruction."

    intent = detect_intent(user_input)

    if intent == "summary":
        return summarize_document(document_text)

    if intent == "quiz":
        return generate_quiz(document_text)

    return answer_question(document_text, user_input)