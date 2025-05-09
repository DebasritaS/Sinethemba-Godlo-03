from datetime import datetime

# This is the data model used in services and tests
class AuditLog:
    def __init__(self, log_id: str, user_id: str, action: str, resource_id: str, timestamp: datetime):
        self.log_id = log_id
        self.user_id = user_id
        self.action = action
        self.resource_id = resource_id
        self.timestamp = timestamp


class AuditLog:
    def __init__(self):
        self._entries = []

    def log(self, message):
        
        self._entries.append(message)
        print(f"Audit Log: {message}")

    def log_action(self, user, action, target, timestamp):
        
        entry = {
            'user': user.get_user_id(),
            'action': action,
            'target': target,
            'timestamp': timestamp
        }
        self._entries.append(entry)

    def get_entries(self):
        return self._entries
