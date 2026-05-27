import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Please add it to your .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)


def call_openai(prompt: str, max_tokens: int = 1200) -> str:
    """
    Send a prompt to OpenAI and return response text.
    """

    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=prompt,
            max_output_tokens=max_tokens,
        )

        return response.output_text

    except Exception as e:
        raise Exception(f"OpenAI API request failed: {str(e)}")