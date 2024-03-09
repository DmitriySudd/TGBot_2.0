__all__ = ['start']

from aiogram import Router
from aiogram.filters.command import CommandStart

from bot.commands import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart)
