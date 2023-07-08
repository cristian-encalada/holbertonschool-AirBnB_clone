#!/usr/bin/python3
"""Unit tests for models/review.py
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittest for class Review"""

    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        r1 = Review()
        self.assertTrue(hasattr(r1, 'place_id'))
        self.assertTrue(hasattr(r1, 'user_id'))
        self.assertTrue(hasattr(r1, 'text'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        r2 = Review()
        self.assertEqual(type(r2.place_id), str)
        self.assertEqual(r2.place_id, "")

        self.assertEqual(type(r2.user_id), str)
        self.assertEqual(r2.user_id, "")

        self.assertEqual(type(r2.text), str)
        self.assertEqual(r2.text, "")

    def test_isInstance(self):
        """Check if the object is an instance of Review"""
        r3 = Review()
        self.assertIsInstance(r3, Review)


if __name__ == "__main__":
    unittest.main()
