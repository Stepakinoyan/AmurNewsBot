from app.users.model import Users
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserDB:
    model = Users

    @classmethod
    async def find_user_by_telegram_id(self, id: str, session: AsyncSession):
        query = select(self.model).filter_by(tg_id=id)

        results = await session.execute(query)

        user = results.scalars().all()

        return user
