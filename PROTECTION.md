# Branch Protection Policy for the main Branch

To maintain the integrity, stability, and security of the project, the following branch protection rules are enforced on the main branch:

✅  **1. Require Pull Request Reviews**

- This rule encourages collaboration and the sharing of knowledge.
  
- Assists in identifying bugs, design flaws, or performance issues early.

- Prevents unauthorized changes from being merged.
  
- Increases accountability and encourages code quality best practices.

✅  **2. Require Status Checks to Pass**

- This rule ensures that all automated tests (CI/CD pipelines) pass before merging, preventing broken code from being introduced to the production/main branch.
  
- It also protects against failures and increases confidence in each deployment.
  
- Enforces consistency in code formatting, style, and linting.

✅  **3. Disable Direct Pushes**

- This rule forces all changes to go through Pull Requests (PRs), enabling audits and discussions while preventing contributors from unintentionally bypassing review and CI/CD checks.
  
- It protects the branch from risky or unreviewed changes that could affect production and helps maintain a clear and traceable project history.
