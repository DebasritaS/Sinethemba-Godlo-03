from abc import ABC
from src.repositories.base import Repository  # Ensure this path is correct
from src.review_cycle import ReviewCycle


class ReviewCycleRepository(Repository[ReviewCycle, int], ABC):
    pass
