import json

import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.database import async_session_maker, engine
from app.main import app as fastapi_app
from app.users.model import Users
from sqlmodel import SQLModel


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    users = open_mock_json("user")

    async with async_session_maker() as session:
        for Model, values in [
            (Users, users),
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope="function")
async def ac():
    "Асинхронный клиент для тестирования эндпоинтов"
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
