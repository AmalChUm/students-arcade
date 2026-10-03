import random

# Secondary plugin - my primary plugin is plugins/sravyasambaturu.py (Magic 8-Ball)

AUTHOR = "Sravya Sambaturu"
APP_NAME = "Word Scrambler"

WORDS = ["python", "arcade", "plugin", "student", "github", "keyboard"]


def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def run():
    word = random.choice(WORDS)
    scrambled = scramble(word)
    return f"Original: {word} -> Scrambled: {scrambled}"