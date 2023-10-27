#!/usr/bin/python3
"""Store first object"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def save(self):
        """saves objects to json"""
        jsData = {}
        for key, value in self.__objects.items():
            jsData.update([(key, value.to_dict())])
        with open(self.__file_path, 'w') as file:
            json.dump(jsData, file)

    def new(self, obj):
        """new object to __objects"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                for key, obj in json.load(file).items():
                    new_Obj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = new_Obj

        except FileNotFoundError:
            pass
