from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from src.app.summarizer import summarize_text
from src.logger import logging
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(input: TextInput):
    text = input.text.strip()
    logging.info(f"Request received: text_length={len(text)}")

    if not text:
        logging.error("Empty input text")
        raise HTTPException(status_code=400, detail="Text input is required.")
    if len(text) < 20:
        logging.error("Text too short")
        raise HTTPException(status_code=400, detail="Text is too short to summarize.")

    try:
        summary = summarize_text(text)
        return {"summary": summary}
    except Exception as e:
        logging.exception("Summarization failed")
        return {"summary": "Summary not available."}

@app.get("/", response_class=HTMLResponse)
async def home():
    if os.path.exists("static/index.html"):
        return open("static/index.html").read()
    return "<h1>Summarizer Microservice</h1>"