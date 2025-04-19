import unittest
from src.notification_service import NotificationService
from user import User

class TestNotificationService(unittest.TestCase):
    def test_send_notification(self):
        notifier = NotificationService()
        user = User(5, "Grace", "grace@example.com", ["User"])
        result = notifier.send_notification(user, "Test Message")
        self.assertTrue("Test Message" in result)
