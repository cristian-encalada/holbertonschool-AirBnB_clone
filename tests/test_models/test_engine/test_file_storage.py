#!/usr/bin/python3
"""
Unit tests for models/engine/file_storage.py
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for class FileStorage"""

    def test_file_path_type(self):
        """Check type of __file_path attribute"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects_type(self):
        """Check type of __objects attribute"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all_method(self):
        """Check methods new(), all() and reload()"""
        storage = FileStorage()
        base1 = BaseModel()
        storage.new(base1)
        all_objs = storage.all()
        self.assertIn(base1, all_objs.values())
        storage.reload()
        all_objs_reloaded = storage.all()  # Get all objects from the reloaded storage
        # Verify that the BaseModel instance is still present in the reloaded storage
        self.assertIn(base1, all_objs_reloaded.values())

    def test_save_fs(self):
        """Check save() method"""
        base2 = BaseModel()
        updated_at = base2.updated_at
        base2.save()
        last_updated_at = base2.updated_at
        self.assertNotEqual(updated_at, last_updated_at)

    def test_path(self):
        """Create an FileStorage"""
        self.storage = FileStorage()
        self.path = "file.json"

if __name__ == '__main__':
    unittest.main()
