from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db
from models import Review
from schemas import ReviewSchema

app = FastAPI()

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
def updated_review(reviews_id: int):
  return {'message':f'Review {reviews_id} created successfully'}

@app.delete('/reviews/{reviews_id}')
def delete_reviews(reviews_id: int, db: Session = Depends(get_db)):
  delete_reviews = db.query(Review).filter(Review.id == reviews_id).first()

  if delete_reviews == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review {reviews_id} does not exist")
  else:
     delete_reviews.delete()
     db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)