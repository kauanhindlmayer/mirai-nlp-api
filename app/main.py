from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import embedding_router, summarization_router, health_router
from app.services.summarization_service import get_summarization_pipeline
from app.config.environment import get_environment_variables

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_summarization_pipeline()
    yield

env = get_environment_variables()

app = FastAPI(
  title=env.API_TITLE,
  description=env.API_DESCRIPTION,
  version=env.API_VERSION,
)

@app.on_event("startup")
def preload_models():
    # Load the summarization model into memory
    get_summarization_pipeline()

app.include_router(health_router.router)
app.include_router(embedding_router.router)
app.include_router(summarization_router.router)
