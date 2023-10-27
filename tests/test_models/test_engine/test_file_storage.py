#!/usr/bin/python3
"""test"""


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()
        self.base_model = BaseModel()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))

    def test_new(self):
        self.storage.new(self.base_model)
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        self.storage.new(self.base_model)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertTrue(data)

    def test_reload(self):
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertTrue(key in self.storage.all())

if __name__ == '__main__':
    unittest.main()