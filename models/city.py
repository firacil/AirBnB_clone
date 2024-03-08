#!/usr/bin/python3
"""contains the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)
