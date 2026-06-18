import unittest
import uuid

from src.common.domain.exceptions import InvalidUuidException
from src.common.domain.value_object import UniqueEntityId


class TestUniqueEntityId(unittest.TestCase):
    def test_constructor_generates_valid_uuid(self):
        unique_entity_id = UniqueEntityId()

        self.assertIsInstance(unique_entity_id.id, str)
        self.assertIsInstance(uuid.UUID(unique_entity_id.id), uuid.UUID)

    def test_constructor_with_valid_uuid(self):
        generated_id = str(uuid.uuid4())

        unique_entity_id = UniqueEntityId(generated_id)

        self.assertEqual(unique_entity_id.id, generated_id)

    def test_constructor_with_invalid_uuid(self):
        with self.assertRaises(InvalidUuidException):
            UniqueEntityId("invalid-id")

    def test_constructor_with_invalid_id_type(self):
        with self.assertRaises(InvalidUuidException):
            UniqueEntityId(None)
