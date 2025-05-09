from datetime import datetime

from pydantic import BaseModel

class AuditLog(BaseModel):
    log_id: str
    action: str
    timestamp: str
    user_id: str
    details: str

 
class AuditLog:
    def __init__(self, id: int, action: str, actor: str, timestamp: datetime, details: str):
        self.id = id
        self.action = action
        self.actor = actor
        self.timestamp = timestamp
        self.details = details