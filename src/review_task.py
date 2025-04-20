class ReviewTask:
    def __init__(self, task_id, access_request, reviewer):
        self.task_id = task_id
        self.access_request = access_request
        self.reviewer = reviewer
        self.is_approved = None  # Assume the task starts as not approved

    def approve(self):
        self.is_approved = True

    def reject(self):
        self.is_approved = False
