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
## 🌐 Optional Frontend
Visit [http://localhost:8000](http://localhost:8000) after starting the service.

## 🔮 Future Ideas
- Multilingual support
- User auth for tracking
- Save summaries to DB
- Summarize from URLs or files
