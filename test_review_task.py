import unittest
from src.review_task import ReviewTask
from src.access_request import AccessRequest
from src.user import User
from datetime import datetime

class TestReviewTask(unittest.TestCase):
    def test_review_approval(self):
        task_id = 1  # Define the task_id
        reviewer = User(1, "Reviewer")  # Assuming you have a User class
        access_request = AccessRequest(1, "Access Request")  # Define access_request
        task = ReviewTask(task_id, reviewer, access_request)
        self.assertEqual(task.status, "Pending")  # Example assertion

    def test_review_rejection(self):
        task_id = 1  # Define the task_id
        reviewer = User(1, "Reviewer")  # Assuming you have a User class
        access_request = AccessRequest(1, "Access Request")  # Define access_request
        task = ReviewTask(task_id, reviewer, access_request)
        self.assertEqual(task.status, "Rejected")  # Example assertion