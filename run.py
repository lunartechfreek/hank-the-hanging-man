# Import modules
import random
import words
import story
import textwrap
import os
import colorama
from colorama import Fore, Style

# To initialize colorama and to autoreset styles
colorama.init(autoreset=True)

# Global variables that are modified in different functions
global TRIES
global GUESSED


def clear():
    """
    Clear function to clean-up the terminal.
    Function checks the users operating system to
    use the correct method to clear the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


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
        print('Type E for easy')
        print('Type M for medium')
        print('Type H for hard\n')
        user_input = input('Please type E, M or H \n').upper()
        clear()

        if user_input == 'E':
            run_story(story.easy)
            difficulty = words.easy_words
            print("Let's save Hank!...")
            break
        elif user_input == 'M':
            run_story(story.medium)
            difficulty = words.medium_words
            print("Let's save Hank!...")
            break
        elif user_input == 'H':
            run_story(story.hard)
            difficulty = words.hard_words
            print("Let's save Hank!...")
            break
        else:
            # Handles invalid input by the user
            print(f'\nSorry, {Fore.RED}{Style.BRIGHT}{user_input}{Fore.RESET}{Style.RESET_ALL} is not a valid input.')  # noqa
            print('Please enter the letter E, M, or H\n')

    return difficulty


def welcome():
    """
    Function to handle the start of the game,
    and to pass the user the choice of difficulty.
    This will return the array that was previously
    selected by the user in the select_difficulty
    function
    """
    print('Welcome to Hank the Hanging Man!')
    while True:
        user_name = input('Please enter your name: \n').capitalize()
        if user_name.isalpha():
            break
        else:
            # Handles invalid input by the user
            print(f'\nSorry, {Fore.RED}{Style.BRIGHT}{user_name}{Fore.RESET}{Style.RESET_ALL} is not a valid name')  # noqa
            print(f'Please use alphabetic characters only.\n')

    run_story(story.intro)

    while True:
        # Loop to ask user if they would like to play
        user_input = input(f'So {user_name}, do you accept the challange? (Y/N) \n').upper()  # noqa
        clear()

        if user_input == 'N':
            print('\nGoodbye!')
            quit()
        elif user_input == 'Y':
            print("\nGreat! Let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print(f'\nSorry, {Fore.RED}{Style.BRIGHT}{user_input}{Fore.RESET}{Style.RESET_ALL} is an invalid input.')  # noqa
            print('Please enter Y or N.\n')

    return difficulty, user_name


def display_word(word, letters_guessed):
    """
    Function to loop through each letter in
    the word and show each letter that has been
    correctly guessed by the user, and to
    hide all other letters, function will
    then return the word
    """
    displayed_word = ''
    for letter in word:
        if letter in letters_guessed:
            displayed_word += letter
        else:
            displayed_word += '_'

    return displayed_word


def play(word, user_name):
    """
    Main function to play the game.
    Has an input to take the guess from the user
    which is then validated and stored in a variable.
    Other functions are then called to handle the
    users guess, and checks the users input is valid.
    """
    word_completion = '_' * len(word)
    global GUESSED
    GUESSED = False
    guessed_letters = []
    guessed_words = []
    global TRIES
    TRIES = 6

    print(display_hangman(TRIES))
    print(display_word(word_completion, guessed_letters))
    print(f'\nThe word is {len(word)} letters long')

    while not GUESSED and TRIES > 0:
        guess = input('Please guess a letter or the full word: \n').upper()
        clear()

        if len(guess) == 1 and guess.isalpha():
            word_completion = letter_guess(guess, word, word_completion, guessed_letters)  # noqa
        elif len(guess) > 1 and guess.isalpha():
            word_guess(guess, word, word_completion, guessed_words)
        else:
            # Handles invalid input by the user
            print(f'\nOh no! {Fore.RED}{Style.BRIGHT}{guess}{Fore.RESET}{Style.RESET_ALL} is not a valid guess!')  # noqa
            print('Please guess a letter or word using only letters!')

        print(display_hangman(TRIES))
        print(display_word(word_completion, guessed_letters))
        # Displays the length of word if the user has tries left
        if TRIES > 0:
            print(f'\nThe word is {len(word)} letters long')

    game_end(word, user_name)


def letter_guess(guess, word, word_completion, guessed_letters):
    """
    Function to handle when the user guesses a word.
    Checks for duplicate inputs.
    Uses colorama to display feedback to the user in the relevant
    colour dependant if the input is correct or not.
    """
    global TRIES
    global GUESSED
    if guess in guessed_letters:
        # Handles duplicate inputs by the user
        print(f'\nYou already guessed the letter {guess}, silly!')
    elif guess not in word:
        print(f'\nOhh dear... {Fore.RED}{Style.BRIGHT}{guess}{Fore.RESET}{Style.RESET_ALL}, is not in the word')  # noqa
        TRIES -= 1
        guessed_letters.append(guess)
    else:
        print(f'\nWell done! {Fore.GREEN}{Style.BRIGHT}{guess}{Fore.RESET}{Style.RESET_ALL} is in the word!')  # noqa
        guessed_letters.append(guess)
        word_completion = update_word(word, guess, word_completion)
        if '_' not in word_completion:
            GUESSED = True

    return word_completion


def word_guess(guess, word, word_completion, guessed_words):
    """
    Function to handle when the user guesses a word.
    Checks for duplicate inputs.
    Uses colorama to display feedback to the user in the relevant
    colour dependant if the input is correct or not.
    """
    global TRIES
    global GUESSED
    if guess in guessed_words:
        # Handles duplicate inputs by the user
        print(f'\nYou already guessed the word {guess}, silly!')
    elif guess != word:
        print(f'\nOhh dear... {Fore.RED}{Style.BRIGHT}{guess}{Fore.RESET}{Style.RESET_ALL}, is not the word')  # noqa
        TRIES -= 1
        guessed_words.append(guess)
    else:
        GUESSED = True
        word_completion = word


def update_word(word, guess, word_completion):
    """
    Function to update the game word,
    replaces the underscores with the letter
    if the letter is correct.
    Code borrowed from Youtube tutorial:
    https://www.youtube.com/watch?v=m4nEnsavl6w&list=PLVVxU9zkt8071XW8qgYXv_62rgO-HwRal&index=5&t=491s
    """
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    return "".join(word_as_list)


def game_end(word, user_name):
    """
    Function to handle the end of the game.
    Displays message to the user to let them know
    if they won or failed.
    Return message uses colorama to change the name
    and word the relevant colour depending on the outcome.
    """
    global GUESSED
    if GUESSED:
        print(f'\n{Fore.GREEN}{Style.BRIGHT}Well done {user_name}{Fore.RESET}{Style.RESET_ALL}!')  # noqa
        print(f'The word was {Fore.GREEN}{Style.BRIGHT}{word}{Fore.RESET}{Style.RESET_ALL}! You saved Hank!\n')  # noqa
    else:
        print(f'\n{Fore.RED}{Style.BRIGHT}Sorry {user_name}{Fore.RESET}{Style.RESET_ALL}')  # noqa
        print(f'You ran out of tries, the word was {Fore.GREEN}{Style.BRIGHT}{word}{Fore.RESET}{Style.RESET_ALL}\n')  # noqa


def replay():
    """
    Function to handle replaying the game,
    changing the difficulty should the user choose to,
    and checking the users input is valid
    """
    while True:
        user_input = input('Would you like to play again? (Y/N) \n').upper()
        clear()

        if user_input == 'N':
            print('\nGoodbye!')
            quit()
        elif user_input == 'Y':
            print("\nGreat! Let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print(f'\n{Fore.RED}{Style.BRIGHT}{user_input}{Fore.RESET}{Style.RESET_ALL} is not a valid input.')  # noqa
            print('Please enter Y or N.\n')

    return difficulty


def display_hangman(tries):
    """
    Function to display hangman phases.
    Also removes indent from hangman graphic.    
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
        # Phase 6, when tries = 1
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
        # Phase 4, when tries = 3
        # Noose, head, torso, arm
        textwrap.dedent("""
            ________
            |/     |
            |      😨
            |     /|
            |
            |
        """),
        # Phase 3, when tries = 4
        # Noose, head, torso
        textwrap.dedent("""
            ________
            |/     |
            |      😩
            |      |
            |
            |
        """),
        # Phase 2, when tries = 5
        # Noose, head
        textwrap.dedent("""
            ________
            |/     |
            |      😲
            |
            |
            |
        """),
        # Phase 1, game start when tries = 6
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
    """
    Main function to run the game
    """
    selected_difficulty, user_name = welcome()
    word = get_word(selected_difficulty)
    play(word, user_name)

    # Loop to ask the user if they want to play again
    while True:
        replay_difficulty = replay()
        if replay_difficulty is None:
            print('Thanks for playing! Goodbye!')
            break
        else:
            replay_word = get_word(replay_difficulty)
            play(replay_word, user_name)


main()
