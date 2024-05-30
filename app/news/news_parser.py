from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime
from httpx import AsyncClient
from app.news.schemas import Article




headers = {"user-agent": UserAgent().random}


async def get_news(type: str):
    if type == "Технологии":
        url = "https://gtrkamur.ru/themes/tehnologii"
    elif type == "Экономика":
        url = "https://gtrkamur.ru/themes/economy"
    elif type == "Строительство":
        url = "https://gtrkamur.ru/themes/construction"

    async with AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=600)
        soup = BeautifulSoup(response.text, "lxml")
        today_date = datetime.now().strftime("%d")

        return [
            Article(
                title=i.find("img").get("alt").replace(" - gtrkamur.ru", ""), url=i.find("a").get("href")
            ).model_dump()
            for i in soup.find_all("li")
            if "https://gtrkamur.ru/news" in i.find("a").get("href")
            and today_date in i.find("div", class_="b-item__time").text
        ]
