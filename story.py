# File to store all story narratives and instructions

#Import colorama to change font colour
from colorama import Fore, Style

# Game instructions
instructions = """
You will first select your difficulty of either easy, medium or hard.
Then you will be presented with an image of a empty noose and
blank lines representing a random word. It is your job to guess the word.
You can guess either a letter or the whole word on each turn but you
will only have six guesses before you lose the game.
Each time you guess a letter correctly it will replace one of the blank
lines and display that letters position in the hidden word.
At any point you can try to guess the entire word.
If guessed correctly it means you win the game!
But with every incorrect guess a new body part will appear on the empty noose.
There are six body parts to be added in total.
If you end up with the entire body on the noose you lose the game!)
"""

# Intoduction narrative
intro = """
The year is 1705 and you were just in the middle of taking your annual bath,
when suddenly you get a knock at the door because your good buddy Hank has
got himself into a bit of a pickle! The villagers say that Hank is a bit of
an idiot, and is bringing down peoples perception of the community!
So they have taken it upon themselves to hang him in the town square!
The only way they will let Hank live is if you agree to take him in and teach
him how to function As a human being! But in order to do that the villagers
need to make sure that you are not an idiot as well! So they challenge
you to a game of hangman... (ironic eh?), to prove your intelligence!\n
Do you accept the challenge? Or shall you let Hank hang for his stupidity?\n
Type Y to accept and save Hank!
Type N to admit you are also an idiot, and let Hank hang!
P.S. Admitting you are also an idiot, may result in your own hanging!
"""

# Narrative for easy difficulty
easy = f"""
{Fore.GREEN}{Style.BRIGHT}Oh so you chose easy eh? 🤨{Fore.RESET}{Style.RESET_ALL}\n
Hank thought that you were the smart one, but now he's not sure...
he starts sweating as they put the noose around his neck!
"""

# Narrative for medium difficulty
medium = f"""
{Fore.CYAN}{Style.BRIGHT}Ok, so you have chosen medium 🙂{Fore.RESET}{Style.RESET_ALL}\n
Hank is somewhat filled with confidence, but has to consider that
you are neither confirming or denying your intelligence…
He hopes you’re not this indecisive while playing!
His life depends on it!
"""

# Narrative for hard difficulty
hard = f"""
{Fore.RED}{Style.BRIGHT}Well look at this, you have chosen hard 🤓{Fore.RESET}{Style.RESET_ALL}\n
Hank is filled with the upmost confidence in you!
But has to consider that you have just made the game that
decides his fate even harder for yourself!
Let’s hope this bravery pays off…
Hanks life depends on it!
"""

# Different narratives to be printed for certain points in game
# Narratives for hangman phase 3
phase_three = [
    "Hank is starting to worry now!",
    "Hank wishes he had a smarter best friend!",
    "Hank asks if he can pick someone else to play!",
    "Hank is starting to sweat a little!",
    "Hank wishes you had listened more in school!",
    "Hank says that you can do better than this!",
    "Hank would like you to think a bit more before answering!",
    "Hank says he wishes you could swap because even he could do better!"
]

# Narratives for hangman phase five
phase_five = [
    "Hank thinks that you should have chose an easier difficulty!",
    "Hank is dripping with sweat now!",
    "Hank is starting to lose hope!",
    "Hank wants to remind you his life is on the line!",
    "Hank says that your the true village idiot and not him!",
    "Hank says that your stupidity will be the death of him!",
    "Hank can't believe what a poor effort your giving!",
    "Hank would like to swap you for the town pig!"
]

# Narratives for hangman phase six
phase_six = [
    "'It looks like this is the end!' cries Hank!",
    "'Im giving up hope' Hank cries",
    "'It was fun while it lasted' Hank thinks to himself",
    "'Can you do no better!?' Hank screams",
    "'One more and im gone!' screams Hank",
    "'Are you trying to let me hang!?' cries Hank",
    "'What did I do to deserve such a stupid friend' wonders Hank",
    "'Please think carefully about this last one!' shouts Hank"
]
