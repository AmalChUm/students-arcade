"""Vowel Counter Arcade Plugin."""

import random

# Plugin metadata read by main.py
AUTHOR = "lui01212"
APP_NAME = "Vowel Counter Arcade"

# Sample phrases for demonstration
SAMPLE_PHRASES = [
    "Open Source Arcade",
    "Python Programming",
    "Hacktoberfest is Awesome",
    "Beautiful is better than ugly",
    "Explicit is better than implicit",
    "Simple is better than complex",
    "Readability counts",
    "Students Arcade",
]

VOWELS = set("aeiouAEIOU")


def count_vowels(text: str) -> int:
    """Counts the total number of vowels (A, E, I, O, U) in text."""
    return sum(1 for char in text if char in VOWELS)


def run() -> str:
    """Demonstrates vowel counting on a sample phrase."""
    phrase = random.choice(SAMPLE_PHRASES)
    total = count_vowels(phrase)
    return f"[Vowel Counter] '{phrase}' -> Found {total} vowel(s)."
