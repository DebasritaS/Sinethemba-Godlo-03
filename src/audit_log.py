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
