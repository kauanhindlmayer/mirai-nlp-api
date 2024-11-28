from fastapi import FastAPI, Depends
from app.authentication import authenticate
from app.models import EmbeddingRequest, EmbeddingResponse
from app.utils import get_embedding

app = FastAPI(
  title = "Mirai Embedding API",
  description="This project is a FastAPI-based application that generates text embeddings using a pre-trained language model.",
  version="1.0.0"
)

@app.get("/health", tags=["Health Check"])
async def health():
  return {"status": "healthy"}

@app.post(
  "/embed", 
  tags=["Embeddings"], 
  dependencies=[Depends(authenticate)], 
  response_model=EmbeddingResponse)
async def generate_embedding(request: EmbeddingRequest):
  embedding = get_embedding(request.text)
  return EmbeddingResponse(embedding=embedding)
