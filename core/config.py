from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator



class Settings(BaseSettings):

    API_PREFIX: str = "/api"
    DEBUG: bool = True
    DATABASE_URL: str
    ALLOWED_ORIGINS:str = ""
    GEMINI_API_KEY: str

    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings  = Settings()

