# 🧠 AI-Powered Text Summarization Microservice

A **FastAPI-based** microservice that uses **Gemini LLM** to summarize text. It is **Dockerized** and easily deployable to **Render**.

---

## 🚀 Setup Instructions


### 1. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 2. **Set Up Environment Variables**

Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_gemini_api_key
```

> ⚠️ **Note:** Never commit `.env` files or API keys to your repository. Use `.gitignore` to exclude them.

### 3. **Run Locally**

```bash
uvicorn app:app --reload
```

### 4. **Run with Docker**

```bash
docker build -t text-summarization .
docker run -p 8000:8000 text-summarization
```

---

## 📬 Example API Requests & Responses

### **GET /**

Returns a welcome message or serves the frontend.

**Request:**

```http
GET http://localhost:8000/
```

**Response:**

```html
AI-Powered Text Summarization Microservice
```

---

### **POST /summarizer**

Summarizes the provided text.

**Request:**

```http
POST http://localhost:8000/summarizer
Content-Type: application/json

{
  "text": "This is a long enough text to test the summarization functionality of our API."
}
```

**Response:**

```json
{
  "summary": "Summarized version here."
}
```

**Error Responses:**

* **Empty text:**

```json
{
  "detail": "Text input is required."
}
```

* **Too short text:**

```json
{
  "detail": "Text too short to summarize."
}
```

---

## 🛠️ API Design Overview

| Endpoint      | Method | Description                                      |
| ------------- | ------ | ------------------------------------------------ |
| `/`           | GET    | Returns static HTML or frontend UI               |
| `/summarizer` | POST   | Accepts text input and returns summarized output |

**Validation:**

* Returns `400` for missing or too-short input.

**Processing:**

* Sends text to Gemini API for summarization.

**Logging:**

* Logs all requests and errors.

---



## 🌟 Future Features

* [ ] **Batch Summarization** – Handle multiple texts in one request
* [ ] **Multilingual Support** – Summarize in multiple languages
* [ ] **Summary Length Control** – Customize output length
* [ ] **Analytics Dashboard** – View usage stats and logs

---

