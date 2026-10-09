import random

AUTHOR = "Zachary Thomas"
APP_NAME = "Palindrome Checker"

def run():
    words = ["racecar", "algorithm", "madam", "developer", "level", "arcade", "noon", "python"]
    word = random.choice(words)

    is_palindrome = word.lower() == word.lower()[::-1]
    
    if is_palindrome:
        return f"{APP_NAME}: The word '{word}' is a palindrome!"
    else:
        return f"{APP_NAME}: The word '{word}' is not a palindrome."