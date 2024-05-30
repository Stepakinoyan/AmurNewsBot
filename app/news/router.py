from typing import Literal
from fastapi import APIRouter
from app.news.news_parser import get_news


router = APIRouter(prefix="/news", tags=["Сбор данных по новостям"])


@router.get("")
async def get_news_by_type(type: Literal["Технологии", "Экономика", "Строительство"]):
    return await get_news(type=type)
