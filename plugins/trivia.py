import random

# Each student names their file plugins/github_username.py

AUTHOR = "David Christian"
APP_NAME = "Trivia"

def run():
    """Main execution function called by main.py."""
    trivia_choice = random.randint(1,5)
    if trivia_choice == 1:
        return f"{APP_NAME} asks: What year did the first Jurassic Park movie release? \n {APP_NAME} says: 1993"
    elif trivia_choice == 2:
        return f"{APP_NAME} asks: The name of the guitarist who did the solo for Beat It? \n {APP_NAME} says: Rocker Eddie Van Halen"
    elif trivia_choice == 3:
        return f"{APP_NAME} asks: How many presidents are on Mount Rushmore? \n {APP_NAME} says: Four"
    elif trivia_choice == 4:
        return f"{APP_NAME} asks: What Country gave women the right to vote first? \n {APP_NAME} says: New Zealand."
    else:
        return f"{APP_NAME} asks: What is a group of Crows called? \n {APP_NAME} says: A Murder of Crows"