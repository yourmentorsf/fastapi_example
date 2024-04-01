from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from sqlalchemy.orm import declarative_base # ненужный импорт
from app.users.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db.sqlite"


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base() # Ошибка!

Base.metadata.create_all(bind=engine)


def get_test_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
