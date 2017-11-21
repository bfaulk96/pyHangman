import getpass

PLAYING = True

NEW_BOARD = """
  ___________
  |          |
  |                  LIVES LEFT: {0}
  |                  LETTERS GUESSED: {1}
  |                     
  |
  |
  |
 _|_
|   |__________
|              |
|______________|
"""

EASY_DISPLAY = [
    """
  ___________
  |          |
  |       (x _ x)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (*   *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (*    )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |
  |         /
 _|_       /
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |        
  |
 _|_
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (     )    LIVES LEFT: {0}
  |                  LETTERS GUESSED: {1}
  |                     
  |
  |
  |
 _|_
|   |__________
|              |
|______________|
    """,
    NEW_BOARD
]

MEDIUM_DISPLAY = [
    """
  ___________
  |          |
  |       (x _ x)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |
  |         /
 _|_       /
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |        
  |
 _|_
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |                  LETTERS GUESSED: {1}
  |                     
  |
  |
  |
 _|_
|   |__________
|              |
|______________|
    """,
    NEW_BOARD
]

HARD_DISPLAY = [
    """
  ___________
  |          |
  |       (x _ x)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |      /---|---\         
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |
  |         / \\
 _|_       /   \\
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |          |       LETTERS GUESSED: {1}
  |          |          
  |          |
  |          |        
  |
 _|_
|   |__________
|              |
|______________|
    """,
    """
  ___________
  |          |
  |       (* _ *)    LIVES LEFT: {0}
  |                  LETTERS GUESSED: {1}
  |                     
  |
  |
  |
 _|_
|   |__________
|              |
|______________|
    """,
    NEW_BOARD
]


# class colors:
#     HEADER = '\033[95m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'


def show_phrase(phrase, letters):
    num_correct = 0
    for char in phrase.lower():
        if char in [' ', '.', '?', ',', '!']:
            print(char + ' ', end='', flush=True)
            num_correct += 1
        elif char in letters:
            print(char + ' ', end='', flush=True)
            num_correct += 1
        else:
            print('_ ', end='', flush=True)
    print('\n')
    return num_correct


def print_display(display, shouldDisplay, lives, letters):
    if should_display:
        print(display[LIVES].format(LIVES, ', '.join(sorted(letters))))
    else:
        print("LIVES LEFT: " + str(LIVES))
        print("LETTERS GUESSED: " + ', '.join(sorted(letters)))
    print('')


print("""
  _    _          _   _  _____ __  __          _   _ 
 | |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
 | |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
 |  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
 | |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
 |_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
                                                     
""")

while PLAYING:
    mode = input('Select a mode. Easy (E), Medium (M), Hard (H): ')
    letters = []
    display = None
    if mode in ['M', 'm', 'medium', 'Medium']:
        LIVES = 7
        display = MEDIUM_DISPLAY
        print("Medium Mode. 7 lives.")
    elif mode in ['H', 'h', 'hard', 'Hard']:
        LIVES = 5
        display = HARD_DISPLAY
        print("Hard Mode. 5 lives.")
    else:
        LIVES = 10
        display = EASY_DISPLAY
        print("Easy Mode. 10 lives.")

    playAgain = input("Would you like to display hangman? (Y/N): ")
    if playAgain in ['Y', 'y', 'yes', 'Yes', 'Yeah', 'yeah']:
        should_display = True
    else:
        should_display = False

    phrase = getpass.getpass('Enter a word or phrase:')
    print("HANGMAN WILL NOW BEGIN.\n")

    correct_num = 0
    WINNER = False
    while not WINNER:
        correct_num = show_phrase(phrase, letters)
        if correct_num == len(phrase):
            WINNER = True
            break
        guess = None
        while guess is None or guess in letters:
            guess = input('Please guess a new letter: ')
        print('')
        letters.append(guess.lower())
        if guess.lower() in phrase.lower():
            print_display(display, should_display, LIVES, letters)
            print("Good job. You guessed a letter in the phrase.")
        else:
            LIVES -= 1
            print_display(display, should_display, LIVES, letters)
            if LIVES == 0:
                break
            print("That letter is not in the phrase. Try again.")

    if WINNER:
        print("You guessed the phrase! Great job! The phrase was:\n\"" + phrase + "\"")
        print("You had " + str(LIVES) + ' lives remaining.')
    else:
        print("You lost! The phrase was:\n\"" + phrase + "\"")

    playAgain = input("Would you like to play again? (Y/N): ")
    if playAgain in ['Y', 'y', 'yes', 'Yes', 'Yeah', 'yeah']:
        print('')
        continue
    else:
        PLAYING = False
