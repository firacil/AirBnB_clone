#!/usr/bin/python3
"""conatains the TestPlace class"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests the class Place"""
    def test_is_subclass(self):
        """Tests if Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        """Tests if Place has an attribute city_id, and is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test if Place has an attribute user_id, and is an empty string"""
        place = Place ()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_description_attr(self):
        """Test if Place has an attribute description, and is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Test if Place has an attribute number_rooms, and is an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test if Place has an attribute number_bathrooms, and ia an int == 0"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)

    def test_name_attr(self):
        """Tests if Place has an attribute name, and is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Place()
        dct = obj.to_dict()
        self.assertEqual(type(dct), dict)
        for item in obj.__dict__:
            self.assertTrue(item in dct)
        self.assertTrue("__class__" in dct)

    def test_str(self):
        """Test the str method"""
        obj = Place()
        string = "[Place] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))
