#!/usr/bin/python3
"""
Unit tests for models/engine/file_storage.py
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Unittest for class FileStorage"""

    def test_all_method(self):
        """Check the all() method"""
        storage = FileStorage()
        base1 = BaseModel()
        base2 = BaseModel()
        storage.new(base1)
        storage.new(base2)
        all_objs = storage.all()
        self.assertIn(base1, all_objs.values())
        self.assertIn(base2, all_objs.values())

    def test_attr_after_create_fs(self):
        """Check instance.name after created"""
        base3 = BaseModel()
        base3.name = "My_First_Model"
        self.assertEqual(base3.name, "My_First_Model")

    def test_save_fs(self):
        """Check save() method"""
        base4 = BaseModel()
        updated_at = base4.updated_at
        base4.save()
        last_updated_at = base4.updated_at
        self.assertNotEqual(updated_at, last_updated_at)

    def test_isInstance_FileStorage(self):
        """Check if an FileStorage object isInstance of BaseModel"""
        base5 = BaseModel()
        self.assertTrue(isinstance(base5, BaseModel))


if __name__ == '__main__':
    unittest.main()
