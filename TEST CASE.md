|Test Case ID	|Test Case Name         |	Description                                                |	Preconditions	                                        |Test Steps	                            | Expected Result |	Status |
----------------------------------------------------------------------------------------------------
|TC-01	      |Schedule Access Review	| Verify that an admin can schedule a periodic access review.|	The admin is logged in with scheduling permissions.   |	1. Navigate to Review Schedule section. 2. Select start date, frequency, and scope. 
3. Click Schedule Review.	Review cycle is scheduled and appears in the review dashboard.|	Pending |
---------------------------------------------------------------------------------------------------
|TC-02	|Assign Reviewers |	Ensure that reviewers can be assigned to access review tasks. |	A review cycle exists, and the admin has assign permissions.	| 1. Open Review Assignment page. 
2. Select a review cycle. 
3. Assign reviewers to respective tasks. 
4. Save changes.	Assigned reviewers receive notifications, and assignments appear in the system. |	Pending |
-------------------------------------------------------------------------------------------------------------
|TC-03	| Approve Access Request | Validate that a reviewer can approve an access request.	| Review cycle is active, and the reviewer has tasks assigned.	| 1. Reviewer logs into the system. 
2. Opens assigned access request. 
3. Selects Approve and submits the decision.	Request status updates to Approved, and logs reflect the decision.	| Pending |
-----------------------------------------------------------------------------------------------------------------------------
|TC-04 |	Reject Access Request	|Validate that a reviewer can reject an access request.	| Review cycle is active, and the reviewer has tasks assigned. |	1. Reviewer logs into the system. 
2. Opens assigned access request. 
3. Selects Reject, optionally provides a reason, and submits.	Request status updates to Rejected, logs reflect the decision, and auto-revocation is triggered (if applicable).	| Pending |
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|TC-05	| Generate Compliance Reports |	Ensure that compliance reports are generated correctly.	| Admin or auditor has report access.	| 1. Navigate to Reports section. 
2. Select report type (e.g., user access history). 
3. Choose a date range. 
4. Click Generate Report.	System generates a report with correct user access details.	| Pending|
------------------------------------------------------------------------------------------------
|TC-06	| Auto-Revoke Unapproved Access	| Verify that unapproved access is revoked after the review deadline. |	Unreviewed access requests exist, and the deadline has passed. |	1. Let the review cycle reach the deadline. 
2. System runs auto-revocation logic.	Unreviewed access is revoked, and the system logs the event.	| Pending |
---------------------------------------------------------------------------------------------------------------
|TC-07	|Integration with IAM & HR Systems	| Validate that the system integrates with IAM/HR systems.	|IAM and HR integrations are enabled.	|1. System fetches user access details from IAM. 
2. System verifies employment status via HR.	Access review pulls correct user roles and employment status.|	Pending|
---------------------------------------------------------------------------------------------------------------------
|TC-08	|User Appeals Rejected Request |	Ensure that users can appeal rejected access requests.	| A rejected access request exists.	| 1. User logs into the system. 
2. Opens Rejected Requests section. 
3. Submits an appeal with justification.	Appeal status updates to Pending Review, and reviewer gets notified.	Pending|
---------------------------------------------------------------------------------------------------------------------
