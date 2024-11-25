import random

def get_random_word():
    with open('10-wordle/valid-wordle-words.txt', 'r') as f:
        words = f.readlines()

    word = random.choice(words).strip()  # Remove newline characters
    return word

def get_valid_input(valid_words):
    in_word = input('Enter guess: ')
    if in_word.lower() in valid_words:
        return in_word.lower()
    else:
        print('That is not a valid word. Please try again.')
        return get_valid_input(valid_words)
