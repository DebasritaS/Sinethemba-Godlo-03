# Activity Diagrams


---
Workflow 1: Schedule Access Review Cycle
---
```mermaid
flowchart TD
    A([Start]) --> B[Admin selects schedule parameters]
    B --> C{Valid schedule?}
    C -- Yes --> D[Create new ReviewCycle]
    C -- No --> E[Display error to Admin]
    D --> F[Notify relevant Managers]
    F --> G([End])
    E --> G

```
---
Workflow 2: Assign Reviewer to Task
---

```mermaid
flowchart TD
    A([Start]) --> B[Manager selects access items]
    B --> C[Choose reviewers]
    C --> D{Reviewer availability?}
    D -- Yes --> E[Assign ReviewTask]
    D -- No --> F[Prompt alternative reviewer]
    E --> G([End])
    F --> G

```

---
Workflow 3: Access Review Execution
---
```mermaid
flowchart TD
    A([Start]) --> B[Reviewer opens task]
    B --> C[Review user access]
    C --> D{Is access justified?}
    D -- Yes --> E[Approve access]
    D -- No --> F[Reject access]
    E --> G([End])
    F --> G

```

---
Workflow 4: Auto-Revoke Unapproved Access
---
```mermaid
flowchart TD
    A([Start]) --> B[Check task deadlines]
    B --> C{Is task still pending?}
    C -- Yes --> D{Is deadline passed?}
    D -- Yes --> E[Revoke access automatically]
    E --> F([End])
    D -- No --> F
    C -- No --> F
```


Workflow 5: Generate Compliance Report
---
```mermaid
flowchart TD
    A([Start]) --> B[Auditor selects report criteria]
    B --> C[System gathers access logs]
    C --> D[Generate report]
    D --> E[Export/download PDF]
    E --> F([End])
```

---
Workflow 6: Access Appeal Process
---
```mermaid
flowchart TD
    A([Start]) --> B[User submits appeal]
    B --> C[Notify Manager]
    C --> D{Review appeal justification}
    D -- Accept --> E[Reinstate access]
    D -- Reject --> F[Maintain denial]
    E --> G([End])
    F --> G
```



---
Workflow 7: MFA Authentication on Login
---
```mermaid
flowchart TD
    A([Start]) --> B[User enters credentials]
    B --> C[Prompt MFA code]
    C --> D{MFA valid?}
    D -- Yes --> E[Grant access]
    D -- No --> F[Reject access]
    E --> G([End])
    F --> G
```



---
Workflow 8: Real-Time IAM Data Sync
---
```mermaid
flowchart TD
    A([Start]) --> B[Schedule IAM system sync]
    B --> C[Connect to IAM/HR APIs]
    C --> D{Successful connection?}
    D -- Yes --> E[Sync user data]
    D -- No --> F[Log error & alert admin]
    E --> G([End])
    F --> G

```
