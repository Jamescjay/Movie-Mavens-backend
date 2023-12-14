from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:56ubPPVEu6RTmHv76DGEfHfdUKsQBNnp@dpg-clthad8l5elc73dp88o0-a.frankfurt-postgres.render.com/reviews_7dne", echo=True)

sessionLocal = sessionmaker(bind=engine)

def get_db():
  db = sessionLocal()
  try:
    yield db
  finally:
    db.close()