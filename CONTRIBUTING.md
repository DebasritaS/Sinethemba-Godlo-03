
# Contributing to This Project

Thank you for considering contributing! 
This guide will help you start with setup, development standards, and submitting pull requests.

---

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/)
- [git](https://git-scm.com/)
- Optional: [virtualenv](https://virtualenv.pypa.io/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Godlos252/Sinethemba-Godlo-03.git
   cd Sinethemba-Godlo-03
2. **Create a virtual environment by running the following in the terminal:**

  *python -m venv venv*
  
  *source venv/bin/activate*

3. **Install dependencies by running the following in the terminal:**
   
  *pip install -r requirements.txt*

4. **Run tests to ensure everything is set up correctly  in the terminal:**
   
  *Pytest*

# Coding Standards

### Style & Linting

We follow PEP 8.

**Lint your code using flake8 or ruff by running the following in the terminal:**

*pip install flake8*

*flake8 src/ tests/*

### Testing

All new code should include relevant unit tests.

-	Use pytest to write and run tests.
-	
-	Test files are located under the tests/ directory and should be named test_*.py.
  
**Run all tests within the terminal:**

*Pytest*

# Picking Issues & Submitting Pull Requests

### Finding Issues

-	Check the Issues tab.

-	Look for labels like good first issue or help wanted.

If you're unsure where to start, feel free to comment on an issue and ask!

### Working on an Issue

-	Comment on the issue to let others know you're working on it.
  
-	Create a new branch:
  
*git checkout -b issue-*

-	Write your code and add tests.
-	
-	Run linting and tests locally before committing.
-	
### Submitting a Pull Request

-	Push your branch:
  
*git push origin issue-*

-	Open a pull request via GitHub.
  
-	Fill out the PR template and link the issue it resolves.
  
-	Be ready to discuss feedback and make revisions.

