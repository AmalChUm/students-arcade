import random

AUTHOR = "Gaige Szy"
APP_NAME = "Rock Paper Scissors"
choices = ["rock", "paper", "scissors"]

def run():
    '''This function will let you play rock/paper/scissors against the random function!'''

    # computer choice of rock, paper, or scissors 🪨📄✂️
    computer_choice = random.choice(choices)

    user_choice = 0

    while user_choice not in choices:
        # this while ensures valid responses are given

        # user choice of rock, paper, or scissors, lowerized
        user_choice = input("Choose [ROCK], [PAPER], or [SCISSORS] by typing into the terminal: (case insensitive)\n").lower()

        match user_choice:
            # matches user_choice to  a case to determine if user won or not

            case "rock":
                if computer_choice == "rock":
                    result = "\nYou chose the same thing! You tied. 🪨"
                elif computer_choice == "paper":
                    result = f"\nThe computer chose {computer_choice} and beat you! 📄  > 🪨"
                else:
                    result = f"\nThe computer chose {computer_choice}, you win! ✂️  > 🪨"

            case "paper":
                if computer_choice == "paper":
                    result = "\nYou chose the same thing! You tied. 📄"
                elif computer_choice == "scissors":
                    result = f"\nThe computer chose {computer_choice} and beat you! ✂️  > 📄"
                else:
                    result = f"\nThe computer chose {computer_choice}, you win! 📄  > 🪨"
                
            case "scissors":
                if computer_choice == "scissors":
                    result = f"\nYou chose the same thing! You tied. ✂️"
                elif computer_choice == "rock":
                    result = f"\nThe computer chose {computer_choice} and beat you! 🪨  > ✂️"
                else:
                    result = f"\nThe computer chose {computer_choice}, you win! ✂️  > 📄"
                
            case _:
                print("You did not enter a valid option.\n")
                user_choice = input("Choose [rock], [paper], or [scissors] by typing into the terminal: (case insensitive)\n").lower()

    return result