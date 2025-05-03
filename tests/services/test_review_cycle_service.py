import unittest
from datetime import datetime
from src.services.review_cycle_service import ReviewCycleService
from src.models.review_cycle import ReviewCycle

class InMemoryReviewCycleRepository:
    def __init__(self):
        self.data = {}

    def create(self, cycle):
        self.data[cycle.cycle_id] = cycle

    def read(self, cycle_id):
        return self.data.get(cycle_id)

    def update(self, cycle):
        self.data[cycle.cycle_id] = cycle

    def list_all(self):
        return list(self.data.values())


class TestReviewCycleService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryReviewCycleRepository()
        self.service = ReviewCycleService(self.repo)

    def test_start_cycle_creates_new_cycle(self):
        self.service.start_cycle("C1", "Reviewer1", "Quarterly Review")
        cycle = self.repo.read("C1")
        self.assertEqual(cycle.status, "In Progress")
        self.assertIsInstance(cycle.started_at, datetime)

    def test_start_cycle_duplicate_raises_error(self):
        self.service.start_cycle("C1", "Reviewer1", "Quarterly Review")
        with self.assertRaises(ValueError):
            self.service.start_cycle("C1", "Reviewer2", "Another Review")

    def test_complete_cycle_marks_as_completed(self):
        self.service.start_cycle("C2", "Reviewer1", "Monthly Review")
        self.service.complete_cycle("C2")
        cycle = self.repo.read("C2")
        self.assertEqual(cycle.status, "Completed")
        self.assertIsNotNone(cycle.completed_at)

    def test_complete_cycle_invalid_status_raises_error(self):
        self.service.start_cycle("C3", "Reviewer1", "Monthly Review")
        cycle = self.repo.read("C3")
        cycle.status = "Completed"  # Manually set
        self.repo.update(cycle)
        with self.assertRaises(ValueError):
            self.service.complete_cycle("C3")

    def test_list_active_cycles_only_returns_in_progress(self):
        self.service.start_cycle("C4", "Reviewer1", "Active Review")
        self.service.start_cycle("C5", "Reviewer2", "To be Completed")
        self.service.complete_cycle("C5")
        active = self.service.list_active_cycles()
        self.assertEqual(len(active), 1)
        self.assertEqual(active[0].cycle_id, "C4")
