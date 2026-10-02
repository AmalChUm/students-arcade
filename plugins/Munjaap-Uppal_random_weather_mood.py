"""A fictional, randomly selected weather mood plugin.

This plugin selects a fictional weather mood at random and
displays a related description.
"""

import random

# Name of the plugin author.
AUTHOR = "Munjaap Uppal"

# Name of the application.
APP_NAME = "Random Weather Mood"

# Fictional weather moods and their descriptions.
_WEATHER_MOODS = {
    "Sunny": "A bright fictional sunbeam suggests a cheerful day ahead.",
    "Cloudy": "Fictional clouds gather softly, inviting a calm moment.",
    "Rainy": "A gentle fictional rain showers the day with fresh energy.",
    "Snowy": "Fictional snowflakes drift down, creating a peaceful atmosphere.",
}

def run():
    """Display a randomly selected fictional weather mood.

    A weather mood is selected from the available fictional moods,
    and the mood and its description are printed.
    """

    # Select one weather mood randomly.
    mood = random.choice(tuple(_WEATHER_MOODS))

    # Display the selected mood and its description.
    print(f"[Fictional random weather mood] {mood}")
    print(_WEATHER_MOODS[mood])

