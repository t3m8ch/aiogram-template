from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


async def on_start_command(message: types.Message):
    await message.answer("Help: /help")


def register_start_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(on_start_command, CommandStart())
