import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import bot, dp, database  # Подключение конфигурации
from handlers.echo import echo_router
from handlers.survey import survey_router

async def on_startup(bot: Bot):
    await database.create_tables()


async def main():
    # регистрируем роутеры
    dp.include_router(survey_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
