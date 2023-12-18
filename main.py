from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db
from models import Review, Movie
from schemas import ReviewSchema, MovieSchema

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/reviews')
def reviews(db: Session = Depends(get_db)):
  reviews= db.query(Review).all()
  return reviews

@app.get('/reviews/{review_id}')
def review(review_id: int, db: Session = Depends(get_db)):
  review = db.query(Review).filter(Review.id == review_id).first()
  return review

@app.post('/reviews')
def create(review: ReviewSchema, db: Session = Depends(get_db)):
  new_review = Review(**review.model_dump())
  db.add(new_review)
  db.commit()
  db.refresh(new_review)
  return {'message':'Review created successfully', 'review': new_review}

@app.patch('/reviews/{reviews_id}')
def update_review(reviews_id: int, updated_review: ReviewSchema, db: Session = Depends(get_db)):
    existing_review = db.query(Review).filter(Review.id == reviews_id).first()

    if existing_review is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review {reviews_id} does not exist")

    # Update only 'ratings' and 'review' fields
    existing_review.ratings = updated_review.ratings
    existing_review.review = updated_review.review

    db.commit()
    db.refresh(existing_review)

    return {'message': f'Review {reviews_id} updated successfully', 'review': existing_review}

@app.delete('/reviews/{reviews_id}')
def delete_reviews(reviews_id: int, db: Session = Depends(get_db)):
  review = db.query(Review).filter(Review.id == reviews_id).first()

  if review == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review {reviews_id} does not exist")
  else:
     db.delete(review)
     db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get('/movies')
def movies(db: Session = Depends(get_db)):
  movies= db.query(Movie).all()
  return movies

@app.get('/movies/{movie_id}')
def movie(movie_id: int, db: Session = Depends(get_db)):
  movie = db.query(Movie).filter(Movie.id == movie_id).first()
  return movie

@app.post('/movies')
def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
  new_movie = Movie(**movie.model_dump())
  db.add(new_movie)
  db.commit()
  db.refresh(new_movie)
  return {'message':'Movie created successfully', 'movie': new_movie}