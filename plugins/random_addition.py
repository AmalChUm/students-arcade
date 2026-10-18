import random

# Original number-addition plugin by Gaige Szy; random behavior updated by Andrew Haralambous.
AUTHOR = "Gaige Szy and Andrew Haralambous"
APP_NAME = "Number Addition"

def run():
    """Add two random integers from 1 to 100 and show the sum."""
    # Generate values without prompting, so the launcher can run every plugin unattended.
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    total = first + second
    return f"{APP_NAME} complete: {first} + {second} = {total}"
