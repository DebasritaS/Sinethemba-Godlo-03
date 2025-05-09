from typing import Dict, Generic, TypeVar, List
from src.repositories.repository import Repository

T = TypeVar('T')
ID = TypeVar('ID')

class InMemoryRepository(Repository[T, ID], Generic[T, ID]):
    def __init__(self):
        self.storage: Dict[ID, T] = {}

    def create(self, entity: T) -> None:
        entity_id = getattr(entity, 'id', None)
        if entity_id is None:
            raise ValueError("Entity must have an 'id' attribute.")
        self.storage[entity_id] = entity

    def read(self, id: ID) -> T:
        return self.storage.get(id)

    def update(self, entity: T) -> None:
        entity_id = getattr(entity, 'id', None)
        if entity_id is None or entity_id not in self.storage:
            raise ValueError("Entity must exist to be updated.")
        self.storage[entity_id] = entity

    def delete(self, id: ID) -> None:
        if id in self.storage:
            del self.storage[id]

    def list_all(self) -> List[T]:
        return list(self.storage.values())
