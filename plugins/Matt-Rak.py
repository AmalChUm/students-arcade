import random

Game_name = "Guessing game"
Author = "Matthew Rakay"

def play_guessing_game():
    print("welcome to the guessing game!")
    print("Pick a number from 1 and 100")

    #generate random number
    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        try:
            # Get the player guess
            guess = int(input("Pick your number:"))
            attempts += 1

            #check the guess 
            if guess < secret_number:
                print ("Too low try again.")
            elif guess > secret_number:
                print("Too high try again.")
            else:
                print (f"YOU'RE THE WINNER!\n Hooray! Hooray! It took {attempts} guesses!")
                break 
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_guessing_game()