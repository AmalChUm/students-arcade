import random

# Each student names their file plugins/github_username.py

AUTHOR = "David Christian"
APP_NAME = "Trivia"

def run():
    """Main execution function called by main.py."""
    trivia_choice = random.randint(1,5)
    if trivia_choice == 1:
        print("1")
    elif trivia_choice == 2:
        print("2")
    elif trivia_choice == 3:
        print("3")
    elif trivia_choice == 4:
        print("4")
    else:
        print("5")

    if trivia_choice == 1:
        print("p1")
    elif trivia_choice == 2:
        print("p2")
    elif trivia_choice == 3:
        print("p3")
    elif trivia_choice == 4:
        print("p4")
    else:
        print("p5")