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
            print("Great! Let's choose the difficulty...\n")
            difficulty = select_difficulty()
            break
        else:
            # Handles invalid input by the user
            print(f'{user_input} is an invalid input. Please enter Y or N.\n')

    return difficulty


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


def play(word):
    """
    Main function to play the game,
    has an input to take the guess from the user
    which is then validated and stored in a variable,
    other functions are then called to handle the 
    users guess.
    """
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's save Hank!")
    print(display_hangman(tries))
    print(display_word(word_completion, guessed_letters))
    print('\n')

    while not guessed and tries > 0:
        guess = input('Please guess a letter or the full word: ').upper()

        if len(guess) == 1 and guess.isalpha():
            word_completion = letter_guess(guess, word, word_completion, guessed, guessed_letters, tries)
        elif len(guess) == len(word) and guess.isalpha():
            word_guess(guess, word, word_completion, guessed, guessed_words, tries)
        else:
            print('Oh no! This is not a valid guess!')
            print('Please guess a letter or word using only letters!')

        print(display_hangman(tries))
        print(display_word(word_completion, guessed_letters))
        print('\n')

    game_end(guessed, word)
        

def letter_guess(guess, word, word_completion, guessed, guessed_letters, tries):
    if guess in guessed_letters:
        print(f'You already guessed the letter {guess}, silly!')
    elif guess not in word:
        print(f'Ohh dear... {guess}, is not in the word')
        tries -= 1
        guessed_letters.append(guess)    
    else:
        print(f'Well done! {guess} is in the word!')
        guessed_letters.append(guess)
        word_completion = update_word(word, guess, word_completion)
        if '_' not in word_completion:
            guessed = True
    
    return word_completion


def word_guess(guess, word, word_completion, guessed, guessed_words, tries):
    if guess in guessed_words:
        print(f'You already guessed the word {guess}, silly!')
    elif guess != word:
        print(f'Ohh dear... {guess}, is not the word')
        tries -= 1
        guessed_words.append(guess)
    else:
        guessed = True
        word_completion = word
    

def update_word(word, guess, word_completion):
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    return "".join(word_as_list)


def game_end(guessed, word):
    if guessed:
        print('Well done you saved Hank!')
    else:
        print(f'Sorry you ran out of tries, the word was {word}')


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
    play(word)
    

main()

