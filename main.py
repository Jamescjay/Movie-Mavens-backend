from fastapi import FastAPI

app = FastAPI()

@app.get('/reviews')
def index():
  return []

@app.post('/reviews')
def create():
  return {}

@app.patch('/reviews/{reviews_id}')
def updated_review(reviews_id: int):
  return {'message':f'Review {reviews_id} created successfully'}

@app.delete('/reviews/{reviews_id}')
def delete_reviews(reviews_id: int):
  return {'message':f'Review {reviews_id} deleted successfully'}