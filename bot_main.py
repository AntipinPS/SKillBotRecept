import asyncio
import sys

import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart; from aiogram.types import Message; from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from token_data import TOKEN; from recipes_handler import router

dp = Dispatcher()
dp.include_router(router)

#Главный обработчик
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f'Привет! Я телеграм-бот с рецептами:')
    await message.answer(
        f"Напиши команду \n /category_search_random и число рецептов. \n\n" \
        f"То есть: \n /category_search_random x. X-число рецептов"
        )

async def main() -> None:
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

#Конечный обработчик
if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO, stream=sys.stdout)
   asyncio.run(main())