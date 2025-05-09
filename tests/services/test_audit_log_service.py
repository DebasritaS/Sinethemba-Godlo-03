import unittest
from datetime import datetime
from src.services.audit_log_service import AuditLogService
from src.models.audit_log import AuditLog


class InMemoryAuditLogRepository:
    def __init__(self):
        self.logs = []
        self._id = 0

    def generate_id(self):
        self._id += 1
        return f"log_{self._id}"

    def create(self, log):
        self.logs.append(log)

    def list_by_user(self, user_id):
        return [log for log in self.logs if log.user_id == user_id]

    def list_all(self):
        return self.logs


class TestAuditLogService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryAuditLogRepository()
        self.service = AuditLogService(self.repo)

    def test_log_action_creates_log_entry(self):
        self.service.log_action("U1", "APPROVED", "AccessRequest123")
        logs = self.repo.list_all()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0].action, "APPROVED")
        self.assertIsInstance(logs[0].timestamp, datetime)

    def test_list_logs_for_user_filters_correctly(self):
        self.service.log_action("U1", "APPROVED", "Req1")
        self.service.log_action("U2", "REJECTED", "Req2")
        self.service.log_action("U1", "DELETED", "Req3")
        logs = self.service.list_logs_for_user("U1")
        self.assertEqual(len(logs), 2)
        self.assertTrue(all(log.user_id == "U1" for log in logs))

if __name__ == "__main__":
    unittest.main()