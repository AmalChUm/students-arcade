# Students Arcade

A small Python launcher (`main.py`) that discovers student plugins in the `plugins/` folder and runs each one.

## Run it

```bash
python main.py
```

If your computer uses `python3`, run `python3 main.py` instead.

## Plugin contract

Each plugin is a Python file in `plugins/` that defines:

```python
AUTHOR = "Your Name"
APP_NAME = "Name of the Activity"

def run():
    return "A result"
```

Plugins must be non-interactive (no `input()`), so they can run in automated workflows.

## Automation

- `.github/workflows/arcade-ci.yml` compiles the Python files and runs the launcher on pushes and pull requests.
- `.github/workflows/arcade-cd.yml` packages the project into `students-arcade-release.zip` and uploads it as a GitHub Actions artifact.