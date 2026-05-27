import streamlit as st

from services.pdf_service import extract_pdf_text, limit_text, validate_pdf_text
from services.agent_service import run_agent
from tools.summarize_tool import summarize_document
from tools.quiz_tool import generate_quiz


st.set_page_config(
    page_title="DocuAgent",
    page_icon="📄",
    layout="centered"
)

st.title("📄 DocuAgent")
st.write("OpenAI-powered PDF assistant for lecture slides and study materials.")

if "document_text" not in st.session_state:
    st.session_state.document_text = ""

if "file_name" not in st.session_state:
    st.session_state.file_name = ""

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading PDF..."):
        extracted_text = extract_pdf_text(uploaded_file)
        extracted_text = limit_text(extracted_text)

    if not validate_pdf_text(extracted_text):
        st.error("No readable text found in this PDF.")
    else:
        st.session_state.document_text = extracted_text
        st.session_state.file_name = uploaded_file.name
        st.success(f"PDF uploaded successfully: {uploaded_file.name}")

if st.session_state.document_text:
    st.divider()

    st.subheader("Choose an action")

    action = st.selectbox(
        "Action",
        [
            "Ask DocuAgent",
            "Generate Summary",
            "Generate Quiz"
        ]
    )

    if action == "Ask DocuAgent":
        user_question = st.text_input(
            "Ask a question or give an instruction",
            placeholder="Example: Summarize this document or explain the main topic"
        )

        if st.button("Ask"):
            if not user_question.strip():
                st.warning("Please enter a question or instruction.")
            else:
                with st.spinner("DocuAgent is thinking..."):
                    result = run_agent(st.session_state.document_text, user_question)

                st.subheader("Response")
                st.write(result)

    elif action == "Generate Summary":
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                result = summarize_document(st.session_state.document_text)

            st.subheader("Summary")
            st.write(result)

    elif action == "Generate Quiz":
        if st.button("Generate Quiz"):
            with st.spinner("Generating quiz..."):
                result = generate_quiz(st.session_state.document_text)

            st.subheader("Quiz")
            st.write(result)

    with st.expander("View extracted text preview"):
        st.text(st.session_state.document_text[:3000])

else:
    st.info("Upload a PDF to start.")