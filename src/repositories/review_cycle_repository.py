from src.review_cycle import ReviewCycle

class ReviewCycleRepository(Repository[ReviewCycle, int], ABC):
    pass
