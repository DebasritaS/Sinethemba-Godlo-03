from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(Generic[T, ID], ABC):
    pass
