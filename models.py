from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, VARCHAR, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Review(Base):
  __tablename__ = "reviews"

  id = Column(Integer(), primary_key=True)
  name = Column(Text(), nullable=False)
  review = Column(VARCHAR, nullable=False)
  date_posted = Column(DateTime(), nullable=False)
  ratings = Column(Integer(), nullable=False)

  movie_id = Column(Integer(), ForeignKey("movies.id"))
  user_id = Column(Integer(), ForeignKey("users.id"))


class User(Base):
  __tablename__ = "users"

  id = Column(Integer(), primary_key=True)
  name =Column(Text(), nullable=False)

  reviews = relationship("Review", backref="user")


class Movies(Base):
  __tablename__ = "movies"

  id = Column(Integer(), primary_key=True)
  title = Column(Integer(), nullable=False)
  image = Column(VARCHAR, nullable=False)

  audiences = relationship("Review", backref="movie")