#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

from models.amenity import Amenity

if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id')),
        Column('amenity_id', String(60), ForeignKey('amenities.id'))
    )


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"))
        user_id = Column(String(60), ForeignKey("users.id"))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        user = relationship("User", back_populates="places")
        cities = relationship("City", back_populates="places")
        reviews = relationship(
            "Review", back_populates="place", cascade="delete, delete-orphan")
        amenities = relationship(
            "Amenity", secondary='place_amenity',
            viewonly=False, overlaps="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Getter to return a list of reviews for a place"""
            from models import storage
            from models.review import Review
            data = storage.all(Review)
            return [v for v in data.values() if v.id == self.id]

        @property
        def amenities(self):
            return [Amenity(id=amenity_id) for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
