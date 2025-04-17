# Below is the class diagram for Mermaid.js.
It includes Classes, Relationships, and Multiplicity


```mermaid
classDiagram
    %% === Classes and Attributes ===
    class User {
        -userId: String
        -name: String
        -email: String
        -role: String
        +submitAccessRequest()
        +viewReviewStatus()
    }

    class AccessRequest {
        -requestId: String
        -userId: String
        -resourceId: String
        -status: String
        -requestDate: Date
        +submit()
        +approve()
        +reject()
        +escalate()
    }

    class ReviewTask {
        -taskId: String
        -reviewerId: String
        -requested: String
        -decision: String
        -reviewedDate: Date
        +makeDecision()
    }

    class Reviewer {
        -reviewerId: String
        -name: String
        -department: String
        +assignTask()
        +reviewTask()
    }

    class ReviewCycle {
        -cycleId: String
        -startDate: Date
        -endDate: Date
        -status: String
        +startCycle()
        +closeCycle()
    }

    class Resource {
        -resourceId: String
        -name: String
        -sensitivity: String
        -ownerId: String
    }

    class AuditLog {
        -logId: String
        -action: String
        -actorId: String
        -timestamp: Date
        +String description
        +recordAction()
    }

    %% === Relationships & Multiplicities ===

    User "1" --> "0..*" AccessRequest : submits
    AccessRequest "1" --> "1" Resource : for
    AccessRequest "1" --> "0..1" ReviewTask : reviewed by
    Reviewer "1" --> "0..*" ReviewTask : assigned
    ReviewCycle "1" --> "0..*" ReviewTask : includes
    ReviewTask "1" --> "1" AccessRequest : evaluates
    AccessRequest "1" --> "0..*" AuditLog : logs
    User "1" --> "0..*" AuditLog : triggers
    Resource "1" --> "0..1" User : owned by
 
```


**AccessRequest** status has these values: Pending, Approved, Rejected, Escalated.

**ReviewCycle** is used to group tasks under a review period.

**Resource sensitivity** is used for risk-based access control.




