"""A fictional, randomly selected weather mood plugin."""

import random

AUTHOR = "Munjaap Uppal"
APP_NAME = "Random Weather Mood"

_WEATHER_MOODS = {
    "Sunny": "A bright fictional sunbeam suggests a cheerful day ahead.",
    "Cloudy": "Fictional clouds gather softly, inviting a calm moment.",
    "Rainy": "A gentle fictional rain showers the day with fresh energy.",
    "Snowy": "Fictional snowflakes drift down, creating a peaceful atmosphere.",
}

def run():
    """Display a randomly selected fictional weather mood."""
    mood = random.choice(tuple(_WEATHER_MOODS))
    print(f"[Fictional random weather mood] {mood}")
    print(_WEATHER_MOODS[mood])


