#!/usr/bin/python3
"""conatains the TestState class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests the class State"""
    def test_is_subclass(self):
        """Tests if State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Tests state has an attribute name, and is an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        obj = State()
        dct = obj.to_dict()
        self.assertEqual(type(dct), dict)
        for item in obj.__dict__:
            self.assertTrue(item in dct)
        self.assertTrue("__class__" in dct)

    def test_str(self):
        """Test the str method"""
        obj = State()
        string = "[State] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))
