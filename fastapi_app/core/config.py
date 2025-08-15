from pathlib import Path
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False,
    echo_pool: bool = False,
    pool_size: int = 50,
    max_overflow: int = 10,


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    # for SQLite:
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/database.db"
    # db_echo: bool = False
    db_echo: bool = True
    # for PostgreSQL:
    db: DatabaseConfig


settings = Settings()
