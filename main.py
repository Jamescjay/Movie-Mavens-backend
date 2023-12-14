from fastapi import FastAPI
from schemas import ReviewSchema

app = FastAPI()

@app.get('/reviews')
def index():
  return []

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