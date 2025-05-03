from src.models.audit_log import AuditLog
from src.repositories.audit_log_repository import AuditLogRepository
from datetime import datetime
from typing import List


class AuditLogService:
    def __init__(self, audit_repo: AuditLogRepository):
        self.audit_repo = audit_repo

    def log_action(self, user_id: str, action: str, target: str):
        log = AuditLog(
            log_id=self.audit_repo.generate_id(),
            user_id=user_id,
            action=action,
            target=target,
            timestamp=datetime.now()
        )
        self.audit_repo.create(log)

    def list_logs_for_user(self, user_id: str) -> List[AuditLog]:
        return self.audit_repo.list_by_user(user_id)

    def list_all_logs(self) -> List[AuditLog]:
        return self.audit_repo.list_all()
