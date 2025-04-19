class AuditLogger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(AuditLogger, cls).__new__(cls)
            cls.__instance.logs = []
        return cls.__instance

    def log(self, entry):
        self.logs.append(entry)

    def get_logs(self):
        return self.logs

# Usage
logger1 = AuditLogger()
logger2 = AuditLogger()
logger1.log("Access approved for user 101")
print(logger2.get_logs())  # Shared instance