from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Review
from schemas import ReviewSchema

app = FastAPI()

@app.get('/reviews')
def reviews(db: Session = Depends(get_db)):
  reviews= db.query(Review).all()
  return reviews

@app.post('/reviews')
def create(review: ReviewSchema):
  print(review)
  return {'message':'Review created successfully'}

@app.patch('/reviews/{reviews_id}')
def updated_review(reviews_id: int):
  return {'message':f'Review {reviews_id} created successfully'}

@app.delete('/reviews/{reviews_id}')
def delete_reviews(reviews_id: int):
  return {'message':f'Review {reviews_id} deleted successfully'}