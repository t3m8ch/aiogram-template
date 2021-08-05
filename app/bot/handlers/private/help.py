from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandHelp


async def on_help_command(message: types.Message):
    await message.answer("Your help message")


def register_help_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_help_command, CommandHelp())
