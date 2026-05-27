from pypdf import PdfReader


def extract_pdf_text(uploaded_file) -> str:
    """
    Extract text from an uploaded PDF file.
    """

    try:
        reader = PdfReader(uploaded_file)
        extracted_text = ""

        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text()

            if page_text:
                extracted_text += f"\n\n--- Page {page_number} ---\n"
                extracted_text += page_text

        return extracted_text.strip()

    except Exception as e:
        raise Exception(f"Failed to extract text from PDF: {str(e)}")


def limit_text(text: str, max_chars: int = 18000) -> str:
    """
    Limit document text before sending it to the LLM.
    """

    if not text:
        return ""

    if len(text) > max_chars:
        return text[:max_chars]

    return text


def validate_pdf_text(text: str) -> bool:
    """
    Check whether extracted PDF text is usable.
    """

    return bool(text and text.strip())