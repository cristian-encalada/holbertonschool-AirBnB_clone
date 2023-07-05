#!/usr/bin/python3
"""
Unit tests for models/base_model.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for the functions in BaseModel"""
    def test_type_attributes(self):
        base0 = BaseModel()
        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

    def test_created(self):
        base1 = BaseModel()
        base1.name = "My first name"
        self.assertEqual(base1.name, "My first name")
        base1.name = "My update name"
        self.assertEqual(base1.name, "My update name")
        base1.number = 87
        self.assertEqual(base1.number, 87)

    def test_inheritance(self):
        base2 = BaseModel()
        self.assertTrue(isinstance(base2, BaseModel))

    def test_save(self):
        base3 = BaseModel()
        self.assertEqual(type(base3.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()
