from abc import ABC
from src.models.entities.audit_log import AuditLog
from src.repositories.repository import Repository  # Ensure this exists

class AuditLogRepository(Repository[AuditLog, int], ABC):
    pass