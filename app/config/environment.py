from functools import lru_cache
import os

from pydantic_settings import BaseSettings

@lru_cache
def get_env_filename():
  runtime_env = os.getenv("ENVIRONMENT")
  return f".env.{runtime_env}" if runtime_env else ".env"

class EnvironmentSettings(BaseSettings):
  API_TITLE: str = "Mirai Embedding API"
  API_DESCRIPTION: str = "This project is a FastAPI-based application that generates text embeddings using a pre-trained language model."
  API_VERSION: str
  API_KEY: str

  class Config:
    env_file = get_env_filename()
    env_file_encoding = "utf-8"

@lru_cache
def get_environment_variables():
  return EnvironmentSettings()