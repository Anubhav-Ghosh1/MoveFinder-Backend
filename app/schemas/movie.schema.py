from pydantic import BaseModel
from datetime import datetime

class MovieRequest(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: int
    runtime: int
    actors: list
    poster: str
    release_date: datetime
    imdb_rating: int

class MovieResponse(BaseModel):
    id: int
    title: str
    director: str
    year: int
    genre: str
    rating: int
    runtime: int
    actors: list
    poster: str
    release_date: datetime
    imdb_rating: int

    class Config:
        orm_mode = True