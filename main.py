from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

from app.quote import Quote
from app.schema import Quote as Qu
from app.database import get_db, get_token


application = FastAPI()

@application.get("/quotes")
async def get_all_quotes(db: Session = Depends(get_db), q: str = Query(None, max_length=50)):
    
    quote = Quote(db)
    if not q:
        return quote.get_all()
    return quote.search(q)


@application.get("/quotes/random")
async def get_random_quote(db: Session = Depends(get_db)):
    quote = Quote(db)
    return quote.get_random()


@application.get("/quoets/{quote_id}")
async def get_quote_by_id(quote_id: int,db: Session = Depends(get_db)):
    quote = Quote(db)
    return quote.get_by_id(quote_id)


@application.post("/quotes")
async def add_quote(UserQuote: Qu, db: Session = Depends(get_db), token: str = Depends(get_token)):
    quote = Quote(db, token)
    return quote.create(UserQuote)


@application.put("/quotes/{quote_id}")
async def edit_quote(quote_id: int, UserQuote: Qu, db: Session = Depends(get_db), token: str = Depends(get_token)):
    quote = Quote(db, token)
    return quote.edit(quote_id, UserQuote)


@application.delete("/quotes/{quote_id}")
async def delete_quote(quote_id: int, db: Session = Depends(get_db), token: str = Depends(get_token)):
    quote = Quote(db, token)
    return quote.delete(quote_id)
