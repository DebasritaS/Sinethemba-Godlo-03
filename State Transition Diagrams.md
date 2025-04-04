# State Diagrams

---
State 1: Review Cycle
---

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Scheduled : Schedule Review
    Scheduled --> InProgress : Start Review
    InProgress --> Completed : All Tasks Completed
    Completed --> Archived : Archive Review
```

---
State 2: Review Task
---

```mermaid
stateDiagram-v2
    [*] --> Assigned
    Assigned --> InProgress : Reviewer Starts Task
    InProgress --> Approved : Approved by Reviewer
    InProgress --> Rejected : Rejected by Reviewer
    Approved --> Closed : Task Finalized
    Rejected --> Closed : Task Finalized
```

---
State 3: Reviewer Assignment
---
```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Assigned : Assigned to Reviewer
    Assigned --> Reassigned : Reassigned to New Reviewer
    Assigned --> Completed : Review Task Completed
```


---
State 4: Access Request
---
```mermaid
stateDiagram-v2
    [*] --> Submitted
    Submitted --> UnderReview : Reviewed by Approver
    UnderReview --> Approved : Access Granted
    UnderReview --> Rejected : Access Denied
    Approved --> Revoked : Auto-Revoked After Deadline
```




---
 State 5: Compliance Report
---
```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Generated : Report Generated
    Generated --> Approved : Approved by Auditor
    Approved --> Archived : Report Archived
```


---
State 6: User Access
---
```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> UnderReview : Review Process Initiated
    UnderReview --> Approved : Access Retained
    UnderReview --> Revoked : Access Revoked
```




---
State 7: Audit Log Entry
---
```mermaid
stateDiagram-v2
    [*] --> Logged
    Logged --> Reviewed : Auditor Reviews Log
    Reviewed --> Archived : Log Archived
```



---
State 8: System Alert
---

```mermaid
stateDiagram-v2
    [*] --> Triggered
    Triggered --> Acknowledged : Admin Acknowledges Alert
    Acknowledged --> Resolved : Issue Resolved

```



