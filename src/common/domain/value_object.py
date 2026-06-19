from dataclasses import dataclass, field
import uuid

from src.common.domain.exceptions import InvalidUuidException


@dataclass(frozen=True)
class UniqueEntityId:
    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    def __post_init__(self):
        value = str(self.id) if isinstance(self.id, uuid.UUID) else self.id
        object.__setattr__(self, 'id', value)
        self.__validate(self.id)

    def __validate(self, value: str) -> None:
        try:
            uuid.UUID(value)
        except (ValueError, TypeError, AttributeError) as exception:
            raise InvalidUuidException() from exception
    def __str__(self) -> str:
        return f"{self.id}"
    
    def __repr__(self) -> str:
        return f"UniqueEntityId(id='{self.id}')"
