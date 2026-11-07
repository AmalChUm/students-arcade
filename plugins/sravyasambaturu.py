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
    # if True
    #     return "This line is intentionally invalid"

    return f"🎱 {APP_NAME} says: {random.choice(responses)}"
