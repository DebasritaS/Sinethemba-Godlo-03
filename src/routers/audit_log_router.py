from fastapi import APIRouter
from src.services.audit_log_service import AuditLogService
from src.repositories.audit_log_repository import AuditLogRepository

router = APIRouter()
service = AuditLogService(AuditLogRepository())

@router.post("/")
def log_action(user_id: str, action: str, entity: str):
    log = service.log_action(user_id, action, entity)
    return log

@router.get("/user/{user_id}")
def get_user_logs(user_id: str):
    return service.list_logs_for_user(user_id)

@router.get("/")
def get_all_logs():
    return service.repository.list_all()
