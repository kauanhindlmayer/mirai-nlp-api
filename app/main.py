import logging
import time

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config.environment import get_environment_variables
from app.routes import embedding_router, summarization_router, health_router
from app.services.embedding_service import get_embedding_service
from app.services.summarization_service import get_summarization_service

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
  logger.info("Starting model warm-up...")
  start_time = time.time()
  get_summarization_service()
  get_embedding_service()
  elapsed = time.time() - start_time
  logger.info(f"Model warm-up complete in {elapsed:.2f} seconds.")
  yield

env = get_environment_variables()

app = FastAPI(
  title=env.API_TITLE,
  description=env.API_DESCRIPTION,
  version=env.API_VERSION,
  lifespan=lifespan,
)

app.include_router(health_router.router)
app.include_router(embedding_router.router)
app.include_router(summarization_router.router)
