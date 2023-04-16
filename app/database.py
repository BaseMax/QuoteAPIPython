from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Header, status, HTTPException


DATABASE_URL = "sqlite:///../QuoteAPI.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    token_type, token = authorization.split()
    if token_type != "Bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    return token