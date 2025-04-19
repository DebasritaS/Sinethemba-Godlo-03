class AuditLog:
    def __init__(self):
        self.__entries = []

    def log_action(self, user, action, target, timestamp):
        entry = {
            'user': user.get_user_id(),
            'action': action,
            'target': target,
            'timestamp': timestamp
        }
        self.__entries.append(entry)

    def get_logs(self):
        return self.__entries
    
    def log(self, entry):
        self._entries.append(entry)

    def get_entries(self):
        return self._entries


class AuditLog:
    def __init__(self):
        self.entries = []  # Initialize the list to store log messages

    def log(self, message):
        self.entries.append(message)
        print(f"Audit Log: {message}")


   