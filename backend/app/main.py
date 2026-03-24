from fastapi import FastAPI
from pydantic import BaseModel
import fitz  # PyMuPDF
import faiss
import numpy as np
import os
import ollama

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

app = FastAPI()

# --- SETTINGS ---
PDF_FILE = r"your_document.pdf"
LLM_MODEL = 'llama3.2'
EMBED_MODEL = 'all-MiniLM-L6-v2'

# --- PROCESS PDF ---
def process_pdf(file_path):
    if not os.path.exists(file_path):
        return None, None, None

    doc = fitz.open(file_path)
    text = "".join([page.get_text() for page in doc])

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text)

    model = SentenceTransformer(EMBED_MODEL)
    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))

    return index, chunks, model

# Load once
index, chunks, embed_model = process_pdf(PDF_FILE)

# --- Request format ---
class Query(BaseModel):
    question: str

# --- API Endpoint ---
@app.post("/chat")
def chat(query: Query):
    if index is None:
        return {"answer": "PDF not found."}

    prompt = query.question

    # RAG search
    query_vec = embed_model.encode([prompt])
    _, I = index.search(np.array(query_vec).astype('float32'), k=3)
    context = "\n".join([chunks[i] for i in I[0]])

    full_prompt = f"Context: {context}\n\nQuestion: {prompt}"

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{'role': 'user', 'content': full_prompt}]
    )

    answer = response['message']['content']

    return {"answer": answer}
