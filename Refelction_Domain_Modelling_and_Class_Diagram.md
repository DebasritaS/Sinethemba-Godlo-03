# Reflection

## The below is the reflection on challenges faced when developing Domain Modelling and Class Diagrams.

**Challenges Faced in Designing the Domain Model and Class Diagram**

Designing the domain model and class diagram for the Automated User Access Review System was difficult and had several challenges, particularly in defining clear relationships and determining appropriate method responsibilities.
One of the primary difficulties was identifying the right level of concept for each entity. For example, distinguishing between User, Reviewer, and Manager required consideration. Initially, inheritance seemed natural, but as the system's workflows became clearer, it became evident that roles might change over time or overlap, making a role-based attribute system more flexible.

Modelling complicated relationships, such as between `AccessRequest`, `ReviewTask`, and `ReviewCycle`, presented another difficulty. In the real workflow, these entities are closely related even if they are conceptually separate. It was challenging to decide which entity "owns" the relationship; for example, should a `ReviewTask` be linked separately within a `ReviewCycle`, or should it be a part of the `AccessRequest` lifecycle? In the end, modularity was preserved by using `ReviewTask` as a bridge entity with references to both `ReviewCycle` and `AccessRequest`.

Uncertainty also existed in the definition of approaches. Adding logic-heavy methods to domain entities (such as `AccessRequest's` `autoRevoke()`) was alluring, but doing so ran the risk of converting the model into a procedural script. I made sure the class diagram represented intent over execution by concentrating on encapsulating responsibilities rather than implementation to uphold object-oriented concepts.

**Alignment with Previous Assignments**
   
The class diagram aligns well with the system's use cases, state transition diagrams, and functional requirements:

•	The `AccessRequest` class maps directly to main user stories like “Submit Access Request” and “`Review Access”.

•	The states defined in the state diagrams (e.g., “`Pending`”, “`Approved`”, “`Rejected`”) are represented as the status attribute of AccessRequest, ensuring consistency across design artifacts

•	Functional requirements like FR-01: Schedule periodic reviews and FR-03: Review and approve access are embedded into the responsibilities of `ReviewCycle` and `ReviewTask`, ensuring traceability.

•	`AuditLog` directly supports non-functional requirements around security and compliance, specifically logging access review actions (mapped to NFR-04).

**Trade-Offs Made**

• **Inheritance vs. Composition:** As previously stated, I used characteristics to show roles rather than strict class inheritance (such as Reviewer inheriting from User). This made shared behaviour less reusable, but it made managing users easier and allowed for active role assignment.

•	**Complexity vs. Clarity:** I purposely limited the abstract links by keeping the diagram flat and straightforward. For example, external service layers not illustrated in this diagram were given responsibility for NotificationService and EscalationEngine instead of modelling them.

•	**Method Minimization:**	I restricted methods to `submit()`, `approve()`, and `reviewTask()`, which are key domain actions, rather than modelling every way that can be present in a complete system. 

**Lessons Learned about Object-Oriented Design**

•	**Responsibility Assignment is Key:** Good design means confirming each class has a clear role and responsibilities. 
•	**Keep Entities Focused:** Each entity should represent a single model with relevant behaviour and data.
•	**Model for Flexibility:** Systems changes. Designing around roles, references, and interfaces ensures adaptability over time, especially in enterprise systems like access reviews, where policies and workflows change frequently.
•	**Design with the User in Mind:** The domain model must reflect how users (end-users, reviewers, admins) interact with the system. 
