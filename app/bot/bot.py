import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from funcs import get_user_from_db, get_news_from_websites
from config import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user = await get_user_from_db(message.from_user.id)

    if user:
        kb = [
            [types.KeyboardButton(text="Технологии")],
            [types.KeyboardButton(text="Экономика")],
            [types.KeyboardButton(text="Строительство")],
        ]

        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

        await message.answer(
            f"Привет, {message.from_user.full_name}!", reply_markup=keyboard
        )
    else:
        await message.answer("Вы не авторизованы.")


@dp.message()
async def get_news(message: types.Message):
        user = await get_user_from_db(message.from_user.id)
        if not user:
            await message.answer("Вы не авторизованы.")
            return

        msg = await message.answer("Загружаю новости, пожалуйста подождите...")

        news = await get_news_from_websites(message.text)
        if news:
            for article in news:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"""
                        Статья: {article.get("title")}\n{article.get("url")}       
                    """,
                )
        else:
            await bot.send_message(chat_id=message.chat.id, text="Ничего не найдено")

        await msg.delete()



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
