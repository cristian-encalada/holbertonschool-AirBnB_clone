#!/usr/bin/python3
"""Unit tests for models/amenity.py
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittest for class Amenity"""
    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        a1 = Amenity()
        self.assertTrue(hasattr(a1, 'name'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        a2 = Amenity()
        self.assertEqual(type(a2.name), str)
        self.assertEqual(a2.name, "")

    def test_isInstance(self):
        """Check if the object is instance of Amenity"""
        a3 = Amenity()
        self.assertIsInstance(a3, Amenity)


if __name__ == "__main__":
    unittest.main()
