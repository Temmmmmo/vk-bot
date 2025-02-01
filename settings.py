from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings"""

    VK_API_TOKEN: str
    VK_GROUP_ID: int
    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=".env", extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
