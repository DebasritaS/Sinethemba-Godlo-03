from src.models.review_cycle import ReviewCycleCreateRequest, ReviewCycleResponse
from src.repositories.review_cycle_repository import ReviewCycleRepository
from datetime import datetime
from typing import List
from src.models.entities.review_cycle import ReviewCycle


class ReviewCycleService:
    def __init__(self, review_repo: ReviewCycleRepository):
        self.review_repo = review_repo

    def start_cycle(self, cycle_id: str, reviewer_id: str, description: str):
        if self.review_repo.read(cycle_id):
            raise ValueError(f"Review cycle {cycle_id} already exists.")

        cycle = ReviewCycle(
            cycle_id=cycle_id,
            reviewer_id=reviewer_id,
            description=description,
            status="In Progress",
            started_at=datetime.now(),
            completed_at=None
        )
        self.review_repo.create(cycle)

    def complete_cycle(self, cycle_id: str):
        cycle = self.review_repo.read(cycle_id)
        if not cycle:
            raise KeyError(f"Cycle ID {cycle_id} not found.")
        if cycle.status != "In Progress":
            raise ValueError("Only 'In Progress' cycles can be completed.")

        cycle.status = "Completed"
        cycle.completed_at = datetime.now()
        self.review_repo.update(cycle)

    def get_cycle(self, cycle_id: str) -> ReviewCycle:
        return self.review_repo.read(cycle_id)

    def list_active_cycles(self) -> List[ReviewCycle]:
        return [c for c in self.review_repo.list_all() if c.status == "In Progress"]
