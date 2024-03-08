#!/usr/bin/pythone3
"""contains the filestorage class"""
import json


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

        classes = {"BaseModel": BaseModel}
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
        with open(FileStorage.__file_path, 'w') as file:
            serialized = {key: obj.to_dict()
                          for key, obj in FileStorage.__objects.items()}
            json.dump(serialized, file)

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
