# AI-use log

## Interaction 1

Date: October 7, 2026
Assistant: Gemini
Purpose: Transitioning implementation plan from claimed issues to Issue #41, generating palindrome string-slicing logic, and formatting submission documentation.
Prompt or summary: "Help me switch to Issue #41 (Palindrome Checker plugin) and produce all required assignment template files matching the course specifications."

### Suggestion accepted

What did the AI suggest?
The AI suggested using Python string slicing (`word.lower() == word.lower()[::-1]`) to determine whether a word is a palindrome.
Why did I accept it?
It is a concise, idiomatic Python approach that uses zero external dependencies and satisfies the requirement to use only standard Python features.
What evidence supported the decision?
Official Python documentation confirms standard string slicing creates a reversed copy without requiring imported libraries.

### Suggestion revised

What did the AI suggest?
The AI originally generated placeholder bracketed text (e.g., `[Your Name]`, `[Your Fork URL]`) throughout all Markdown files.
What did I change?
I manually edited all files to insert my actual student name, GitHub repository URLs, commit hashes, and local environment path.
Why did I change it?
To accurately document my personal local environment and GitHub fork details for grading.

### Suggestion rejected

What did the AI suggest?
The AI suggested adding interactive `input()` statements to let users type their own words at run time.
Why did it not fit the repository or issue?
`main.py` executes `run()` automatically across discovered plugins. Prompting for interactive console input could block automated launcher execution or pipeline tests.

Related issue: https://github.com/AmalChUm/students-arcade/issues/41
Related branch or pull request: feature/issue-41-palindrome-checker
