#!/usr/bin/python3
"""Unit tests for models/state.py
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittest for class State"""
    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        s1 = State()
        self.assertTrue(hasattr(s1, 'name'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        s2 = State()
        self.assertEqual(type(s2.name), str)
        self.assertEqual(s2.name, "")

    def test_isInstance(self):
        """Check if the object is instance of State"""
        s3 = State()
        self.assertIsInstance(s3, State)


if __name__ == "__main__":
    unittest.main()
