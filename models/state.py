#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models.base_model import BaseModel, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            list_of_cities = storage.all(City)
            return [city for city
                    in list_of_cities.values()
                    if city.state_id == self.id
                    ]
