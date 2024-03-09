__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters.command import CommandStart

from bot.commands.start import start

bot_commands = (
    ('start', 'Давайте начнем тест', 'Хорошая команда, чтобы начать работу с ботом'),
    ('help', 'Помощь и справка', 'Поможет, если это будет нужно'),
)


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart)
