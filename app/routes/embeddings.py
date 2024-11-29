from fastapi import APIRouter, Depends
from app.models.embeddings import EmbeddingRequest, EmbeddingResponse
from app.services.auth_service import authenticate
from app.services.embedding_service import get_embedding_service, EmbeddingService

router = APIRouter(tags=["Embeddings"])

@router.post(
  "/embed",
  dependencies=[Depends(authenticate)],
  response_model=EmbeddingResponse,
)
async def generate_embedding(
  request: EmbeddingRequest,
  embedding_service: EmbeddingService = Depends(get_embedding_service),
):
  embedding = embedding_service.get_embedding(request.text)
  return EmbeddingResponse(embedding=embedding)
