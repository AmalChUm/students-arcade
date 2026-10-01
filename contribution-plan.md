# Contribution plan
Issue: #9, Rock Paper Scissors
Issue URL:
Selected difficulty: Intermediate
Proposed branch: feature/rock-paper-scissors
Expected files: rockpaperscissors.py

## My interpretation of the task
The issue asks me to create a valid and unbreaking game of rock, paper, scissors in the plugins directory.

## Acceptance criteria

- The new file is inside plugins/ and has a unique, descriptive filename.
- The module defines AUTHOR, APP_NAME, and run().
- The module is discovered and executed by python main.py.
- The output is readable and the change is documented in the pull request.
- The result identifies the available choices and outcome.

## Possible risks or questions
- Risk involved in interrupting the main.py loop with a user response and holding the operation from proceeding until a valid respopnse is given, but only minute. Nothing in the code suggests a major issue.
- How is the optimization of this plugin?