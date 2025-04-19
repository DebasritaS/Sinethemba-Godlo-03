import unittest
from src.access_request import AccessRequest, AccessStatus
from user import User
from datetime import datetime

class TestAccessRequest(unittest.TestCase):
    def setUp(self):
        self.user = User(1001, "Alice", "alice@example.com", ["User"])
        self.request = AccessRequest(1001, self.user, "Database", datetime.now())

    def test_initial_status(self):
        self.assertEqual(self.request.get_status(), "Pending")

    def test_approve(self):
        self.request.approve()
        self.assertEqual(self.request.get_status(), "Approved")

    def test_invalid_status_change(self):
        self.request.reject()
        self.request.revoke()
        self.assertEqual(self.request.get_status(), "Revoked")  # Should be latest

