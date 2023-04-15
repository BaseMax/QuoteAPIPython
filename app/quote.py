from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
import random

from .database import get_db
from .models import Quote as QuoteModel
from .schema import Quote as QuoteSchema

class Quote:
    """
        Quote class can use for get Quotes and create and ...
    """
    
    def __init__(self, db = Depends(get_db)) -> None:
        self.db = db
        
    
    def get_all(self):
        return self.db.query(QuoteModel).all()
    
    
    def get_by_id(self, quote_id: int):
        quote = self.db.query(QuoteModel).filter(QuoteModel.id == quote_id).first() 
        if quote:
            return quote
        return HTTPException(status_code=404, detail="quote not found.")
    
    
    def get_random(self):
        count = self.get_count()
        if count == 0:
            return JSONResponse({
                "detail": "can not found any quote.",
            }, status_code=404)
        return self.get_by_id(random.randint(1, count))
    
    
    def get_count(self):
        return self.db.query(QuoteModel).count()


    def create(self, UserQuote: QuoteSchema):
        db_quote = QuoteModel(text=UserQuote.text, author=UserQuote.author)
        self.db.add(db_quote)
        self.db.commit()
        self.db.refresh(db_quote)
        return db_quote
    
    
    def edit(self, quote_id: int, UserQuote: QuoteSchema):
        quote = self.get_by_id(quote_id)
        if not quote:
            return JSONResponse({
                "detail": "quote not found."
            }, 404)
        
        quote.text = UserQuote.text
        quote.author = UserQuote.author
        
        self.db.commit()
        self.db.refresh(quote)
        return quote
        