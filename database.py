import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
DB_URL = f"postgresql://{user}:{password}@localhost:5432/fliga"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
