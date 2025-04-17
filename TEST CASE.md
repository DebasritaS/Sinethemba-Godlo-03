# 1. TEST CASE

|Test Case ID	 |Test Case Name         |	Description                                                |	Preconditions	                                        |Test Steps	                            | Expected Result |	Status|
--------------|-----------------------|------------------------------------------------------------| -------------------------------------------------------|----------------------------------------|-----------------|-------|
|TC-01	      |Schedule Access Review	| Verify that an admin can schedule a periodic access review.|	The admin is logged in with scheduling permissions.   |	1. Navigate to the Review Schedule section. 2. Select start date, frequency, and scope. 3. Click Schedule Review.	| The review cycle is scheduled and appears in the review dashboard.|	Pending |
|TC-02	|Assign Reviewers |	Ensure that reviewers can be assigned to access review tasks. |	A review cycle exists, and the admin has assigned permissions.	| 1. Open the Review Assignment page. 2. Select a review cycle. 3. Assign reviewers to respective tasks. 4. Save changes. | Assigned reviewers receive notifications, and assignments appear in the system. |	Pending |
|TC-03	| Approve Access Request | Validate that a reviewer can approve an access request.	| The review cycle is active, and the reviewer has tasks assigned.	| 1. The reviewer logs into the system. 2. Opens the assigned access request. 3. Selects approve and submits the decision.	| Request status updates to Approved, and logs reflect the decision.	| Pending |
|TC-04 |	Reject Access Request	|Validate that a reviewer can reject an access request.	| The review cycle is active, and the reviewer has tasks assigned. |	1. The reviewer logs into the system. 2. Opens the assigned access request. 3. Selects Reject, optionally provides a reason, and submits.	|Request status updates to Rejected, logs reflect the decision, and auto-revocation is triggered (if applicable).	| Pending |
|TC-05	| Generate Compliance Reports |	Ensure compliance reports are generated correctly.	| The admin or auditor has report access.	| 1. Navigate to the Reports section. 2. Select the report type (e.g., user access history). 3. Choose a date range. 4. Click Generate Report.	| The system generates a report with correct user access details.	| Pending|
|TC-06	| Auto-Revoke Unapproved Access	| Verify that unapproved access is revoked after the review deadline. |	Unreviewed access requests exist, and the deadline has passed. |	1. Let the review cycle reach the deadline. 2. The system runs auto-revocation logic.	|Unreviewed access is revoked, and the system logs the event.	| Pending |
|TC-07	|Integration with IAM & HR Systems	| Validate that the system integrates with IAM/HR systems.	|IAM and HR integrations are enabled.	|1. The system fetches user access details from IAM. 2. The system verifies employment status via HR.	|Access review pulls correct user roles and employment status.|	Pending|
|TC-08	|User Appeals Rejected Request |	Ensure users can appeal rejected access requests.	| A rejected access request exists.	| 1. User logs into the system. 2. Opens the Rejected Requests section. 3. Submit an appeal with justification.	|Appeal status updates to Pending Review, and the reviewer gets notified.	|Pending|



# 2. NON-FUNCTIONAL TEST SCENARIOS
## Perfomance Test Scenario

Test Objective: Ensure the system can handle high user load and process access reviews efficiently.

Scenario: 

- Create 500 concurrent users log in and review access requests.
  
- Measure response timer for:
  
      - Loading the dashboard
  
      - Approving/rejecting access requests
  
      - Generating compliance reports
  
- Validating that the system latency remains below 2 seconds per action.

Expect Results:

- The system should not exceed 2 seconds response time under load.
  
- No timeout errors or system crashes should occur.

## Security Test Scenario

Test Objective: Validate system security against unauthorized access and data breaches.

Scenario:

- Perform access testing by attemping to:
  
      - Do SQL Injection in access review queries.
  
      - Unauthorised access to another user's access review tasks.
  
      - API calls for forged authentication tokens.
  
- Check if security policies enforce:
  
      - Role-based access control (RBAC)
  
      - Data encryption for stored and transmitted information
  
Expected Results

- System prevents SQL injection attempts
  
- Unauthorized users cannot access the restricted review tasks.
  
- Encrypted data cannot be decrypted without proper access.

