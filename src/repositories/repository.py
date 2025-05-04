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

from typing import Generic, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(Generic[T, ID]):
    def get(self, id: ID) -> T:
        raise NotImplementedError

    def get_all(self) -> list[T]:
        raise NotImplementedError

    def create(self, entity: T) -> T:
        raise NotImplementedError

    def update(self, id: ID, entity: T) -> T:
        raise NotImplementedError

    def delete(self, id: ID) -> None:
        raise NotImplementedError