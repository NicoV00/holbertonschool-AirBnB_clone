#!/usr/bin/python3
"""test"""
import unittest
from models.base_model import BaseModel


class Testmodel(unittest.TestCase):
    """Testing base model class"""

    def test__str__(self):
        """Test __str__"""
        self.assertEqual(str(test)[:11], "[BaseModel]")

    def test_to_dict(self):
        """test_to_dict """
        bm = BaseModel()
        dic = bm.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertTrue(type(dic['created_at']) is str)
        self.assertTrue(type(dic['updated_at']) is str)


if __name__ == "__main__":
    unittest.main()
