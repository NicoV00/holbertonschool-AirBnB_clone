#!/usr/bin/python3
"""test"""

import unittest
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class base model"""
    """Global variables"""
    test = BaseModel()

    def test__str__(self):
        """Test __str__"""
        self.assertEqual(str(self.test)[:11], "[BaseModel]")
    def test_to_dict(self):
        """test_to_dict """
        bm = BaseModel()
        dic = bm.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertTrue(type(dic['created_at']) is str)
        self.assertTrue(type(dic['updated_at']) is str)

    def test_id(self):
        """Test the id attribute."""
        test_dict = {}
        for index in range(1, 101):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.id, test_dict.get(
                f"model{index + 1}", self.test).id
            )
    def test_create_kwargs(self):
        """ create class from dictionary """
        my_model = BaseModel()
        self.dict = my_model.to_dict()
        self.kwargs = BaseModel(self.dict)
        self.assertIsInstance(self.kwargs, BaseModel)

    def test_update(self):
        """ test update date """
        my_model = BaseModel()
        update_old = my_model.updated_at
        my_model.save()
        update_new = my_model.updated_at
        self.assertTrue(update_old != update_new)

    def test_created_at(self):
        """Test create_at attribute."""
        test_dict = {}
        for index in range(1, 20):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.created_at, test_dict.get(
                f"model{index + 1}", self.test).created_at
            )

if __name__ == "__main__":
    unittest.main()
