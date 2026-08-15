from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# engine — это "точка входа" для общения с базой данных
engine = create_engine(DATABASE_URL)

# SessionLocal — фабрика сессий (каждый запрос к API будет открывать свою сессию)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base — базовый класс, от которого будут наследоваться все модели (таблицы)
Base = declarative_base()

# Функция-зависимость: будет использоваться в эндпоинтах, чтобы получить сессию БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# yield - это своего рода итератор, который в данной функции будет ждать конца использования сессии, после чего
# закрывать её

