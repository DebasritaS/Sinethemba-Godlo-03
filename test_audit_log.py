import unittest
from src.audit_log import AuditLog

class TestAuditLog(unittest.TestCase):
    def test_log_entry(self):
        log = AuditLog()
        log.log("User reviewed request")
        self.assertIn("User reviewed request", log.get_entries())
