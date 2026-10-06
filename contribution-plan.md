# Contribution plan

Issue: #44 — Add a multiplication-quiz arcade plugin
Issue URL: https://github.com/AmalChUm/students-arcade/issues/44
Selected difficulty: beginner
Task/category label: task: plugin
Proposed branch: feature/issue-44-multiplication-quiz
Expected files: plugins/multiplication_question.py and assignment evidence files

## My interpretation of the task

Create a plugin that generates two random integers from 1 to 12
and displays a multiplication question with its correct answer.
Follow the existing plugin interface without changing main.py.

## Acceptance criteria

- [x] Add a unique descriptive Python filename in plugins/.
- [x] Define AUTHOR, APP_NAME, and run().
- [x] Display both random numbers and the correct product.
- [x] Use only the Python standard library.
- [x] Confirm main.py discovers and runs the plugin.
- [x] Keep the output readable and explain verification in the pull request.
- [x] Avoid executing the activity when the module is imported.

## Possible risks or questions

- Existing plugins may have skipped modules or import-time output.
- Use UTF-8 mode when saving output containing emojis.
- Check the multiplication result across several runs.

## Optional issue

Issue: #26 — Add a plugin summary to the arcade runner
Issue URL: https://github.com/AmalChUm/students-arcade/issues/26
Difficulty: advanced
Category: task: launcher
Expected file: main.py
Complete separately if time permits.