import random

# Each student names their file plugins/github_username.py

AUTHOR = "Mackenzie Klupp"
APP_NAME = "D20 roller"

def run():
    """Main execution function called by main.py."""
    roll_result = random.randint(1, 20)
    return f"🎲 {APP_NAME} rolled a {roll_result}! (1-20)"