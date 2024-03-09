#!/usr/bin/python3
"""Contains the TestUser classes"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test if User is subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email_attr(self):
        """Tests if User has email attribute"""
        user = User()
        self.assertTrue(hasattr(user, "email"))

    def test_password_attr(self):
        """Test if user has password attribute"""
        user = User()
        self.assertTrue(hasattr(user, "password"))

    def test_first_name_attr(self):
        """Test if user has first_name attributes"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))

    def test_last_name_attr(self):
        """Test if user has last_name attributes"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
