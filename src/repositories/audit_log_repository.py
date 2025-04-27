from src.audit_log import AuditLog

class AuditLogRepository(Repository[AuditLog, int], ABC):
    pass
