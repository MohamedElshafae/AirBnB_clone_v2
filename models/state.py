#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ == 'states'
        name = Column(String(128), nullable=True)
        cities = relationship("City", backref="state")

    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances"""
            all_city = storage.all(City)
            list = []

            for city in all_city.values():
                if self.id == city.state_id:
                    list.append(city)
            return list
