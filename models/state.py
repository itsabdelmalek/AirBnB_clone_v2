#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False, unique=True)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """Get a list of all related City objects"""
            from models import storage
            city_list = []
            city_all = storage.all(City)
            for city in city_all.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
