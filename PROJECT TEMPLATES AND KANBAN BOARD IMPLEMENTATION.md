# 1. Template Analysis and Selection

I have created a **Kanban Template**, a **Custom Template**, and a **Bug Triage Project Template** under GitHub Projects.


![image](https://github.com/user-attachments/assets/7d14e3ab-025e-4802-95c8-5eb68c07dbd7)




| Template            | Features                                              | Best For                                      | Limitations |
|---------------------|-------------------------------------------------------|-----------------------------------------------|-------------|
| **Basic Kanban**    | Simple columns (To Do, In Progress, Done)             | Small teams, simple workflows                | No automation |
| **Bug Triage**      | Prioritizes and organizes bug reports                 | Large projects with frequent bug reports     | Not suited for feature tracking |
| **Custom Template** | Fully customizable columns & workflows                 | Teams with unique workflows                  | Requires manual setup |

I have chosen **Kanban Board** because it enhances the workflow visibility, efficiency, and productivity. Also assist in identifying the bottleneck, keeping teams on track, and measuring success.

# 2. Custom Kanban Board Creation

![image](https://github.com/user-attachments/assets/26ab36b1-5abd-41c2-a603-22ef94101cf0)


# 3. Kanban Board Explanation

A **Kanban board** is a visual tool that helps teams in a project to manage work efficiently by tracking progress through different stages. It consists of comlumns representing **Backlog, To Do, In Progress, Testing, Blocked, and Done**.

A **Kanban board** is a visual workflow that reflects the board with columns that reflect different stages of work (**Backlog, To Do, In Progress, Testing, Blocked, and Done**). Each Task (card) moves froom left to right as it progresses. This visual flow ensures that everyone sees the current state of work immediately. **Work In Progress** limit depends on the number of members assigned tasks, that will help each member to focus on what he/she needs to do by doing so I will be preventing overloading team members and reduces context switching. 

**Continous delivery**, teams pull tasks when they have capacity to ensure a steady workflow. Small, frequesnt deliveries alighn with Agile's focus on incremental progress. **Adaptability and Flexibility**, that will assist with workflow that evolve based on team performance and process improvements. **Transparency and Collaboration**, assist with preventing duplicate work because everyone sees what's in progress.

# 4. Reflection

Havinig to choose the right fit Github Project Template and customizing it for your team can be challenging due to various factors such as:

Template Limitations: Basic Kanban lacks automantion and requires manual updates. Automated Kanban is strict, making customization harder (adding a new columns requires extra setup). 

Aligning with Workflow Needs: Some teams require a review stage (questions and answers or code review) in which default templates do not include. •	If using Agile sprints, GitHub’s Kanban does not inherently support sprint cycles like Jira or ClickUp.

Managing Work-in-Progress (WIP) Limits:	GitHub’s built-in Kanban does not enforce WIP limits (unlike Trello or Monday.com, which allow automatic restrictions). Requires manual discipline or GitHub Actions to automate enforcement.


## Comparing of GitHub Templates to Other Tools

|Feature	| GitHub Projects	| Jira	|Trello	| ClickUp |
|---------|-----------------|-------|-------|---------|
|Kanban Support	| Yes	| Yes	| Yes | Yes|
|Sprint Management | Limited| Strong	| Limited|	Strong|
|Automation|	 GitHub Actions|	 Built-in	| Power-ups|	Custom Workflows|
|WIP Limits|	 Manual setup	 |Built-in	| Power-ups| 	 Custom rules|
|Customization|	 Flexible but requires setup	| High|	 Moderate |	 High|
|Best For|	Dev teams using GitHub	|Agile/Enterprise	|Visual task tracking|	All-in-one project mgmt|

