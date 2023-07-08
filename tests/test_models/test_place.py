#!/usr/bin/python3
"""Unit tests for models/place.py
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittest for class Place"""

    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        p1 = Place()
        self.assertTrue(hasattr(p1, 'city_id'))
        self.assertTrue(hasattr(p1, 'user_id'))
        self.assertTrue(hasattr(p1, 'name'))
        self.assertTrue(hasattr(p1, 'description'))
        self.assertTrue(hasattr(p1, 'number_rooms'))
        self.assertTrue(hasattr(p1, 'number_bathrooms'))
        self.assertTrue(hasattr(p1, 'max_guest'))
        self.assertTrue(hasattr(p1, 'price_by_night'))
        self.assertTrue(hasattr(p1, 'latitude'))
        self.assertTrue(hasattr(p1, 'longitude'))
        self.assertTrue(hasattr(p1, 'amenity_ids'))

    def test_attribute_values(self):
        """Check type/value of attributes"""
        p2 = Place()
        self.assertEqual(type(p2.city_id), str)
        self.assertEqual(p2.city_id, "")

        self.assertEqual(type(p2.user_id), str)
        self.assertEqual(p2.user_id, "")

        self.assertEqual(type(p2.name), str)
        self.assertEqual(p2.name, "")

        self.assertEqual(type(p2.description), str)
        self.assertEqual(p2.description, "")

        self.assertEqual(type(p2.number_rooms), int)
        self.assertEqual(p2.number_rooms, 0)

        self.assertEqual(type(p2.number_bathrooms), int)
        self.assertEqual(p2.number_bathrooms, 0)

        self.assertEqual(type(p2.max_guest), int)
        self.assertEqual(p2.max_guest, 0)

        self.assertEqual(type(p2.price_by_night), int)
        self.assertEqual(p2.price_by_night, 0)

        self.assertEqual(type(p2.latitude), float)
        self.assertEqual(p2.latitude, 0.0)

        self.assertEqual(type(p2.longitude), float)
        self.assertEqual(p2.longitude, 0.0)

        self.assertEqual(type(p2.amenity_ids), str)
        self.assertEqual(p2.amenity_ids, "")

    def test_isInstance(self):
        """Check if the object is an instance of Place"""
        p3 = Place()
        self.assertIsInstance(p3, Place)


if __name__ == "__main__":
    unittest.main()
