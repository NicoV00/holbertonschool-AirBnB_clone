#!/usr/bin/python3
"""test"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
 

test = BaseModel()
file_storage = FileStorage()


class Testmodel(unittest.TestCase):
    """Testing base model class"""

    def test_id(self):
        """Test the id attribute"""
        test_dict = {}
        for index in range(1, 101):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.id, test_dict.get(
                f"model{index + 1}", test).id
            )

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
