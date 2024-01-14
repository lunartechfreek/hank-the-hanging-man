import random
import words 
import story
import textwrap


global TRIES
global GUESSED

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
        user_input = input('Please type E, M or H \n').upper()  

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
            print(f'\nSorry, {user_input} is not a valid input.')
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
            print(f'\nSorry, {user_name} is not a valid name')
            print(f'Please use alphabetic characters only.\n')

    run_story(story.intro)

    while True:
        # Loop to ask user if they would like to play
        user_input = input(f'So {user_name}, do you accept the challange? (Y/N) \n').upper()  

        if user_input == 'N':
            print('\nGoodbye!')
            quit()
        elif user_input == 'Y':
            print("\nGreat! Let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print(f'\nSorry, {user_input} is an invalid input.')
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
    Main function to play the game,
    has an input to take the guess from the user
    which is then validated and stored in a variable,
    other functions are then called to handle the 
    users guess.
    """
    word_completion = '_' * len(word)
    global GUESSED
    GUESSED = False
    guessed_letters = []
    guessed_words = []
    global TRIES
    TRIES = 6

    print("Let's save Hank!")
    print(display_hangman(TRIES))
    print(display_word(word_completion, guessed_letters))
    print(f'\nThe word is {len(word)} letters long')

    while not GUESSED and TRIES > 0:
        guess = input('Please guess a letter or the full word: \n').upper()

        if len(guess) == 1 and guess.isalpha():
            word_completion = letter_guess(guess, word, word_completion, guessed_letters)
        elif len(guess) > 1 and guess.isalpha():
            word_guess(guess, word, word_completion, guessed_words)
        else:
            print(f'\nOh no! {guess} is not a valid guess!')
            print('Please guess a letter or word using only letters!')

        print(display_hangman(TRIES))
        print(display_word(word_completion, guessed_letters))
        if TRIES > 0:
            print(f'\nThe word is {len(word)} letters long')

    game_end(word, user_name)
        

def letter_guess(guess, word, word_completion, guessed_letters):
    global TRIES
    global GUESSED
    if guess in guessed_letters:
        print(f'You already guessed the letter {guess}, silly!')
    elif guess not in word:
        print(f'Ohh dear... {guess}, is not in the word')
        TRIES -= 1
        guessed_letters.append(guess)    
    else:
        print(f'Well done! {guess} is in the word!')
        guessed_letters.append(guess)
        word_completion = update_word(word, guess, word_completion)
        if '_' not in word_completion:
            GUESSED = True
    
    return word_completion


def word_guess(guess, word, word_completion, guessed_words):
    global TRIES
    global GUESSED
    if guess in guessed_words:
        print(f'You already guessed the word {guess}, silly!')
    elif guess != word:
        print(f'Ohh dear... {guess}, is not the word')
        TRIES -= 1
        guessed_words.append(guess)
    else:
        GUESSED = True
        word_completion = word

    
    

def update_word(word, guess, word_completion):
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    return "".join(word_as_list)


def game_end(word, user_name):
    global GUESSED
    if GUESSED:
        print(f'\nWell done {user_name}!')
        print(f'The word was {word}! You saved Hank!\n')
    else:
        print(f'\nSorry {user_name}')
        print(f'You ran out of tries, the word was {word}\n')


def replay():
    """
    Function to handle replaying the game,
    changing the difficulty should the user choose to,
    and checking the users input is valid
    """
    while True:
        # Loop to ask user if they would like to play again
        user_input = input('Would you like to play again? (Y/N) \n').upper()  

        if user_input == 'N':
            print('\nGoodbye!')
            quit()
        elif user_input == 'Y':
            print("\nGreat! Let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print(f'\n{user_input} is not a valid input.')
            print('Please enter Y or N.\n')

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
    selected_difficulty, user_name = welcome()
    word = get_word(selected_difficulty)
    play(word, user_name)

    while True:
        replay_difficulty = replay()
        if replay_difficulty is None:
            print('Thanks for playing! Goodbye!')
            break
        else:
            replay_word = get_word(replay_difficulty)
            play(replay_word, user_name)
    

main()


