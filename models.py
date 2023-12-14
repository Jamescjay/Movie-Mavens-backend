from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, Integer, DateTime

Base = declarative_base()

class Review(Base):
  __tablename__ = "reviews"

  id = Column(Integer(), primary_key = True),
  name = Column(Text())
  review = Column(VARCHAR())
  date_posted = Column(DateTime())
  ratings = Column(Integer())