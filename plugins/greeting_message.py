import random

AUTHOR = "Zora Smith"
APP_NAME = "Greeting Message"

def run():
    greetings = [
        "Hello!",
        "Hi there!",
        "Welcome!",
        "Good to see you!",
        "Hope you're having a great day!",
        "Nice to meet you!"
    ]

    greeting = random.choice(greetings)
    return f"{APP_NAME}: {greeting}"
    