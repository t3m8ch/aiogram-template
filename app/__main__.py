import asyncio
import logging
from pathlib import Path
from typing import Optional

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.dispatcher.storage import BaseStorage
from aiogram.utils import executor
from pydantic_loader.toml_config import load_toml

from app.bot import register_handlers
from app.config import Config, FSMConfig


def run():
    config = load_toml(Config, Path("config.toml"))

    event_loop = asyncio.get_event_loop()

    logging.basicConfig(
        level=config.logging.level,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    fsm_storage = _get_fsm_storage(config.bot.fsm)

    bot = Bot(token=config.bot.token, parse_mode="HTML", loop=event_loop)
    dispatcher = Dispatcher(bot, storage=fsm_storage, loop=event_loop)

    register_handlers(dispatcher)

    executor.start_polling(dispatcher)


def _get_fsm_storage(fsm_config: Optional[FSMConfig]) -> BaseStorage:
    if not fsm_config:
        return MemoryStorage()

    if fsm_config.use_redis:
        return RedisStorage2()

    return MemoryStorage()


if __name__ == '__main__':
    run()
