# AI-use log

## Interaction 1

Date: October 6, 2026
Assistant: AI Assistant
Purpose: Create a reusable pull-request checklist template for Issue #31.
Prompt or summary: Requested a Markdown template for a pull-request checklist, asked how to create and save a `.md` file structure using GitHub Desktop, and asked if the checklist needed updates to match the documentation-task requirements.

### ### Suggestion accepted

What did the AI suggest? 
The initial Markdown template layout, the exact file path location (`.github/pull_request_template.md`), and step-by-step instructions on making focused sequential commits using GitHub Desktop.

Why did I accept it? 
It directly satisfied the acceptance criteria in the issue description, met the requirement for multiple descriptive commits, and mapped perfectly to GitHub Desktop's layout.

What evidence supported the decision? 
GitHub Desktop tracked the file in the correct location and allowed the creation of focused commits with the recommended messages.

### ### Suggestion revised

What did the AI suggest? 
The AI suggested adding specific plugin requirements to the checklist (like checking for the `plugins/` directory, `AUTHOR`, and `APP_NAME` variables).

What did I change? 
I updated the template from a general checklist to one that explicitly details these specific repository-level requirements.

Why did I change it? 
The assignment documentation guidelines (Step 14) explicitly mandate checking filenames and plugin metadata against actual repository behavior to receive full credit for documentation tasks.

### ### Suggestion rejected

What did the AI suggest? 
Suggested creating files outside of desktop

Why did it not fit the repository or issue? 
I was working out of Desktop, not git bash

Related issue: #31
Related branch or pull request: feature/issue-31-pull-request-checklist
