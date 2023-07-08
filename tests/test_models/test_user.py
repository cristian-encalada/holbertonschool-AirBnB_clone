#!/usr/bin/python3
"""Unit tests for models/place.py
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittest for class User"""

    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        u1 = User()
        self.assertTrue(hasattr(u1, 'email'))
        self.assertTrue(hasattr(u1, 'password'))
        self.assertTrue(hasattr(u1, 'first_name'))
        self.assertTrue(hasattr(u1, 'last_name'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        u2 = User()
        self.assertEqual(type(u2.email), str)
        self.assertEqual(u2.email, "")

        self.assertEqual(type(u2.password), str)
        self.assertEqual(u2.password, "")

        self.assertEqual(type(u2.first_name), str)
        self.assertEqual(u2.first_name, "")

        self.assertEqual(type(u2.last_name), str)
        self.assertEqual(u2.last_name, "")

    def test_isInstance(self):
        """Check if the object is an instance of User"""
        u3 = User()
        self.assertIsInstance(u3, User)


if __name__ == "__main__":
    unittest.main()
