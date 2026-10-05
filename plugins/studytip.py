import random

AUTHOR = "Destiny Jordan"
APP_NAME = "Random Study Tip"

TIPS = [
    "Set a regular daily goal and/or schedule.",
    "Create a cozy learning environment to study in.",
    "Stay hydrated and nourished.",
    "Use the Pomodoro technique where you study in 25 minute increments with a 5-10 minute break.",
    "Put away any distractions or put your devices on Do Not Disturb.",
    "Reward yourself after successful studying sessions with things you enjoy such as playing games afterwards or scrolling on social media.",
    "If you don't understand a topic, try teaching it to someone else or talking about it aloud and review anything that you didn't understand.",
    "Join a study group or create a study session with friends that will hold you accountable and keep you focused.",
]

def run():
    tip = random.choice(TIPS)
    return f"{APP_NAME}: {tip}"