import random

# Plugin metadata read by main.py
AUTHOR = "Gemini"
APP_NAME = "Daily Tip Generator"

# Collection of tips for students and developers
TIPS = [
    "Commit early and commit often! Small PRs are much easier to review.",
    "Always write descriptive commit messages (e.g., 'Fix header bug' instead of 'fix').",
    "Use `git status` frequently to check which files are staged before committing.",
    "Never push sensitive info like API keys, passwords, or personal credentials to GitHub!",
    "Read error messages carefully—most of the time, the exact file and line number are given.",
    "Create a new Git branch whenever you start working on a new feature or fix.",
    "Take regular breaks! Stepping away from the screen solves more bugs than staring at code.",
    "Write code for human readers first, and computers second.",
]

def run() -> str:
    """Returns a randomly selected developer tip."""
    selected_tip = random.choice(TIPS)
    return f"💡 Tip of the Day: {selected_tip}"