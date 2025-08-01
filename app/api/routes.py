from fastapi import APIRouter, HTTPException, Request
from app.models.parser import parse_document_from_url
from app.llm_api import query_llm  
from app.services.rag_service import run_rag_pipeline
import subprocess
import asyncio

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



WEBHOOK_SECRET = "This is the secrete key"  # Replace with a strong secret

@router.post("/webhook")
async def webhook_listener(request: Request):
    # Verify secret header (optional but strongly recommended)
    secret = request.headers.get("X-Webhook-Secret")
    if secret != WEBHOOK_SECRET:
        raise HTTPException(status_code=403, detail="Forbidden")

    payload = await request.json()
    print("Webhook payload received:", payload)

    # Run deploy.sh asynchronously
    process = await asyncio.create_subprocess_shell(
        "./deploy.sh",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        print(f"Deployment failed:\n{stderr.decode()}")
        raise HTTPException(status_code=500, detail="Deployment failed")

    print(f"Deployment succeeded:\n{stdout.decode()}")
    return {"message": "Deployment triggered successfully"}
