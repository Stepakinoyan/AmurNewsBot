import json
from fastapi import APIRouter, Depends
from sqlalchemy import insert
from app.users.dao import UserDB
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session_maker
from app.users.model import Users

router = APIRouter(prefix="/users", tags=["Получение информации о пользователях"])


@router.post("/find")
async def find_user(tg_id: int, session: AsyncSession = Depends(get_session)):
    return await UserDB.find_user_by_telegram_id(id=tg_id, session=session)


@router.post("/add")
async def prepare_db(session: AsyncSession = Depends(get_session)):
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