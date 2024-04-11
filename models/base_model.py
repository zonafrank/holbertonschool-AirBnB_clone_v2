#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, String
from os import getenv

Base = object

if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = None
    created_at = None
    updated_at = None

    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60),
                    primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=lambda: datetime.now(timezone.utc))
        updated_at = Column(DateTime,
                            nullable=False,
                            default=lambda: datetime.now(timezone.utc),
                            onupdate=lambda: datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs and isinstance(kwargs, dict):
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())

            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            else:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            else:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        self_dict = {}
        for key, val in self.__dict__.items():
            if key != "_sa_instance_state":
                self_dict[key] = val
        return '[{}] ({}) {}'.format(cls, self.id, self_dict)

    def __repr__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        self_dict = {}
        for key, val in self.__dict__.items():
            if key != "_sa_instance_state":
                self_dict[key] = val
        return '[{}] ({}) {}'.format(cls, self.id, self_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """Delete current instance from storage"""
        from models import storage
        storage.delete(self)
