from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from crud import movie_controller as crud
from schemas import movie_schema as schemas
from db.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=schemas.MovieResponse)
def create_movie(movie: schemas.MovieRequest, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@app.get("/movies/", response_model=list[schemas.MovieResponse])
def read_movies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_movies(db, skip=skip, limit=limit)
