from pydantic import BaseModel


class ReviewSchema(BaseModel):
  movie_id: int
  name: str
  review: str
  date_posted: str
  ratings: int

class UserSchema(BaseModel):
  name: str

class MovieSchema(BaseModel):
  Title: str
  Poster: str
  
