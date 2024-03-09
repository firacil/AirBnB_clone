#!/usr/bin/python3
"""
    contains the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)
