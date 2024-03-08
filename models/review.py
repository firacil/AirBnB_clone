#!/usr/bin/python3
"""contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes the class"""
        super().__init__(*args, **kwargs)
