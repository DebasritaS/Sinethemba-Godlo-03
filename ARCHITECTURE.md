
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

