
C4Context
  title Automated User Access Review - Context Diagram

  Person(admin, "IT Manager / Security Officer", "Reviews and approves access requests")
  Person(user, "Employee", "Requests access to systems")
  System(System, "Automated User Access Review", "Manages access reviews and approvals")

  System_Ext(IdP, "Identity Provider (LDAP, AD, Okta)", "Manages authentication and user roles")
  System_Ext(Email, "Notification Service", "Sends email/SMS alerts")
  System_Ext(HRSystem, "HR System", "Provides employee roles for validation")

  admin -> System : "Reviews & Approves Access"
  user -> System: "Requests Access"
  System -> IdP: "Syncs User Roles & Permissions"
  System -> Email: "Sends Notifications"
  System -> HRSystem: "Validates Employee Roles"


C4Container
  title Automated User Access Review - Container Diagram

  Person(admin, "IT Manager / Security Officer")
  System_Boundary(App, "Automated User Access Review") {
    Container(Frontend, "Web App (React/Vue)", "User Interface for Access Reviews")
    Container(Backend, "Backend API (Node.js/Express)", "Manages business logic and integrations")
    ContainerDb(Database, "PostgreSQL/MongoDB", "Stores access records, logs, and reviews")
    Container(Notification, "Notification Service", "Sends review alerts via email/SMS")
  }

  System_Ext(IdP, "Identity Provider (LDAP, AD, Okta)")
  System_Ext(HRSystem, "HR System")

  admin -> Frontend : "Access Review Actions"
  Frontend -> Backend : "API Calls (REST/GraphQL)"
  Backend -> Database : "Stores Access Review Data"
  Backend -> Notification : "Triggers Review Notifications"
  Backend -> IdP : "Syncs User Roles"
  Backend -> HRSystem : "Fetches Employee Role Data"

C4Component
  title Automated User Access Review - Component Diagram

  Container_Boundary(Backend, "Backend API (Node.js/Express)") {
    Component(AuthModule, "Authentication Module", "Handles OAuth2, SAML, JWT")
    Component(AccessReviewEngine, "Access Review Engine", "Generates periodic review tasks")
    Component(ApprovalWorkflow, "Approval Workflow", "Ensures manual approval before revocation")
    Component(NotificationService, "Notification Service", "Sends alerts & reminders")
    Component(IntegrationLayer, "Integration Layer", "Handles LDAP, HR System, Notifications")
  }

  AuthModule -> AccessReviewEngine : "Validates User Authentication"
  AccessReviewEngine -> ApprovalWorkflow : "Assigns review tasks to managers"
  ApprovalWorkflow -> NotificationService : "Triggers alerts for pending approvals"
  IntegrationLayer -> AccessReviewEngine : "Syncs Data from LDAP & HR System"
  NotificationService -> IntegrationLayer : "Sends Emails & SMS"

