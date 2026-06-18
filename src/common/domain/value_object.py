from dataclasses import dataclass, field
import uuid

from src.common.domain.exceptions import InvalidUuidException


@dataclass
class UniqueEntityId:
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        self.__validate(self.id)

    def __validate(self, value: str) -> None:
        try:
            uuid.UUID(value)
        except (ValueError, TypeError, AttributeError) as exception:
            raise InvalidUuidException() from exception
