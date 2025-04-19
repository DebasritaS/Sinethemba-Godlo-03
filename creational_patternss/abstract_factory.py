# abstract_factory.py

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.role} named {self.name}"


# Abstract Factory Interface
class UserFactory:
    def create_user(self, name):
        raise NotImplementedError


# Concrete Factory for Reviewer
class ReviewerFactory(UserFactory):
    def create_user(self, name):
        return User(name, "Reviewer")


# Concrete Factory for Manager
class ManagerFactory(UserFactory):
    def create_user(self, name):
        return User(name, "Manager")

class AbstractUserFactory:
    def create_user(self, name):
        pass

    def create_notification(self):
        pass

class ReviewerFactory(AbstractUserFactory):
    def create_user(self, name):
        return Reviewer(name)

    def create_notification(self):
        return ReviewerNotification()


class ManagerFactory(AbstractUserFactory):
    def create_user(self, name):
        return Manager(name)

    def create_notification(self):
        return ManagerNotification()

class ReviewerNotification:
    def send(self):
        return "Sending reviewer-specific notification."


class ManagerNotification:
    def send(self):
        return "Sending manager-specific notification."

# Import the classes if they're in separate files, or define them here
class Reviewer:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "Reviewer"


class Manager:
    def __init__(self, name):
        self.name = name

    def role(self):
        return "Manager"


class AbstractUserFactory:
    def create_user(self, name):
        pass

    def create_notification(self):
        pass


class ReviewerFactory(AbstractUserFactory):
    def create_user(self, name):
        return Reviewer(name)

    def create_notification(self):
        return ReviewerNotification()


class ManagerFactory(AbstractUserFactory):
    def create_user(self, name):
        return Manager(name)

    def create_notification(self):
        return ManagerNotification()


# Define the Notification classes as needed
class ReviewerNotification:
    def send(self):
        return "Sending reviewer-specific notification."


class ManagerNotification:
    def send(self):
        return "Sending manager-specific notification."

