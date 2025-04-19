import unittest
from src.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(1001, "Alice", "alice@example.com", ["Reviewer"])
        self.assertEqual(user.get_user_id(), 1)
        self.assertIn("Reviewer", user.get_roles())

    def test_assign_role(self):
        user = User(2, "Bob", "bob@example.com", [])
        user.assign_role("Manager")
        self.assertIn("Manager", user.get_roles())

    def test_remove_role(self):
        user = User(3, "Carol", "carol@example.com", ["Reviewer"])
        user.remove_role("Reviewer")
        self.assertNotIn("Reviewer", user.get_roles())
