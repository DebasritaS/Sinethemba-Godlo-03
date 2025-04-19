import unittest
from src.review_cycle import ReviewCycle
from datetime import datetime, timedelta

class TestReviewCycle(unittest.TestCase):
    def test_add_and_close_cycle(self):
        start = datetime.now()
        end = start + timedelta(days=30)
        cycle = ReviewCycle("Q1", start, end)
        self.assertEqual(cycle.get_status(), "Open")
        cycle.close()
        self.assertEqual(cycle.get_status(), "Closed")
