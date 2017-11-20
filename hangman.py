import getpass
import pythonHangman

PLAYING = True


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


def show_guesses(letters):
    if letters:
        print('LETTERS GUESSED: ', end='', flush=True)
        for index, l in enumerate(sorted(letters)):
            if index == len(letters)-1:
                print(l)
            else:
                print(l + ', ', end='', flush=True)

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
    if mode in ['M', 'm', 'medium', 'Medium']:
        LIVES = 7
        print("Medium Mode. 7 lives.")
    elif mode in ['H', 'h', 'hard', 'Hard']:
        LIVES = 5
        print("Hard Mode. 5 lives.")
    else:
        LIVES = 10
        print("Easy Mode. 10 lives.")

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
        if guess.lower() in phrase.lower():
            print("Good job. You guessed a letter in the phrase.")
        else:
            LIVES -= 1
            if LIVES == 0:
                break
            print("That letter is not in the phrase. Try again.")
        print("LIVES LEFT: " + str(LIVES))
        letters.append(guess.lower())
        show_guesses(letters)
        print('')

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