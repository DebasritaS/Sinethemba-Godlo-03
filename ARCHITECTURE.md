C4Context
  title Automated User Access Review System - System Context Diagram
    Person(admin, "Security Administrator", "Manages user access reviews, generates reports, and configures the system.")
     Person(manager, "Line Manager", "Reviews and approves/revokes user access for their team members.")
    System(accessReviewSystem, "Automated User Access Review System", "Automates the process of user access review and certification.")
    System_Ext(identityProvider, "Identity Provider (IdP)", "Manages user identities and authentication (e.g., Azure AD, Okta).")
    System_Ext(resourceSystem, "Resource System", "Systems containing resources with user access (e.g., File Servers, Databases, Applications).")
    System_Ext(auditLog, "Audit Log System", "Stores audit logs of user access and review activities.")

    Rel(admin, accessReviewSystem, "Configures, Manages, and Generates Reports")
    Rel(manager, accessReviewSystem, "Reviews and Approves/Revokes Access")
    Rel(accessReviewSystem, identityProvider, "Retrieves User Information")
    Rel(accessReviewSystem, resourceSystem, "Retrieves Access Permissions")
    Rel(accessReviewSystem, auditLog, "Stores Audit Logs")

C4Container
    title Automated User Access Review System - Containers Diagram

    Container(webApp, "Web Application", "Provides the user interface for administrators and managers.", "Angular/React")
    Container(api, "API", "Handles business logic and data processing.", "Node.js/Python Flask/Django")
    ContainerDb(database, "Database", "Stores user access data, review configurations, and audit trails.", "PostgreSQL/MySQL")
    Container(accessSync, "Access Sync Service", "Synchronizes user access data from resource systems and IdP.", "Java/Go")
    Container(notificationService, "Notification Service", "Sends email notifications for review tasks and approvals.", "Python/Node.js")
    Container(reportGenerator, "Report Generator", "Generates access review reports.", "Python/Java")

    Rel(webApp, api, "API Calls")
    Rel(api, database, "Reads/Writes Data")
    Rel(accessSync, database, "Writes Data")
    Rel(accessSync, identityProvider, "Retrieves User Data")
    Rel(accessSync, resourceSystem, "Retrieves Access Data")
    Rel(api, accessSync, "Triggers Synchronization")
    Rel(api, notificationService, "Sends Notifications")
    Rel(api, reportGenerator, "Generates Reports")
    Rel(reportGenerator, database, "Reads Data")
    Rel(api, auditLog, "Writes Audit Logs")

C4Component
    title Automated User Access Review System - API Components Diagram

    Container(api, "API", "Handles business logic and data processing.", "Node.js/Python (Flask/Django)")

    Component(userManagement, "User Management", "Handles user authentication and authorization.", "API")
    Component(reviewManagement, "Review Management", "Manages access review workflows.", "API")
    Component(accessData, "Access Data Service", "Retrieves and processes user access data.", "API")
    Component(notificationAdapter, "Notification Adapter", "Adapts to the notification service.", "API")
    Component(reportAdapter, "Report Adapter", "Adapts to the report generation service.", "API")
    Component(auditLogAdapter, "Audit Log Adapter", "Adapts to the audit log service.", "API")

    Rel(api, userManagement, "Uses")
    Rel(api, reviewManagement, "Uses")
    Rel(api, accessData, "Uses")
    Rel(api, notificationAdapter, "Uses")
    Rel(api, reportAdapter, "Uses")
    Rel(api, auditLogAdapter, "Uses")

    ContainerDb(database, "Database", "Stores user access data, review configurations, and audit trails.", "PostgreSQL/MySQL")
    Rel(accessData, database, "Reads Data")
    Rel(reviewManagement, database, "Reads/Writes Data")
    Rel(userManagement, database, "Reads Data")
    Rel(auditLogAdapter, auditLog, "Writes Audit Logs")
    Rel(reportAdapter, reportGenerator, "Generates Reports")
    Rel(notificationAdapter, notificationService, "Sends Notifications")
