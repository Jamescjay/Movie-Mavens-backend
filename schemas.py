from pydantic import BaseModel


class ReviewSchema(BaseModel):
  name: str
  review: str
  date_posted: str
  ratings: int
