import random

AUTHOR = "Arian Nunez"
APP_NAME = "Lottery Numbers"


def run():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return "Your lottery numbers are: " + str(numbers)