import random

AUTHOR = "Matthew Sabadac"
APP_NAME = "Random Playing Card"

def run():
    ranks = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace"
    ]

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    rank = random.choice(ranks)
    suit = random.choice(suits)

    return f"Your random card is the {rank} of {suit}."
