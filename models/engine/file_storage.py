#!/usr/bin/python3
"File storage"
import json
from models.base_model import BaseModel


class FileStorage:
    """File storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "Returns objects'"
        return FileStorage.__objects
