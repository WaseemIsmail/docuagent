# DocuAgent

DocuAgent is a small OpenAI-powered PDF assistant that allows users to upload lecture slides or PDF documents and interact with the content using AI.

## Features

- Upload PDF documents
- Extract text from PDF files
- Ask questions from uploaded content
- Generate document summaries
- Generate quiz questions
- Simple agent-style tool routing
- Basic MCP server exposing document tools

## Tech Stack

- Python
- Streamlit
- OpenAI API
- OpenAI Python SDK
- pypdf
- MCP Python SDK

## Folder Structure

```text
docuagent/
│
├── app.py
├── mcp_server.py
├── requirements.txt
├── .env.example
├── .env
├── README.md
│
├── services/
│   ├── pdf_service.py
│   ├── openai_service.py
│   ├── vector_service.py
│   └── agent_service.py
│
└── tools/
    ├── summarize_tool.py
    ├── qa_tool.py
    └── quiz_tool.py
```

## How to Run

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

Copy `.env.example` and rename it to `.env`.

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### 5. Run Streamlit app

```bash
streamlit run app.py
```

### 6. Run MCP server

```bash
python mcp_server.py
```

## Project Purpose

This project demonstrates hands-on experience with LLM application development, OpenAI API integration, document-based question answering, simple agentic workflows, prompt engineering, and basic MCP tool server implementation.