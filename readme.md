# 🧠 LLM Query Retrieval System

A FastAPI-based backend system designed to extract information from documents using a Retrieval-Augmented Generation (RAG) pipeline powered by Hugging Face's **Mistral-7B-Instruct** LLM.

---

## 🚀 Features

- 🔎 Document parsing from URL (PDF, DOCX)
- 🧠 LLM query answering using Hugging Face Inference API
- 🧩 Simple RAG pipeline: combines retrieval + generation
- ⚡ FastAPI RESTful endpoints for interaction
- 📁 Modular structure for scalability and maintainability

---

## 📂 Project Structure

app/
├── api/
│ └── routes.py # FastAPI route definitions
├── models/
│ └── parser.py # Document parsing logic
├── services/
│ ├── rag_service.py # RAG pipeline logic
│ └── llama_interface.py # Hugging Face LLM API integration
├── main.py # FastAPI app entry point
.env # Hugging Face API token
requirements.txt # Project dependencies
Procfile # For Heroku deployment
README.md

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sutarvaibhav649/llm-query-retrieval.git
cd llm-query-retrieval

python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows


pip install -r requirements.txt

HF_API_TOKEN=your_huggingface_api_key_here


uvicorn app.main:app --reload

Method	Endpoint	Description
GET	/	Health check
GET	/api/v1/llama-test?prompt=	Test LLM response with input prompt
GET	/api/v1/test-parse?url=	Parse content from a document URL
GET	/api/v1/rag-query?url=...&question=...	RAG response for given question