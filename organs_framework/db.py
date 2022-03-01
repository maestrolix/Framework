from sqlalchemy import create_engine
from settings import DB
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB, echo=True)

Session = sessionmaker(bind=engine)
