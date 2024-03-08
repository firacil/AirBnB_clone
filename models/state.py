#!/usr/bin/python3
"""contains the State class"""
from models.base_model import BaseModel

class State(BaseModel):
    """Represents a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)
