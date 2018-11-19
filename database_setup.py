import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class ShoeStore(Base):
    __tablename__ = 'shoestore'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    picture = Column(String(250))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }


class Shoe(Base):
    __tablename__ = 'shoe_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    price = Column(String(8))
    shoestore_id = Column(Integer, ForeignKey('shoestore.id'))
    shoestore = relationship(ShoeStore)
    

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'price': self.price,
            'description': self.description
        }


engine = create_engine('sqlite:///shoecatalog.db')


Base.metadata.create_all(engine)
