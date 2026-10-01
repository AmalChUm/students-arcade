"""Palindrome Checker Arcade Plugin."""

import random

# Plugin metadata read by main.py
AUTHOR = "lui01212"
APP_NAME = "Palindrome Checker Arcade"

# Sample words for demonstration
SAMPLE_WORDS = [
    ("racecar", True),
    ("level", True),
    ("arcade", False),
    ("students", False),
    ("radar", True),
    ("python", False),
    ("madam", True),
    ("rotor", True),
    ("github", False),
    ("kayak", True),
]


def is_palindrome(text: str) -> bool:
    """Checks if text is a palindrome, ignoring non-alphanumeric characters and case."""
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def run() -> str:
    """Demonstrates palindrome checking on a selected word."""
    word, expected = random.choice(SAMPLE_WORDS)
    result = is_palindrome(word)
    verdict = "IS a palindrome" if result else "is NOT a palindrome"
    return f"[Palindrome Checker] '{word}' -> {verdict}!"
