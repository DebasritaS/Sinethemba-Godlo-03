from src.review_task import ReviewTask

class ReviewTaskRepository(Repository[ReviewTask, int], ABC):
    pass
