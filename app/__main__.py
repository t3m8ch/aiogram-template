import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from pydantic_loader.toml_config import load_toml

from app.config import Config


def run():
    config = load_toml(Config, Path("config.toml"))

    event_loop = asyncio.get_event_loop()

    logging.basicConfig(
        level=config.logging.level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    fsm_storage = MemoryStorage()

    bot = Bot(token=config.bot.token, parse_mode="HTML", loop=event_loop)
    dispatcher = Dispatcher(bot, storage=fsm_storage, loop=event_loop)

    executor.start_polling(dispatcher)


if __name__ == '__main__':
    run()
