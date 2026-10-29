import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql://postgres.aepyjrhmjzlipdvxydao:Ab2LAEjKDx7gat7i@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres")
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "super-secret-dev-key-123")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    CORS_ORIGINS: str = os.environ.get("CORS_ORIGINS", "*")

settings = Settings()