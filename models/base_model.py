#!/usr/bin/python3
"""
    Contains class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel:
    """The base class for the other class in this package"""

    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """String representation of the class"""
        return ("[{:s}] ({}) {}",
                .format(self.__class__.__name__, self.id, self.__dict__)
                )

    def save(self):
        """updates the updatedat attribute to the current date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
