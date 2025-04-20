import unittest
from src.review_task import ReviewTask
from src.access_request import AccessRequest
from src.user import User
from datetime import datetime

class TestReviewTask(unittest.TestCase):
    def test_review_approval(self):        
        task_id = 1  
        reviewer = User(1, "Reviewer", "reviewer@example.com", ["Manager"])
        access_request = AccessRequest(1, reviewer, "Admin Panel", "2024-04-17")  
        task = ReviewTask(task_id, access_request, reviewer)
        task.approve()
        self.assertTrue(task.is_approved)  

    def test_review_rejection(self):
        task_id = 1  
        reviewer = User(1, "Reviewer", "reviewer@example.com", ["Manager"])
        access_request = AccessRequest(1, reviewer, "Admin Panel", "2024-04-17") 
        task = ReviewTask(task_id, access_request, reviewer)
        task.reject()
        self.assertFalse(task.is_approved) 
