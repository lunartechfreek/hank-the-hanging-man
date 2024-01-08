import random
import words 
import story

def get_word(difficulty_selected):
    """
    Function to return random word, taking
    a parameter of game difficulty chosen
    """
    word = random.choice(difficulty_selected)
    return word.upper()

def run_story(story):
    """
    Function to display relevant section
    of story narrative
    """
    print(story)

def welcome():
    """
    Function to handle the start of the game
    """
    run_story(story.intro)

    while True:
        # Loop to ask user if they would like to play
        user_input = input('Do you accept the challange? (Y/N)').upper()  

        if user_input == 'N':
            print('Goodbye!')
            break
        elif user_input == 'Y':
            print('Lets Play!...\n')
        else:
            # Handles invalid input by the user
            print('Invalid input. Please enter Y or N.\n')

def main():
    welcome()

main()
