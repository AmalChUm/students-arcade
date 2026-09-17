import random

AUTHOR = "Sravya Sambaturu"
APP_NAME = "Magic 8-Ball"

def run():
    """Main execution function called by main.py."""
    responses = [
        "Yes, definitely!",
        "Ask again later.",
        "Outlook not so good."
    ]
    return f"🎱 {APP_NAME} says: {random.choice(responses)}"
