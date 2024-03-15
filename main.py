import os
import asyncio
import json
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

# from hendlers import commands
from data.database import create_table
from hendlers import commands


logging.basicConfig(level=logging.INFO)

load_dotenv()

bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher()

dp.include_router(commands.router)

async def main():
    await create_table()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
