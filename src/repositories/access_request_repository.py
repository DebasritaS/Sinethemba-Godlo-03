from src.access_request import AccessRequest

class AccessRequestRepository(Repository[AccessRequest, int], ABC):
    pass
