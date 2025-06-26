import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("summarizer")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"

def summarize_text(text: str) -> str:
    try:
        if len(text.split()) < 10:
            return "Text too short to summarize."

        prompt = f"Please summarize the following text and make sure the summary i seasy to understand :\n\n{text}"
        response = model.generate_content(prompt)

        return response.text.strip()
    except Exception as e:
        logger.error(f"Summarization failed: {e}")
        return "Summary not available."
