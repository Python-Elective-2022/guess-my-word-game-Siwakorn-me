# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish .
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list


def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)


# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program


word_list = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """

    count = 0
    for letters in secret_word:
        if letters in letters_guessed:
            pass
        else:
            return False
    return True


print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
print(is_word_guessed('pineapple', []))


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    """

    guess_string = ''

    for letter in secret_word:
        if letter in letters_guessed:
            guess_string += letter
        else:
            guess_string += '_ '
    return guess_string


# Testcases
print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))


def get_available_letters(letters_guessed):
    """
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE...
    not_guessed = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            not_guessed += letter
    return not_guessed


# Testcases
print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))


def game_loop(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """

    print("Let the game begin!")
    print("I am thinking of a word with " + str(len(secret_word)) + " letters.", end="\n\n")
    letters_guessed = []
    guesses_left = 8
    while guesses_left != 0:
        print("You have " + str(guesses_left) + " guesses left.")
        print("Letters available to you: " + get_available_letters(letters_guessed))
        current_guess = input("Guess a letter: ")
        print(current_guess.lower())
        if current_guess.lower() in letters_guessed:
            print("You fool! You tried this letter already: " + (get_guessed_word(secret_word, letters_guessed)))
            print(end="\n\n")
        elif current_guess.lower() in secret_word:
            letters_guessed += current_guess.lower()
            print("Correct: " + get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            print(end="\n\n")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("You WIN")
                break
        else:
            letters_guessed += current_guess.lower()
            print("Incorrect, this letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            guesses_left -= 1
            print(end="\n\n")
    if guesses_left == 0:
        print("GAME OVER ! The word was " + secret_word + ".")


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)


# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()
