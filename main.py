from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.quote import Quote 


application = FastAPI()

@application.get("/quotes")
async def get_all_quotes(db: Session = Depends(get_db)):
    quote = Quote(db)
    return quote.get_all()


    
@application.get("/quotes/random")
async def get_random_quote(db: Session = Depends(get_db)):
    quote = Quote(db)
    return quote.get_random()

    

@application.get("/quoets/{quote_id}")
async def get_quote_by_id(quote_id: int,db: Session = Depends(get_db)):
    quote = Quote(db)
    return quote.get_by_id(quote_id)


