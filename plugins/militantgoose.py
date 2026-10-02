import random

AUTHOR = "militantgoose"
APP_NAME = "Magic 8-Ball"

RESPONSES = {
    "affirmative": [
        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
    ],
    "neutral": [
        "Reply hazy, try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
    ],
    "negative": [
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful",
    ],
}

# Flatten so each of the 20 answers is equally likely, like the real toy
ALL_RESPONSES = [r for group in RESPONSES.values() for r in group]


def run():
    return random.choice(ALL_RESPONSES)

if __name__ == "__main__":
    print(AUTHOR)
    print(APP_NAME)
    print(run())
