#!/usr/bin/python3
""" A Python file similar to model_state.py named model_city.py
that contains the class definition of a City """

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """ Definies a class of all cities """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
