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
    Function to handle the start of the game,
    and to pass the user the choice of difficulty.
    This will return the array that was previously
    selected by the user in the select_difficulty
    function
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
    """
    Function to display hangman phases
    """
    phases = [
        # Phase 7, game over when tries = 0
        # Noose, head, torso, both arms, both legs
       textwrap.dedent("""
            ________
            |/     |
            |      💀
            |     /|\\
            |     / \\
            |

        """),
        # Phase 5, when tries = 1
        # Noose, head, torso, both arms, leg
        textwrap.dedent("""
            ________
            |/     |
            |      🥵
            |     /|\\
            |     /
            |
            
        """),
        # Phase 5, when tries = 2
        # Noose, head, torso, both arms
        textwrap.dedent("""
            ________
            |/     |
            |      😱
            |     /|\\
            |     
            |
            
        """),
        # Phase 3, when tries = 3
        # Noose, head, torso, arm
        textwrap.dedent("""
            ________
            |/     |
            |      😨
            |     /|
            |     
            |
            
        """),
        # Phase 2, when tries = 4
        # Noose, head, torso
        textwrap.dedent("""
            ________
            |/     |
            |      😩
            |      |
            |     
            |
            
        """),
        # Phase 1, when tries = 5
        # Noose, head
        textwrap.dedent("""
            ________
            |/     |
            |      😲
            |        
            |     
            |
            
        """),
        # Phase 0, game start when tries = 6
        # Empty noose
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

