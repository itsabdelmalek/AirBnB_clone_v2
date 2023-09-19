#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True,
                nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs) -> None:
        """Initializes a new BaseModel """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    date = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns the str representation of the BaseModel instance"""
        cl = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cl, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dict representation of the BaseModel instance"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Deletes the current instance from storage"""
        models.storage.delete(self)
