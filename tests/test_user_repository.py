import unittest
from src.repositories.in_memory_user_repository import InMemoryUserRepository
from src.models.user import User



class TestInMemoryUserRepository(unittest.TestCase):

    def setUp(self):
        self.repo = InMemoryUserRepository()

    def test_create_and_read_user(self):
        user = User(user_id="1", name="Alice", email="alice@example.com", roles=["Admin"])
        self.repo.create(user)
        retrieved = self.repo.read("1")
        self.assertEqual(retrieved.name, "Alice")
        self.assertEqual(retrieved.email, "alice@example.com")

    def test_update_user(self):
        user = User(user_id="2", name="Bob", email="bob@example.com", roles=["User"])
        self.repo.create(user)
        user.name = "Robert"
        self.repo.update(user)
        updated_user = self.repo.read("2")
        self.assertEqual(updated_user.name, "Robert")

    def test_delete_user(self):
        user = User(user_id="3", name="Charlie", email="charlie@example.com", roles=["Guest"])
        self.repo.create(user)
        self.repo.delete("3")
        with self.assertRaises(KeyError):
            self.repo.read("3")

    def test_read_nonexistent_user(self):
        with self.assertRaises(KeyError):
            self.repo.read("nonexistent-id")

if __name__ == "__main__":
    unittest.main()

