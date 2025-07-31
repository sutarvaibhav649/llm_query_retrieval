from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="LLM Query Retrieval System")

app.include_router(router, prefix="/api/v1")
