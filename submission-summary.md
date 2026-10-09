# Submission Summary

29. Student name: Zachary Thomas
30. Selected issue title and URL: Add a palindrome-checker arcade plugin - https://github.com/AmalChUm/students-arcade/issues/41
31. Difficulty label and task/category label: difficulty: beginner, task: plugin
32. Parent repository URL: https://github.com/AmalChUm/students-arcade
33. Fork URL: https://github.com/zachrt/students-arcade
34. Local clone folder name: students-arcade
35. Feature branch URL: https://github.com/zachrt/students-arcade/tree/feature/issue-41-palindrome-checker
36. Commit URLs:
    - https://github.com/zachrt/students-arcade/commit/1776a1a6e535f0846cafbd538e0db8bcab07af65
37. Verification output: Recorded in evidence/02-verification.txt
38. Pull-request URL: https://github.com/AmalChUm/students-arcade/pull/103
39. Screenshot of the issue on the board: evidence/screenshots/01-kanban-board.png
40. Screenshot showing the issue moving through statuses: evidence/screenshots/02-kanban-workflow.png
41. contribution-plan.md: Included in root directory
42. ai-log.md: Included in root directory
43. evidence/01-setup.txt: Included in evidence directory
44. evidence/02-verification.txt: Included in evidence directory
45. evidence/03-self-review.txt: Included in evidence directory
46. Short reflection: Completed below

---

## Reflection

**48. Why did you choose this issue?**
I selected Issue #41 after prior beginner choices were claimed by other students. It allowed me to implement standard Python string manipulation while strictly adhering to the repository's plugin interface.

**49. What did you learn by reading the existing repository before coding?**
I learned how `main.py` dynamically inspects and loads modules from the `plugins/` folder by reflecting on `AUTHOR`, `APP_NAME`, and invoking `run()`.

**50. How does the plugin or documentation contribution fit the existing Students Arcade structure?**
It acts as a self-contained module in `plugins/`. Standardizing `AUTHOR`, `APP_NAME`, and `run()` allows `main.py` to auto-discover and run it without requiring any edits to core launcher files.

**51. What was the most important acceptance criterion?**
Keeping `main.py` completely unmodified so dynamic plugin discovery functions as intended.

**52. Which AI suggestion did you accept?**
Using Python's built-in string slicing (`word.lower()[::-1]`) to verify palindromes cleanly.

**53. Which AI suggestion did you revise or reject?**
Rejecting interactive `input()` calls inside `run()` to avoid blocking non-interactive runner execution.

**54. What did you verify yourself instead of trusting the AI?**
I verified local execution by executing `python3 main.py` directly in my terminal and ensuring my output printed as expected.

**55. What evidence shows that your contribution works?**
The execution log captured in `evidence/02-verification.txt`.

**56. What was the difference between your fork and the parent repository?**
My fork contains the `feature/issue-41-palindrome-checker` branch with `plugins/palindrome_checker.py` and assignment evidence files.

**57. What would you improve in a future pull request?**
Add case-insensitive multi-word phrase evaluation (e.g., stripping spaces/punctuation for phrases like "A man, a plan, a canal: Panama").
