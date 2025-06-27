from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from src.summarization.summarizer import summarize_text
from src.logger import logging
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

class TextInput(BaseModel):
    text: str
    
@app.get("/", response_class=HTMLResponse)
async def home():
    if os.path.exists("static/index.html"):
        return open("static/index.html").read()
    return "<h1>AI-Powered Text Summarization Microservice</h1>"

@app.post("/summarizer")
async def summarize(input: TextInput):
    text = input.text.strip()
    logging.info(f"Request received: text_length={len(text)}")

    if not text:
        logging.error("Empty input text")
        raise HTTPException(status_code=400, detail="Text input is required.")



    try:
        summary = summarize_text(text)
        logging.info("summarization successfully ")
        return {"summary": summary}
    except Exception as e:
        logging.exception("Summarization failed")
        
        return {"summary": "Summary not available."}
