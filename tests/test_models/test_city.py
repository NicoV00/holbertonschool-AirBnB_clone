#!/usr/bin/python3
"""test"""


import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

if __name__ == '__main__':
    unittest.main()