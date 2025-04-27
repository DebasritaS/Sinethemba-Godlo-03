from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def read(self, id: ID) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[T]:
        pass
