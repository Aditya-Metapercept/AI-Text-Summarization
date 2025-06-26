bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## 🧪 Run Tests
```bash
pytest
```

## 🐳 Docker
```bash
docker build -t summarizer .
docker run -p 8000:8000 summarizer
```

## 📬 API
**POST /summarize**
```json
{ "text": "Some long text to summarize..." }
```
**Response**
```json
{ "summary": "Summarized version here." }
```
