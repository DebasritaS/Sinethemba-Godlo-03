# Import all pattern files
from singleton import AuditLogger
from factory_method import user_factory
from builder import ReviewTaskBuilder
from prototype import ReviewTemplate
from abstract_factory import ReviewerFactory, ManagerFactory
from object_pool import ConnectionPool

# Singleton
logger = AuditLogger()
logger.log("System started")

# Factory Method
user = user_factory("manager")
print("User Role:", user.role)

# Builder
task = (ReviewTaskBuilder()
.set_reviewer("John")
.add_user("alice")
.add_resource("Database")
.build())
task.display()

# Prototype
template = ReviewTemplate("Quarterly Review", ["User", "Resource", "Status"])
template_cloned = template.clone()
print("Original:", template.name, template.fields)
print("Cloned:", template_cloned.name, template_cloned.fields)

# Abstract Factory
factory = ReviewerFactory()
print("\n=== Abstract Factory ===")
reviewer_factory = ReviewerFactory()
manager_factory = ManagerFactory()
reviewer = reviewer_factory.create_user("Alice")
manager = manager_factory.create_user("Bob")
reviewer_notification = reviewer_factory.create_notification()
manager_notification = manager_factory.create_notification()
print("Reviewer:", reviewer.role)
print("Manager:", manager.role)
print("Factory User:", factory.create_user("Alice"))
print("Manager:", manager_factory.create_user("Bob").role)
print("Notification Type:", type(reviewer_notification).__name__)
print("Notification Message:", reviewer_notification.send())

# Object Pool
pool = ConnectionPool(size=10)
# Acquire some connections
conn1 = pool.acquire()
conn2 = pool.acquire()
print("Acquired:", conn1.id, conn2.id)

# Release one connection back
pool.release(conn1)

# Re-acquire (should reuse)
conn3 = pool.acquire()
print("Reused:", conn3.id)