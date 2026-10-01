import random

# Each student names their file plugins/github_username.py

AUTHOR = "Gaige Szy"
APP_NAME = "Number Addition"

def run():
    """Add two random integers from 1 to 100 and show the sum."""
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    total = first + second
    return f"{first} + {second} = {total}"
