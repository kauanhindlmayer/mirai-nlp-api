from fastapi import APIRouter, Depends
from app.models.summarization import SummarizeRequest, SummarizeResponse
from app.services.auth_service import authenticate
from app.services.summarization_service import get_summarization_service, SummarizationService

router = APIRouter(tags=["Summarization"])

@router.post(
  "/summarize",
  dependencies=[Depends(authenticate)],
  response_model=SummarizeResponse,
)
async def summarize_text(
  request: SummarizeRequest,
  summarization_service: SummarizationService = Depends(get_summarization_service),
):
  summary = summarization_service.summarize(request.text)
  return SummarizeResponse(summary=summary)
