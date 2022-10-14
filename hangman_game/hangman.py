import random
import string
from words import words
'''from filename import variable'''


def get_valid_word(words):
    word = random.choice(words)
    while ("-" in word) or (" " in word):
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print("You have used these letters:", ' '.join(used_letters))
        # '<separator>'.join(<iterable Data Structue>)

        # curraent word
        word_list = [
            letter if letter in used_letters else "_" for letter in word]
        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in (alphabet - used_letters):
            # if used letter is in alphabet but not in used_letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that character.Please Try Another.")
        else:
            print("You just typed an Invalid Character")
    # while the length if word letters > 0, iterate


hangman()
