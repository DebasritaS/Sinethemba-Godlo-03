class NotificationService:
    def send_notification(self, user, message):
        print(f"Notification to {user.get_name()} ({user.get_user_id()}): {message}")