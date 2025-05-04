from src.models.user import User
from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_id: str, name: str, email: str, roles: list[str]):
        if self.user_repo.read(user_id):
            raise ValueError(f"User with ID {user_id} already exists.")

        if not email or "@" not in email:
            raise ValueError("Invalid email address.")

        user = User(user_id=user_id, name=name, email=email, roles=roles)
        self.user_repo.create(user)

    def get_user(self, user_id: str) -> User:
        user = self.user_repo.read(user_id)
        if not user:
            raise KeyError(f"User with ID {user_id} not found.")
        return user

    def update_user_email(self, user_id: str, new_email: str):
        user = self.get_user(user_id)
        if not new_email or "@" not in new_email:
            raise ValueError("Invalid email address.")
        user.email = new_email
        self.user_repo.update(user)

    def delete_user(self, user_id: str):
        self.user_repo.delete(user_id)
