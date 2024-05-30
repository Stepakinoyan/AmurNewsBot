from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TOKEN: str
    MODE: Literal["TEST", "PROD"]

    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_USER: str
    DB_PORT: int

    TEST_DB_NAME: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_USER: str
    TEST_DB_PORT: int

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SECRET_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
