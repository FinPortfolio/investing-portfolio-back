# app/adapters/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка подключения к базе данных
sql_file_name = "database.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sql_file_name}"
connect_args = {"check_same_thread": False}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Функция зависимости для получения сессии
# Создание зависимости Session.
# Сессия базы данных (Session) хранит объекты в памяти и отслеживает любые необходимые
# изменения в данных, а затем использует engine для коммуникации с базой данных.
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
