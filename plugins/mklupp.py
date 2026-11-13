import random

# Each student names their file plugins/github_username.py

AUTHOR = "Mackenzie Klupp"
APP_NAME = "D20 roller"

def run():
    """Main execution function called by main.py."""
    responses = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    return f"🎱 {APP_NAME} rolled at: {random.choice(responses)}"