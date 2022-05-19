from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """configurações gerais usadas na aplicação

    Args:
        BaseSettings (_type_): _description_
    """
    API_V1_STR:  str = "/api/v1"
    DB_URL = "postgresql+asyncpg://postgres:test@localhost:5434/faculdade"
    DBBaseModel = declarative_base()
    
    class Config:
        case_sensitive = True


settings = Settings()