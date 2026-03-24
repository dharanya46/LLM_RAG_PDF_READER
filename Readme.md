# 🤖 LLM PDF RAG Chatbot

## 📌 Overview

This project is an AI-powered chatbot that can:

* Read PDF documents
* Answer questions using Retrieval-Augmented Generation (RAG)
* Provide accurate, context-aware responses

---

## 🚀 Features

* 📄 PDF Upload
* 🔍 Text Extraction
* ✂️ Chunking
* 🧠 Embedding Generation
* 📦 Vector Search (FAISS)
* 💬 Question Answering
* 📝 Document Summarization

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **LLM:** Ollama (Llama3.2)
* **Embeddings:** Sentence Transformers
* **Vector DB:** FAISS

---

## 📁 Project Structure

```
backend/
  └── app/
      └── main.py

frontend/
  └── app.py
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/llm-pdf-rag-project.git
cd llm-pdf-rag-project
```

---

### 2️⃣ Run Backend

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 3️⃣ Run Frontend

```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 How It Works

1. User uploads a PDF
2. Text is extracted and split into chunks
3. Embeddings are generated
4. Stored in FAISS vector database
5. Relevant chunks are retrieved based on query
6. LLM generates a context-based answer

---

## 🔮 Future Improvements

* Multi-PDF support
* Chat history
* Cloud deployment

---

