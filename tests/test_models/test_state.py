#!/usr/bin/python3
"""test"""


import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

if __name__ == '__main__':
    unittest.main()