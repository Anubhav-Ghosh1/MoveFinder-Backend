from sqlalchemy import Column, Integer, String
from app.db.database import Base
from sqlalchemy.dialects.postgresql import JSONB

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)
    genre = Column(String)
    rating = Column(Integer)
    runtime = Column(Integer)
    actors = Column(JSONB)
    poster = Column(String)
    imdb_rating = Column(Integer)