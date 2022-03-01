from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from organs_framework.db import engine

Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'title': self.title,
            'lastname': self.lastname
        }
        return data


Base.metadata.create_all(engine)
