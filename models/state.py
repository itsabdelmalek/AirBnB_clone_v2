#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import os

env_value = os.environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    if env_value == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            from models.__init__ import storage
            from models.city import City

            city_list = []
            d_storage = storage.all(City)
            for key, value in d_storage.items():
                if self.id == value.state_id:
                    city_list.append(value)
            return city_list
