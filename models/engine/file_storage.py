#!/usr/bin/python3
"""Store first object"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def save(self):
        """saves objects to json"""
        
    def new(self, obj):
        """new object to __objects"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as file:
                for key, obj in json.load(file).items():
                    newObj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = newObj
        except FileNotFoundError:
            pass
