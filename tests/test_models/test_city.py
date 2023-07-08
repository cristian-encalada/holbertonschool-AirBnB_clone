#!/usr/bin/python3
"""Unit tests for models/city.py
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unittest for class City"""
    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        c1 = City()
        self.assertTrue(hasattr(c1, 'state_id'))
        self.assertTrue(hasattr(c1, 'name'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        c2 = City()
        self.assertEqual(type(c2.state_id), str)
        self.assertEqual(c2.state_id, "")

        self.assertEqual(type(c2.name), str)
        self.assertEqual(c2.name, "")

    def test_isInstance(self):
        """Check if the object is instance of City"""
        c4 = City()
        self.assertIsInstance(c4, City)


if __name__ == "__main__":
    unittest.main()
