# ***** Chapter 5-7 exercise | Cory Friedt | IS125 *****

# Generates a "random" number
import random

# Asks the user for a number
def ask_number(question):
    user_response = int(input(question))
    return user_response


# Shows the user the game instructions
def show_instructions():
    print(
        """
 _________        .------------------.
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Welcome to my | |             
|:______B:|      | |                | |             
|:______B:|      | | Guessing Number| |             
|         |      | |                | |             
|:_____:  |      | |      Game!     | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:     

I randomly generated a number between 1 and 100, try to guess that in as few attempts as possible!                   
    
    """
    )


# Shows the user they won, shows correct number and the amount of attempts
def show_win(random_number, attempts):
    print("\nCorrect! The number was",random_number,"and you guessed it in",attempts,"tries!\n")


# ***** Main Function *****

# Create empty list for scores
scores = []

def main():
    show_instructions()  # Show instructions
    random_number = random.randint(1, 100)  # Generate random number
    attempts = 1  # initilize attempts
    name = input("\nWhat is your name?: ")
    guess = ask_number("\nWhat is your guess?: ")  # Recieve guess from user

    # loop until number guessed correctly
    while guess != random_number:
        if guess > random_number:
            print("\nLower!")
        else:
            print("\nHigher!")

        guess = ask_number("\nWhat is your guess?: ")
        attempts += 1

    show_win(random_number, attempts) # Call show_win function
    entry = (name, attempts) # Create tuple for name and attempts
    scores.append(entry) # Append that tuple to scores

# Play again loop and update high scores
play_again = "yes"
while play_again.lower() == "yes":
    main()
    scores.sort(key = lambda x: x[1])
    scores = scores[:5]
    print("*** HIGH SCORES ***", scores,"\n")
    play_again = input("Would you like to play again? (yes or no):")

# Print High Scores on Exit
print("*** HIGH SCORES ***", scores,"\n")


