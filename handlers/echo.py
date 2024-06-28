from aiogram import Router, types
from config import dp

echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.reply("Я Вас не понимаю. Вот команды, которые я понимаю:"
                        "\n/start - начало")
    reversed_text = ' '.join(message.text.split()[::-1])
    await message.answer(reversed_text)


