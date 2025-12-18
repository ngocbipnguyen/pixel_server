from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg2://bachnn:123456@127.0.0.1:5432/fast_server"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit =False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
