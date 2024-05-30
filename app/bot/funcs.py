from httpx import AsyncClient


async def get_user_from_db(user_id: int):
    async with AsyncClient() as client:
        response = await client.post(
            "http://api:8000/users/find", params={"tg_id": user_id}, timeout=600
        )

    return response.json()


async def get_news_from_websites(type: str):
    async with AsyncClient() as client:
        response = await client.get("http://api:8000/news", params={"type": type}, timeout=600)

    return response.json()
