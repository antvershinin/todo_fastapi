from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    completed = Column(Boolean)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
