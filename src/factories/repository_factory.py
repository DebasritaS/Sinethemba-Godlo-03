from src.repositories.user_repository import UserRepository
from src.repositories.access_request_repository import AccessRequestRepository
from src.repositories.review_task_repository import ReviewTaskRepository
from src.repositories.review_cycle_repository import ReviewCycleRepository
from src.repositories.audit_log_repository import AuditLogRepository

class RepositoryFactory:
    @staticmethod
    def get_user_repository():
        return UserRepository()

    @staticmethod
    def get_access_request_repository():
        return AccessRequestRepository()

    @staticmethod
    def get_review_task_repository():
        return ReviewTaskRepository()

    @staticmethod
    def get_review_cycle_repository():
        return ReviewCycleRepository()

    @staticmethod
    def get_audit_log_repository():
        return AuditLogRepository()
        
    elif backend == 'sql':
    return SQLUserRepository(db_path="users.db") 