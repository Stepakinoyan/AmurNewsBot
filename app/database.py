from typing import AsyncGenerator

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.test_database_url
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.database_url
    DATABASE_PARAMS = {}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    async with async_session() as session:
        yield session
