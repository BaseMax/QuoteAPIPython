from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
# from app.schema import Quote
from app.quote import Quote 


application = FastAPI()

@application.get("/quotes")
async def get_all_quotes(db: Session = Depends(get_db)):
    quote = Quote(db)
    quote.get_all()
    
    