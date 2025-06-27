import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv
import sys
from src.logger import logging
from src.exception import CustomException
load_dotenv()


try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    logging.info("Gemini Api key  configured successfully.")
except Exception as e:
    logging.error(f"Failed to configure Generative AI Key: {e}")
    raise CustomException(e, sys)

try:

    model = genai.GenerativeModel("gemini-1.5-flash")  
    logging.info("Gemini model loaded succesfully ")
except Exception as e :
    logging.error(f"Failed to loaded Gemini model {e}")
    raise CustomException(e, sys)
def summarize_text(text: str) -> str:
    try:
        if len(text.split()) < 10:
            return "Text too short to summarize."

        prompt = f"Please summarize the following text and make sure the summary is easy to understand :\n\n{text}"
        response = model.generate_content(prompt)

        return response.text.strip()
    except Exception as e:
        logging.error(f"Summarization failed: {e}")
        return "Summary not available."
