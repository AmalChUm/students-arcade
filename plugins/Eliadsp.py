import random

# Each student names their file plugins/github_username.py

AUTHOR = "Eliad Spraggins"
APP_NAME = "Card Generator"

def run():
    """Main execution function called by main.py."""
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♥", "♦", "♣"]
    return f"🃏 {APP_NAME} says: Your random card is {random.choice(ranks)}{random.choice(suits)}"