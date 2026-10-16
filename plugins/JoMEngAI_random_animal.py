"""Random-animal activity for the Students Arcade launcher."""

import random

AUTHOR = "Joseph Mendoza"
APP_NAME = "Random Animal"

ANIMALS = [
    ("Dolphin", "Mammal"),
    ("Eagle", "Bird"),
    ("Frog", "Amphibian"),
    ("Turtle", "Reptile"),
    ("Salmon", "Fish"),
    ("Butterfly", "Insect"),
    ("Elephant", "Mammal"),
    ("Penguin", "Bird"),
]


def run() -> str:
    """Return a randomly selected animal and its category."""
    animal, category = random.choice(ANIMALS)
    return f"{APP_NAME}: {animal} | Category: {category}"
