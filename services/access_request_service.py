from src.models.access_request import AccessRequest
from src.repositories.access_request_repository import AccessRequestRepository
from datetime import datetime


class AccessRequestService:
    def __init__(self, request_repo: AccessRequestRepository):
        self.request_repo = request_repo

    def submit_request(self, request_id: str, user_id: str, resource: str, reason: str):
        if self.request_repo.read(request_id):
            raise ValueError(f"Request ID {request_id} already exists.")

        if not resource or not reason:
            raise ValueError("Resource and reason are required.")

        request = AccessRequest(
            request_id=request_id,
            user_id=user_id,
            resource=resource,
            reason=reason,
            status="Pending",
            submitted_at=datetime.now()
        )
        self.request_repo.create(request)

    def approve_request(self, request_id: str, approver_id: str):
        request = self.request_repo.read(request_id)
        if not request:
            raise KeyError(f"Request ID {request_id} not found.")
        if request.status != "Pending":
            raise ValueError("Only pending requests can be approved.")
        
        request.status = "Approved"
        request.approved_by = approver_id
        request.approved_at = datetime.now()
        self.request_repo.update(request)

    def reject_request(self, request_id: str, approver_id: str, reason: str):
        request = self.request_repo.read(request_id)
        if not request:
            raise KeyError(f"Request ID {request_id} not found.")
        if request.status != "Pending":
            raise ValueError("Only pending requests can be rejected.")

        request.status = "Rejected"
        request.approved_by = approver_id
        request.approved_at = datetime.now()
        request.rejection_reason = reason
        self.request_repo.update(request)

    def get_request(self, request_id: str) -> AccessRequest:
        return self.request_repo.read(request_id)

    def list_requests_by_user(self, user_id: str) -> list[AccessRequest]:
        return self.request_repo.list_by_user(user_id)
