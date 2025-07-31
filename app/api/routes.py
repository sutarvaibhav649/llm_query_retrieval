from fastapi import APIRouter, HTTPException
from app.models.parser import parse_document_from_url
from app.llm_api import query_llm  
from app.services.rag_service import run_rag_pipeline

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the LLM Query Retrieval System"}

@router.get("/llama-test")
async def llama_test(prompt: str):
    try:
        response = query_llm(prompt)  
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test-parse")
async def test_parse(url: str):
    try:
        parsed_data = parse_document_from_url(url)
        return parsed_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/rag-query")
async def rag_query(url: str, question: str):
    try:
        result = run_rag_pipeline(url, question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
