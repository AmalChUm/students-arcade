"""Magic 8-Ball arcade plugin.

The launcher imports this module, reads AUTHOR and APP_NAME, and calls run().
"""

import random

AUTHOR = "Justin Mehl"  
APP_NAME = "Magic 8-Ball"

POSITIVE = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
]

NEUTRAL = [
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
]

NEGATIVE = [
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

ANSWERS = POSITIVE + NEUTRAL + NEGATIVE


def run():
    """Shake the 8-Ball and return a mystical answer."""
    answer = random.choice(ANSWERS)
    return f"{APP_NAME}: {answer}"
