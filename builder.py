# builder.py

class ReviewTask:
    def __init__(self, reviewer, user, resource):
        self.reviewer = reviewer
        self.user = user
        self.resource = resource

    def display(self):
        print(f"Reviewer: {self.reviewer}, User: {self.user}, Resource: {self.resource}")

class ReviewTaskBuilder:
    def __init__(self):
        self._reviewer = None
        self._user = None
        self._resource = None

    def set_reviewer(self, reviewer):
        self._reviewer = reviewer
        return self

    def add_user(self, user):
        self._user = user
        return self

    def add_resource(self, resource):
        self._resource = resource
        return self

    def build(self):
        return ReviewTask(self._reviewer, self._user, self._resource)
