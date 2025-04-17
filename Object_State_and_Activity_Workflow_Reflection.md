# Reflection

## Choosing Granularity for States and Actions

One of the primary challenges was deciding the right level of granularity for both state transition and activity diagrams.

Too many details made my diagrams overwhelming, especially when modelling review cycles. For example where actions like “assign reviewers”, “notify user”, “approve or reject”, and “log audit” could all be broken into sub-states.

Also, too few details made it challenging to capture meaningful transitions. For example, collapsing “Access Review Task Created” and “Pending Reviewer Action” into one state would have missed the core of the review lifecycle.

## Aligning diagrams with Agile user stories

Other user stories were broader (e.g., “As an IAM team member, I want to integrate with HR Systems”), requiring multiple actions or processes, and modelling this in one activity diagram often led to clutter.

Others were implementation-focused (e.g., “Automatically revoke access after deadline”) and mapped well to specific states (“Pending Review” → “Revoked”). 

I decomposed broad user stories into task-level actions (mirroring activity diagram steps).

I used state diagrams for objects with a defined lifecycle (e.g., Review Task, Review Cycle) and matched transitions to user decisions.

## Compare state diagrams

|Comparison	|State Diagrams	|Activity Diagrams|
|-----------|---------------|-----------------|
|Focus |	Lifecycle of a specific object|	Overall system or user workflow|
|Best for	|Access Task, Review Cycle, Audit Log behavior	|Multi-role workflows like Review Execution|
|Example Benefit	|Shows exactly when an object becomes "Revoked" |	Visualizes entire path from request to audit|
|Challenge |	Hard to show parallelism or roles	|Can be too high-level for object-specific logic|
