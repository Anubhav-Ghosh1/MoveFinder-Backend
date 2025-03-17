from sqlalchemy.orm import Session
from schemas import movie_schema as schemas
from models import movie_schema as models

def create_movie(db: Session, movie: schemas.MovieRequest):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def update_movie(db: Session, movie_id: int, movie: schemas.MovieRequest):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    db_movie.title = movie.title or db_movie.title
    db_movie.director = movie.director or db_movie.director
    db_movie.year = movie.year or db_movie.year
    db_movie.genre = movie.genre or db_movie.genre
    db_movie.rating = movie.rating or db_movie.rating
    db_movie.runtime = movie.runtime or db_movie.runtime
    db_movie.actors = movie.actors or db_movie.actors
    db_movie.poster = movie.poster or db_movie.poster
    db_movie.release_date = movie.release_date or db_movie.release_date
    db_movie.imdb_rating = movie.imdb_rating or db_movie.imdb_rating
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_movies_by_title(db: Session, title: str):
    return db.query(models.Movie).filter(models.Movie.title == title).all()

def get_movies_by_director(db: Session, director: str):
    return db.query(models.Movie).filter(models.Movie.director == director).all()