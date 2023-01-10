from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseSettings
from decouple import config
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = config('API_V1_STR')
    DB_URL: str = config('DB_URL')
    DBBasemodel = declarative_base()

    JWT_SECRET: str = config('JWT_SECRET')
    """
    import secrets

    token: str = secrets.token_urlsafe(32)

    """
    ALGORITHM: str = 'HS256'

    # Token válido por uma semana => 7 dias
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()
