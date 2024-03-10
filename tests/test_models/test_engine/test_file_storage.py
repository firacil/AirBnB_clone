#!/usr/bin/python3
""" Unitttest module for the FileStorage class"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """test case for FileStorage class"""
    
    def setUp(self):
        """sets up test methods"""
        pass

    def Storagereset(self):
        """resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """tears down test methods"""
        self.Storagereset()
        pass

    def test_instantiation(self):
        """test instantation"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_fattributes(self):
        """tests class attributes"""
        self.Storagereset()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def helper_test_all(self, classname):
        """Helper tests all() method for classname"""
        self.Storagereset()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_all_base_model(self):
        """tests all() model for BaseModel."""
        self.helper_test_all("BaseModel")

    def test_all_user(self):
        """tests all() model for User."""
        self.helper_test_all("User")

    def test_all_state(self):
        """tests all() model for state."""
        self.helper_test_all("State")

    def test_all_city(self):
        """tests all() model for City."""
        self.helper_test_all("City")

    def test_all_amenity(self):
        """tests all() model for Amenity."""
        self.helper_test_all("Amenity")

    def test_all_place(self):
        """tests all() model for place."""
        self.helper_test_all("Place")

    def test_all_review(self):
        """tests all() model for Review."""
        self.helper_test_all("Review")


if __name__ == '__main__':
    unittest.main()
