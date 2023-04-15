from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from .database import engine


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String(60), index=True)
    password: str = Column(String(40))

class Quote(Base):
    __tablename__ = "quotes"
    id: int = Column(Integer, primary_key=True, index=True)
    text: str = Column(Text, index=True)
    author: str = Column(String(30), index=True)

Base.metadata.create_all(bind=engine)