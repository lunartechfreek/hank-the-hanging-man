import random
import words 
import story
import textwrap

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

def select_difficulty():
    """
    Function for user to choose a difficulty,
    which will return the array of words 
    for the difficulty chosen
    """
    while True:
        # Loop to ask user to choose a difficulty
        print('Type E for easy')
        print('Type M for medium')
        print('Type H for hard\n')
        user_input = input('Please type E, M or H ').upper()  

        if user_input == 'E':
            run_story(story.easy)
            difficulty = words.easy_words
            break
        elif user_input == 'M':
            run_story(story.medium)
            difficulty = words.medium_words
            break
        elif user_input == 'H':
            run_story(story.hard)
            difficulty = words.hard_words
            break
        else:
            # Handles invalid input by the user
            print('Invalid input. Please enter .\n')

    return difficulty

def welcome():
    """
    Function to handle the start of the game
    """
    run_story(story.intro)

    while True:
        # Loop to ask user if they would like to play
        user_input = input('Do you accept the challange? (Y/N) ').upper()  

        if user_input == 'N':
            print('\nGoodbye!')
            quit()
        elif user_input == 'Y':
            print("\nLet's save Hank!...")
            print("First let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print('Invalid input. Please enter Y or N.\n')

    return difficulty

def display_hangman(tries):
    phases = [
       textwrap.dedent("""
            ________
            |/     |
            |      💀
            |     /|\\
            |     / \\
            |

        """),
        textwrap.dedent("""
            ________
            |/     |
            |      🥵
            |     /|\\
            |     /
            |
            
        """),
        textwrap.dedent("""
            ________
            |/     |
            |      😱
            |     /|\\
            |     
            |
            
        """),
        textwrap.dedent("""
            ________
            |/     |
            |      😨
            |     /|
            |     
            |
            
        """),
        textwrap.dedent("""
            ________
            |/     |
            |      😩
            |      |
            |     
            |
            
        """),
        textwrap.dedent("""
            ________
            |/     |
            |      😲
            |        
            |     
            |
            
        """),
        textwrap.dedent("""
            ________
            |/     |
            |     
            |     
            |     
            |
            
        """)
    ]

    return phases[tries]

def main():
    selected_difficulty = welcome()
    word = get_word(selected_difficulty)
    

main()

