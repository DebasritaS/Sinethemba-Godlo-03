import unittest
from src.review_task import ReviewTask
from src.access_request import AccessRequest
from src.user import User
from datetime import datetime

class TestReviewTask(unittest.TestCase):
    def test_review_approval(self):
        user = User(1, "Dave", "dave@example.com", ["Reviewer"])
        access = AccessRequest(1002, user, "App", datetime.now())
        task = ReviewTask(user, access)
        task.review(approve=True)
        self.assertEqual(access.get_status(), "Approved")

    def test_review_rejection(self):
        user = User(2, "Emma", "emma@example.com", ["Reviewer"])
        access = AccessRequest(1003, user, "Server", datetime.now())
        task = ReviewTask(user, access)
        task.review(approve=False)
        self.assertEqual(access.get_status(), "Rejected")
