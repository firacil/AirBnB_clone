#!/usr/bin/python3
"""Contains the TestUser classes"""
import unittest
from models.user import User
from models.base_mode import BaseModel


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test if User is subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
