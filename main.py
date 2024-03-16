import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from data.database import create_table
from hendlers import commands

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher()

dp.include_router(commands.router)


async def main():
    await create_table()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
