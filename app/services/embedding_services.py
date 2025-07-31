from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from typing import List, Tuple

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_faiss_index(chunks: List[dict]) -> Tuple[faiss.IndexFlatL2, List[str]]:
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, texts

def search(query: str, index: faiss.IndexFlatL2, texts: List[str], top_k: int = 3) -> List[str]:
    q_embedding = model.encode([query], convert_to_numpy=True)
    D, I = index.search(q_embedding, top_k)
    return [texts[i] for i in I[0]]
