from pydantic import BaseModel, Field


class Quote(BaseModel):
    """"""
    text: str = Field(min_length=10)
    author: str = Field(min_length=5)
