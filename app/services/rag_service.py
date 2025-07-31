from app.models.parser import parse_document_from_url
from app.services.embedding_services import create_faiss_index, search
from app.llm_api import query_llm
from app.utils.prompt_template import generate_prompt

def run_rag_pipeline(document_url: str, question: str):
    parsed = parse_document_from_url(document_url)
    chunks = parsed["chunks"]
    index, texts = create_faiss_index(chunks)
    top_chunks = search(question, index, texts, top_k=3)
    trimmed = [chunk[:800] for chunk in top_chunks]
    prompt = generate_prompt(question, trimmed)
    answer = query_llm(prompt)
    return {
        "question": question,
        "chunks_used": top_chunks,
        "llm_prompt": prompt,
        "answer": answer
    }
