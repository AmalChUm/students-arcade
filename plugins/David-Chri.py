import random

# Each student names their file plugins/github_username.py

AUTHOR = "David Christian"
APP_NAME = "Coin Flipper"

def run():
    """Main execution function called by main.py."""
    responses = ["Heads!", "Tails!"]
    return f"🎱 {APP_NAME} says: {random.choice(responses)}"