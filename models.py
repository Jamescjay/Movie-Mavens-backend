from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, Integer, DateTime

Base = declarative_base()

class Review(Base):
  __tablename__ = "reviews"

  id = Column(Integer(), primary_key=True)
  name = Column(Text(), nullable=False)
  review = Column(VARCHAR, nullable=False)
  date_posted = Column(DateTime(), nullable=False)
  ratings = Column(Integer(), nullable=False)