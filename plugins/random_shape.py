import random

AUTHOR = "Mahroush"
APP_NAME = "Random Shape"


def run():
    shapes = {
        "Triangle": 3,
        "Square": 4,
        "Pentagon": 5,
        "Hexagon": 6,
        "Heptagon": 7,
        "Octagon": 8
    }

    shape = random.choice(list(shapes.keys()))
    sides = shapes[shape]

    return f"{APP_NAME}: {shape} has {sides} sides."