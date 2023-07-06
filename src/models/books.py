import uuid
from typing import Optional
from pydantic import BaseModel, Field, validator


class Books(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4(), alias="_id")
    title: str
    description: str
    price: float = Field(gt=0)
    author: str
    pages: int = Field(gt=0)
    genre: str

    validator('genre')

    def genre_must_be_in_genres(cls, genre):
        genres = ['Fiction', 'Non Fiction']
        if genre not in genres:
            raise ValueError(f'Genre must be in {genres}')
        return genre

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "One hundread years of solitude",
                "description": " One of the most influential literary works of our time by the masterful Gabriel Garcia Marquez",
                "price": 25,
                "author": "Gabriel Garica Marquez",
                "pages": 417,
                "genre": "Fiction"
            }
        }


class BooksUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "title": "One hundread years of solitude",
                "description": "Good Looks",
                "price": 20
            }
        }
