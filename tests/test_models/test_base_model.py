#!/usr/bin/python3
""" Unittesting base_model module"""
from models import storage
import unittest
import uuid
import json
import os
import re
import time
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Testing the User Class"""
    
    def setUp(self):
        """ sets up test method"""
        pass

    def tearDown(self):
        """tears down test Methods"""
        self.Storagereset()
        pass

    def test_instantitation(self):
        """tests instantation of BaseModel class"""
        bm = BaseModel()
        self.assertEqual(str(type(bm)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(bm, BaseModel)
        self.assertTrue(issubclass(type(bm), BaseModel))

    def test_no_args_init_(self):
        """ Test when __init__ with no arguments"""
        self.Storagereset()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
            m = "__init__() missing 1 required positional argument: 'self'"
            self.assertEqual(str(e.exception), m)

    def test_attributes(self):
        """tests attributes vaalue for instance of BaseModel class"""
        attributes = storage.attributes()["BaseModel"]
        bm = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(bm, k))
            self.assertEqual(type(getattr(bm, k, None)), v)

    def test_id(self):
        """Test for unique uuid"""
        u = [BaseModel().id for i in range(100)]
        self.assertEqual(len(set(u)), len(u))

    def test_str(self):
        """ test for __str__ method"""
        bm = BaseModel()
        reg = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = reg.match(str(bm))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), bm.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        dd = bm.__dict__.copy()
        dd["created_at"] = repr(dd["created_at"])
        dd["updated_at"] = repr(dd["updated_at"])
        self.assertEqual(d, dd)

    def test_save(self):
        """ tests method save()"""
        bm = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        bm.save()
        d = bm.updated_at - date_now
        self.assertTrue(abs(d.total_seconds()) < 0.01)

    def test_to_dict(self):
        """ Tests to_dict method"""
        bm = BaseModel()
        bm.name = "John"
        bm.age = 89
        dic = bm.to_dict()
        self.assertEqual(dic["id"], bm.id)
        self.assertEqual(dic["__class__"], type(bm).__name__)
        self.assertEqual(dic["created_at"], bm.created_at.isoformat())
        self.assertEqual(dic["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(dic["name"], bm.name)
        self.assertEqual(dic["age"], bm.age)

    def test_dict_no_args(self):
        """test to_dict() with no arguments"""
        self.Storagereset()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        m = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), m)

    def test_to_dict_excess_args(self):
        """tests to to_dict() with too many arguments"""
        self.Storagereset()
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)
        m = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), m)

    def test_instantiation(self):
        """tests instantiation **kwargs"""

        bm = BaseModel()
        bm.name = "Firaol"
        bm.my_number = 89
        bm_json = bm.to_dict()
        bm_new = BaseModel(**bm_json)
        self.assertEqual(bm_new.to_dict(), bm.to_dict())

    def test_instantiation_kwargs(self):
        """tests instantiation with **kwargs from dict"""
        d = {"__class__": "BaseModel",
             "updated_at":
             datetime(2050, 12, 30, 23, 59, 59, 123456).isoformat(),
             "created_at": datetime.now().isoformat(),
             "id": uuid.uuid4(),
             "var": "foobar",
             "int": 108,
             "float": 3.14}
        bm = BaseModel(**d)
        self.assertEqual(bm.to_dict(), d)

    def test_2save(self):
        """tests that storage.save() is called from save()."""
        self.Storagereset()
        bm = BaseModel()
        bm.save()
        key = "{}.{}".format(type(bm).__name__, bm.id)
        d = {key: bm.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_save_noargs(self):
        """ test save() with no argument"""
        self.Storagereset()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        m = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), m)

    def test_save_exargs(self):
        """ tests save() with too many arguments"""
        self.Storagereset()
        with self.assertRaises(TypeError) as e:
            BaseModel.save(self, 98)
        m = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), m)

    def Storagereset(self):
        """ Resets Filestorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()
