# Contribution plan

Issue: Add a palindrome-checker arcade plugin (#41)
Issue URL: https://github.com/AmalChUm/students-arcade/issues/41
Selected difficulty: difficulty: beginner
Proposed branch: feature/issue-41-palindrome-checker
Expected files: plugins/palindrome_checker.py

## My interpretation of the task

The issue asks for a new arcade plugin that checks whether a given word is a palindrome (reads the same forwards and backwards). To comply with the launcher interface without interrupting batch runs using interactive console `input()`, the plugin picks a word from a set of words and evaluates it, returning a formatted string result.

## Acceptance criteria

- [ ] Create a new file `plugins/palindrome_checker.py`.
- [ ] Define required module metadata (`AUTHOR` and `APP_NAME`).
- [ ] Implement `run()` function that returns a readable string.
- [ ] Ensure only Python standard library packages (`random`) are used.
- [ ] Leave `main.py` and unrelated files untouched.

## Possible risks or questions

- Risk: Filename collision with another student's submission. Mitigated by using a descriptive filename (`palindrome_checker.py`).
- Question: Should user input be accepted via prompt? The standard `main.py` launcher calls `run()` programmatically, so returning a random evaluation keeps it non-blocking and automated.
