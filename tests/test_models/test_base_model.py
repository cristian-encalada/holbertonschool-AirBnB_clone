#!/usr/bin/python3
"""
Unit tests for models/base_model.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for class BaseModel"""
    def test_type_attributes_bm(self):
        """Check attribute types"""
        base0 = BaseModel()
        self.assertEqual(type(base0.id), str)
        self.assertEqual(type(base0.created_at), datetime)
        self.assertEqual(type(base0.updated_at), datetime)

    def test_created_bm(self):
        """Check instance.name after create/update"""
        base1 = BaseModel()
        base1.name = "My first name"
        self.assertEqual(base1.name, "My first name")
        base1.name = "My update name"
        self.assertEqual(base1.name, "My update name")
        base1.number = 87
        self.assertEqual(base1.number, 87)

    def test_isInstance_BaseModel(self):
        """Check if object isInstance of BaseModel"""
        base2 = BaseModel()
        self.assertTrue(isinstance(base2, BaseModel))
        self.assertTrue(isinstance(base2.id, str))
        self.assertTrue(isinstance(base2.created_at, datetime))
        self.assertTrue(isinstance(base2.updated_at, datetime))

    def test_save_bm(self):
        """Check save() method"""
        base3 = BaseModel()
        updated_at = base3.updated_at
        base3.save()
        last_updated_at = base3.updated_at
        self.assertNotEqual(updated_at, last_updated_at)

    def test_to_dict_bm(self):
        """Check to_dict() method"""
        base4 = BaseModel()
        base_json = base4.to_dict()
        self.assertEqual(type(base_json), dict)
        self.assertEqual(type(base_json["created_at"]), str)
        self.assertEqual(type(base_json["updated_at"]), str)

    def test_hasattr_after_create(self):
        """Check if a new instance has proper attributes"""
        base5 = BaseModel()
        self.assertTrue(hasattr(base5, 'id'))
        self.assertTrue(hasattr(base5, 'created_at'))
        self.assertTrue(hasattr(base5, 'updated_at'))

    def test_str_(self):
        """Check __str__"""
        b6 = BaseModel()
        string_rep = f"[{b6.__class__.__name__}] ({b6.id}) {b6.__dict__}"
        self.assertEqual(string_rep, b6.__str__())

    def test_to_dict2_bm(self):
        """Check to_dict"""
        base7 = BaseModel()
        self.assertIn('id', base7.to_dict())
        self.assertIn('created_at', base7.to_dict())
        self.assertIn('updated_at', base7.to_dict())

    def test_invalid_kwargs(self):
        """Check TypeError for string input for kwargs"""
        with self.assertRaises(TypeError):
            base8 = BaseModel(**"test")

if __name__ == '__main__':
    unittest.main()
