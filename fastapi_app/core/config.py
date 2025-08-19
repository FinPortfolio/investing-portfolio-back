# core/config.py
from typing import Literal

import logging
from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

LOG_DEFAULT_FORMAT = "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"

BASE_DIR = Path(__file__).parent.parent


ENV_FILES = (
    BASE_DIR / ".env.app.template",
    BASE_DIR / ".env.app",
)

EXISTING_ENV_FILES = (f for f in ENV_FILES if f.exists())


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class GunicornConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    timeout: int = 900


class LoggingConfig(BaseModel):
    log_level: Literal[
        'debug',
        'info',
        'warning',
        'error',
        'critical',
    ] = 'info'
    log_format: str = LOG_DEFAULT_FORMAT


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    stocks: str = "/stocks"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=EXISTING_ENV_FILES,
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    run: RunConfig = RunConfig()
    gunicorn: GunicornConfig = GunicornConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()


# логгер
logger = logging.getLogger("uvicorn.error")
if EXISTING_ENV_FILES:
    logger.info(
        f"The following variables have been loaded: DB_URL: {settings.db.url}, "
        f"DB_ECHO: {settings.db.echo}, DB_ECHO_POOL: {settings.db.echo_pool}."
    )
else:
    logger.warning("No .env file found. Using defaults or environment variables.")
