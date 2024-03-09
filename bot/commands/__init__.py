__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters.command import CommandStart
from aiogram.filters.command import Command

from bot.commands.start import start
from bot.commands.help import help_command


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
