# Contributing

Thank you for contributing to this project. Please follow the workflow below when making changes.

## Contribution Workflow

### 1. Fork the Repository

Fork the repository on GitHub and clone your fork locally:

```
git clone <your-fork-url>
cd <repository-name>
```

### 2. Create a Feature Branch

Do not make changes directly on main. Create a dedicated feature branch for your work:

```
git checkout -b feature/<feature-name>
```

For example:

```
feature/issue-8-dice-plugin
feature/issue-16-guessing-interface
```

Keep your changes focused on the issue or task you are addressing.

### 3. Implement the Plugin

Implement the requested plugin using the project's existing structure and conventions.

When making changes:

- Work in a dedicated feature branch.
- Keep the change focused on this issue.
- Preserve the MIT license and existing attribution.
- Do not add credentials, tokens, private information, or unnecessary dependencies.
- Verify the result with python main.py when the task changes executable Python behavior.
- Open a pull request that links this issue and explains the verification performed.

### 4. Verify Your Changes

If the task changes executable Python behavior, run:

```
python3 main.py
```

Confirm that the program runs successfully and that the new or modified plugin behaves as expected.

### 5. Review and Commit Your Changes

Before committing, review your changes:

```
git status
git diff
```

Create meaningful commits that clearly describe the changes:

```
git add .
git commit -m "Add <plugin-name> plugin"
```

Avoid vague commit messages such as update, changes, or stuff.

### 6. Push Your Branch

Push your feature branch to your fork:

```
git push -u origin feature/<feature-name>
```

### 7. Open a Pull Request

Open a pull request from your feature branch to the original repository's main branch.

The pull request should:

- Explain what was changed.
- Explain why the change was made.
- Link the pull request to the relevant issue.
- Describe the verification performed.
- Mention any relevant test or verification results.

For example:

Verification: Ran python3 main.py successfully and confirmed that the new plugin behaves as expected.

## Contribution Checklist

Before opening a pull request, confirm that:

- [ ] I worked in a dedicated feature branch.  
- [ ] My changes are focused on this issue.
- [ ] I preserved the MIT license and existing attribution.
- [ ] I did not add credentials, tokens, private information, or unnecessary dependencies.
- [ ] I ran python3 main.py when the task changed executable Python behavior.
- [ ] I reviewed my changes. 
- [ ] I created meaningful commit messages.
- [ ] I pushed my feature branch to my fork.
- [ ] My pull request links the relevant issue, explains the changes and verification performed. 