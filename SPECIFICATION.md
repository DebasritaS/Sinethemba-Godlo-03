# Automated User Access Review System

## Domain

The system operates within the domain of Identity and Access Management (IAM), focusing on compliance and security governance. It is designed for organisations that require periodic access reviews (which can be done Monthly, Quarterly, or Half-yearly) to ensure that users have the right access permissions based on their roles and responsibilities. The system will integrate with existing user directories, role-based access controls (RBAC), and approval workflows to facilitate efficient and accountable access management.

## Problem Statement

It is difficult for organizations to maintain secure and compliant access control because of a manual, inconsistent, and time-consuming review process. Not having an automated method increases the risk of outdated user permissions, which could lead to security vulnerabilities, violations of compliance, and operational inefficiencies. Additionally, staff movement is a major issue, as users will retain access to their previous roles and responsibilities.

### The Automated User Access Review System aims to:
- **Streamline** access reviews through automation.
- **Ensure compliance** with security policies and regulations.
- **Reduce administrative overhead** by providing scheduled and ad-hoc access reviews.
- **Enhance security** by enforcing periodic reviews and requiring managerial approvals for revocations.
- **Improve visibility and reporting** with comprehensive logs and dashboards.

## Individual Scope and Feasibility Justification

The system is feasible due to the following factors:

### Technical Viability:
- Built as a full-stack web application using a scalable architecture.
- Utilizes Node.js (Express) for the backend and a modern frontend framework (React/Vue).
- Stores and processes data using a relational or document-based database (PostgreSQL/MongoDB).
- It implements secure authentication and authorization with OAuth2, SAML, or JWT.

### Business Justification:
- Reducing the risk of security breaches due to outdated permissions.
- It saves time and cost by automating periodic access reviews.
- Meets compliance standards (e.g., ISO 27001, SOC 2, GDPR) required by many organizations.

### Operational Feasibility:
- It integrates with existing user management systems (Active Directory, Okta, LDAP, etc.).
- It provides customizable workflows to match different organizational needs.
- Send notifications and alerts to ensure timely reviews and approvals.

This system ensures better security, compliance, and efficiency while keeping managerial control over access revocations to prevent unintended disruptions.
