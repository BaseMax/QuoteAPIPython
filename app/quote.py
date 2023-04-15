from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from .models import Quote as QuoteModel
from app.database import get_db

class Quote:
    """Quote class can use for get Quotes and create and ...
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
    