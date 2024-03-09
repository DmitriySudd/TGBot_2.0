import os
import asyncio
from aiogram import Dispatcher, Bot
from commands import register_user_commands


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(token=os.getenv('token'))

    register_user_commands(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
