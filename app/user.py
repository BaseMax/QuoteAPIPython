from fastapi import Depends

from .database import get_db
from .models import User as UserModel


class User:
    """
        a class for auth users
    """
    
    def __init__(self, db = Depends(get_db)) -> None:
        self.db = db
        
    
    def check(self, token):
        user = self.db.query(UserModel).filter(UserModel.token == token).first()
        if user:
            return True
        return False
