from fastapi import FastAPI
from app.routes import health, embeddings
from app.config.environment import get_environment_variables

env = get_environment_variables()

app = FastAPI(
  title=env.API_TITLE,
  description=env.API_DESCRIPTION,
  version=env.API_VERSION,
)

app.include_router(health.router)
app.include_router(embeddings.router)
