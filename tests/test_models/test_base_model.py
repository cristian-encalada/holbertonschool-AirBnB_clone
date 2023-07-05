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

if __name__ == '__main__':
    unittest.main()
