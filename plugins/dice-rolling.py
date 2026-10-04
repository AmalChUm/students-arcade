import random

AUTHOR = "Madelyn Moore"
APP_NAME = "Dice Roller"

def run():
    dice = random.randint(1,6)
    return f"{APP_NAME}: You rolled a {dice}!"