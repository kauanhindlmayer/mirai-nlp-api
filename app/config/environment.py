import os
from functools import lru_cache
from pydantic_settings import BaseSettings

@lru_cache
def get_env_filename() -> str:
  runtime_env = os.getenv("ENVIRONMENT")
  return f".env.{runtime_env}" if runtime_env else ".env"

class EnvironmentSettings(BaseSettings):
  API_TITLE: str = "Mirai NLP API"
  API_DESCRIPTION: str = "A support service for Mirai that handles text embedding and summarization."
  API_VERSION: str
  API_KEY: str
  
  class Config:
    env_file = get_env_filename()
    env_file_encoding = "utf-8"

@lru_cache
def get_environment_variables() -> EnvironmentSettings:
  return EnvironmentSettings()
