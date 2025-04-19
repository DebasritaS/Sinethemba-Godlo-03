# factory_method.py

class User:
    def __init__(self, role):
        self.role = role

    def get_permissions(self):
        if self.role == "admin":
            return ["read", "write", "delete"]
        return ["read"]

def user_factory(role):
    return User(role)
