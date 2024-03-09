#!/usr/bin/pythone3
"""contains the filestorage class"""
import datetime
import json
import os


class FileStorage:
    """
        serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Place": Place, "Review": Review}
        return classes

    def all(self):
        """returns the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets an object in __objects"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to the json file"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            serialized = {key: obj.to_dict()
                          for key, obj in FileStorage.__objects.items()}
            json.dump(serialized, f)

    def reload(self):
        """deserializes the json file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objLoaded = json.load(file)
                objLoaded = {key: self.classes()[val["__class__"]](**val)
                             for key, val in objLoaded.items()}
                FileStorage.__objects = objLoaded
        except FileNotFoundError:
            pass

    def attributes(self):
        """ Returns valid attributes and their type for all classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
                     {"place_id": str,
                      "user_id": str,
                      "text": str}
        }
        return attributes
