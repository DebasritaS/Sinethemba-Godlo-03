# User Case Specifications
## Use Case: Approve/Reject Access
### Description: 
This use case describes how a Manager/HOD or Access Owners (Reviewers) evaluate user access rights and either approve or reject access to specific resources based on compliance policies and business needs.

**System Actors are:**

**Manager/Head of Department**

**Access Owners (Reviewers)**

**Identity and Access Management (IAM) Team**

**Risk Management Team**

### Preconditions

- The user’s access request must be part of an active review cycle.
- The system must have the latest access details from the IAM and HR Systems.
- The assigned Manager/Head of Department or Access Owners (Reviewers) must have permission to review the user’s access.
- The review process must adhere to compliance policies.

### Postconditions

- If the access is approved, the user retains their access to the resource.
- If the access is rejected, the system will trigger an automated access revocation (or queue it for manager approval if required).
- System logs help with the decision for audit and compliance tracking.
- The reviewer and user will receive a notification (by email) about the decision of the access to the resource.

### Basic Flow (Happy Path):
1.	The system notifies the assigned Manager/Head of Department or Access Owners (Reviewers) that a review task is pending.
2.	Reviewer logs into the Review Management Dashboard.
3.	The **reviewer** views the list of access requests, including details such as:
   
 - User identity
 - Current roles and permissions
 - Last access date
 - Risk indicators (e.g., inactive accounts, policy violations, resigned users)
4.	The Reviewer selects an access request and elects to either:
   
 - Approve (user retains access)
 - Reject (user access is revoked or queued for revocation)
5.	The system records the decision in the audit logs.
6.	The system sends a confirmation notification to the user and relevant stakeholders.
7.	The system updates the access control records.

### Alternative Flows
**A1: Insufficient Information for Decision**

**1.	Condition: The reviewer requires more information before making a final decision.**

**2.	Flow:**
- The Reviewer requests additional justification from the End User.
- The System notifies the End User and updates the request status to “pending justification”.
- Once justification is received, the reviewer resumes the review process.
  
**A2: User Appeals a Rejected Access Request**

**1.	Condition: The end User disagrees with the rejection of his/her access and files for an appeal.**

**2.	Flow:**
- The User submits an appeal through the system.
- The Manager/Head of Department or Access Owners (Reviewers) receive notification and re-evaluate requests.
- The IAM Team or Risk Management Team may conduct an additional risk assessment.
- A final decision is made and recorded in the system.

**A3: Auto-Revoke After Timeout**

**1.	Condition: The Reviewer does not act (Approve or reject) within the specified review period.**

**2.	Flow:**
- The System sends periodic reminders to the Reviewer.
- If no action is taken by the Review and the deadline is reached, the system automatically rejects the access.
- The decision is logged, and a notification is sent to the relevant stakeholders.
