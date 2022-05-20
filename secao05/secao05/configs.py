from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:test@localhost:5434/faculdade"
    
    class Config:
        case_sensitive = True


settings: Settings = Settings()