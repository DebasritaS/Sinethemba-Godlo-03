from user import User
from access_request import AccessRequest
from review_task import ReviewTask
from review_cycle import ReviewCycle
from audit_log import AuditLog
from notification_service import NotificationService
from datetime import datetime

# Create instances
user = User(user_id=1, name="Alice", email="alice@example.com", roles=["Reviewer"])
print("User ID:", user.get_user_id())
print("Name:", user.get_name())
print("Email:", user.get_email())
print("Roles:", user.get_roles())
audit_log = AuditLog()
notifier = NotificationService()


# User requests access
user = User(1, "Alice", "alice@example.com", ["Reviewer"])
access_request = user.request_access(101, "Database")

print("Status:", access_request.get_status())

# Create access request
user = User(user_id=1, name="Nicole", email="godlosinethemba@gmail.com", roles=["Applicant"])

access_request = AccessRequest(
    request_id=101,
    user=user,
    resource="Database",
    date_requested=datetime.now()
)
access_request = user.request_access(101, "Database")

print("Access Request created:", access_request.get_status())

# Review process
reviewer = User(user_id=1, name="Bob", email="bob@example.com", roles=["Reviewer"])
access_request = AccessRequest(
    request_id=101,
    user=user,
    resource="Database",
    date_requested=datetime.now()
)

task = ReviewTask(task_id=1, reviewer=reviewer, access_request=access_request)
task = ReviewTask(1, reviewer, access_request)
task.review(approve=True)

audit_log = AuditLog()
audit_log.log("Some action happened.")
audit_log.log(f"{reviewer.get_name()} reviewed and approved the request")


# Notification
notifier.send_notification(user, f"Your access request to {access_request.get_resource()} was {access_request.get_status()}")
notifier = NotificationService()
notifier.send_notification(user, "Your access has been granted.")

# Review cycle
start_date = datetime(2025, 4, 1)
end_date = datetime(2025, 6, 30)
cycle = ReviewCycle("Quarterly", start_date, end_date)
cycle.add_task(task)
