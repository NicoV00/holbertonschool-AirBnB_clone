#!/usr/bin/python3
"""test"""


import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_user_to_dict(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')

if __name__ == '__main__':
    unittest.main()