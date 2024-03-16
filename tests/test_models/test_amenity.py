#!/usr/bin/python3
"""conatains the TestAmenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the class Amenity"""
    def test_is_subclass(self):
        """Tests if Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Tests Amenity has an attribute name, and is an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Amenity()
        dct = obj.to_dict()
        self.assertEqual(type(dct), dict)
        for item in obj.__dict__:
            self.assertTrue(item in dct)
        self.assertTrue("__class__" in dct)

    def test_str(self):
        """Test the str method"""
        obj = Amenity()
        string = "[Amenity] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))
