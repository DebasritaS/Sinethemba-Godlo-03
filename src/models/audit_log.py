from datetime import datetime


class AuditLog:
    def __init__(self, id: int, action: str, actor: str, timestamp: datetime, details: str):
        self.id = id
        self.action = action
        self.actor = actor
        self.timestamp = timestamp
        self.details = details