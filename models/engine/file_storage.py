#!/usr/bin/python3
"""
That serializes instances to a JSON file and
deserializes JSON file to instances.
"""


import json

class FileStorage:
    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets the obj with a unique key in the __objects dictionary.
        Args:
            obj: The object to store.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects, only if the file exists.
        If the file doesn't exist, no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = models.classes[class_name]
                    new_obj = cls(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass