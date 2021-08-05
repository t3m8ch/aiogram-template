import logging
from typing import Optional

from pydantic import BaseSettings, validator


class LoggingConfig(BaseSettings):
    level: str = "info"

    @validator("level")
    def level_must_exist(cls, value: str):
        if value.lower() not in ("error", "warning", "info", "debug"):
            raise ValueError("Level must be one of these: "
                             "error, warning, info, debug")

        return logging.getLevelName(value.upper())


class FSMConfig(BaseSettings):
    use_redis: bool


class SSLConfig(BaseSettings):
    certificate: str
    private_key: str


class BotConfig(BaseSettings):
    token: str
    superusers: Optional[list[int]]
    fsm: Optional[FSMConfig]
    ssl: Optional[SSLConfig]


class DBConfig(BaseSettings):
    url: str = "postgresql+asyncpg://localhost/telegram_bot"


class Config(BaseSettings):
    bot: BotConfig
    logging: LoggingConfig = LoggingConfig()
    db: DBConfig = DBConfig()
