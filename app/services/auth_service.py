from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from app.config.environment import get_environment_variables

env = get_environment_variables()
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

async def authenticate(api_key: str = Security(api_key_header)):
  if api_key != env.API_KEY:
    raise HTTPException(status_code=401, detail="Invalid API Key")
