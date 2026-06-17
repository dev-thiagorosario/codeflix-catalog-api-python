import unittest
import uuid
from src.category.domain.entities import Category

from datetime import datetime


class TestCategory(unittest.TestCase):
    def test_constructor(self):
        created_at = datetime.now()

        category = Category('Movie', 'some description', True, created_at)

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, True)
        self.assertEqual(category.created_at, created_at)
        self.assertIsInstance(category.id, uuid.UUID)

    def test_constructor_with_default_values(self):
        category = Category(name='Movie')

        self.assertEqual(category.name, 'Movie')
        self.assertIsNone(category.description)
        self.assertTrue(category.is_active)
        self.assertIsInstance(category.created_at, datetime)
        self.assertIsInstance(category.id, uuid.UUID)
