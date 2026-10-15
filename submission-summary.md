# Students Arcade Contribution Submission

## Student
Zora Smith

## Selected issue
Issue #33 — Add a greeting-message arcade plugin

Issue URL:
https://github.com/AmalChUm/students-arcade/issues/33

## Pull request
https://github.com/AmalChUm/students-arcade/pull/90

## Issue details

Difficulty label:
beginner

Task/category label:
task: plugin

## Repository information

Parent repository:
https://github.com/AmalChUm/students-arcade

Fork repository:
https://github.com/ZoraS123/students-arcade

Local clone folder:
students-arcade

Feature branch:
feature/issue-33-greeting-message

Feature branch URL:
https://github.com/ZoraS123/students-arcade/tree/feature/issue-33-greeting-message

## Commit URLs

1. Document issue 33 contribution setup  
https://github.com/AmalChUm/students-arcade/pull/90/changes/7c83560d558d6bd2b90ee037b9ab32f9581123ed

2. Add greeting plugin structure  
https://github.com/AmalChUm/students-arcade/pull/90/changes/1b8c0eba50150df7bf6847b3dafedd2667d45c05

3. Implement random greeting behavior  
https://github.com/AmalChUm/students-arcade/pull/90/changes/af59cf7501b4396bef29c5354e87ba173f2d1bff

4. Add verification and AI documentation  
https://github.com/AmalChUm/students-arcade/pull/90/changes/a8bc286f80e7e69b7226aad3286d375984e02f42

5. Update contribution plan completion  
https://github.com/AmalChUm/students-arcade/pull/90/changes/57aef277d6313d33779b4f190e5a59429662b289

6. Add submission summary and board evidence  
https://github.com/AmalChUm/students-arcade/pull/90/changes/210773f962b2c732911bf42efb3eed27b011412a

## Kanban Project

https://github.com/users/AmalChUm/projects/3

Board screenshot:
evidence/screenshots/issue-33-in-review.png

Issue details screenshot:
evidence/screenshots/issue-33-details.png

Status progression:
Issue #33 was moved from Backlog to In Progress when work began, then to In Review after implementation and local verification. The current board screenshot shows the final In Review status.

## Optional issue

Issue #36 — Add a unit-converter arcade plugin

Issue URL:
https://github.com/AmalChUm/students-arcade/issues/36

Status:
Claimed but not completed.

## Reflection

### Why did you choose this issue?
I chose Issue #33 because it was a beginner-friendly plugin task with a clear scope. It gave me a chance to practice working with an existing repository without making changes to the main launcher.

### What did you learn by reading the existing repository before coding?
I learned how the Students Arcade repository discovers plugins and that each plugin follows the same basic interface using `AUTHOR`, `APP_NAME`, and `run()`.

### How does this contribution fit the existing Students Arcade structure?
The greeting-message plugin is stored in the `plugins` folder and follows the same structure as the existing arcade plugins, so `main.py` can discover and run it automatically.

### What was the most important acceptance criterion?
The most important criterion was making sure the plugin could be discovered and executed by the existing launcher without modifying `main.py`.

### Which AI suggestion did you accept?
I accepted the suggestion to use Python's `random` module and `random.choice()` to select one greeting from a list of six greetings.

### Which AI suggestion did you revise or reject?
I revised the organization of the assignment files when `contribution-plan.md` was initially placed inside the evidence folder. I moved it to the repository root so the structure matched the assignment.

### What did you verify yourself instead of trusting the AI?
I ran `python3 main.py` myself and checked that the plugin was discovered, my name and activity name were displayed correctly, a greeting was returned, and the existing plugins still ran.

### What evidence shows that your contribution works?
The verification output showed `Greeting Message by Zora Smith`, displayed a greeting, and reported `Ran 8 plugin(s).`

### What was the difference between your fork and the parent repository?
The parent repository is the original Students Arcade repository. My fork is my own copy where I created my feature branch and committed my changes before opening a pull request back to the parent repository.

### What would you improve in a future pull request?
In a future pull request, I would organize the required documentation files correctly from the beginning and review the submission checklist earlier so fewer files need to be moved or corrected later.
