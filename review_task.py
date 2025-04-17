class ReviewTask:
    def __init__(self, task_id, reviewer, access_request):
        self.__task_id = task_id
        self.__reviewer = reviewer  # Association to User
        self.access_request = access_request # Association to AccessRequest
 

    def review(self, approve=True):
        if approve:
            self.access_request.approve()
        else:
            self.access_request.reject()