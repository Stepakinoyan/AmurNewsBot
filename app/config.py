from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["TEST", "PROD"]

    TOKEN: str

    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_USER: str
    DB_PORT: int

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    TEST_DB_NAME: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_USER: str
    TEST_DB_PORT: int

    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def test_database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
