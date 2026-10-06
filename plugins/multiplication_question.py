import random

AUTHOR = "Deandre Skelton"
APP_NAME = "Multiplication Quiz"


def run():
    """Generate a multiplication question and show its correct answer."""
    first = random.randint(1, 12)
    second = random.randint(1, 12)
    answer = first * second

    return (
        f"Question: What is {first} x {second}?\n"
        f"Answer: {first} x {second} = {answer}"
    )