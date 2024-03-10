#!/usr/bin/python3
"""conatains the TestReview class"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the class Review"""
    def test_is_subclass(self):
        """Tests if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_to_dict(self):
        """Test to_dict method"""
        obj = Review()
        dct = obj.to_dict()
        self.assertEqual(type(dct), dict)
        for item in obj.__dict__:
            self.assertTrue(item in dct)
        self.assertTrue("__class__" in dct)

    def test_str(self):
        """Test the str method"""
        obj = Review()
        string = "[Review] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))
