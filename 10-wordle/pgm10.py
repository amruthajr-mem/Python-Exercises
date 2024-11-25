from colorama import init, Back
from demo import get_random_word, get_valid_input
import copy

print('-----------------Wordle----------------')

init(autoreset=True)
word = get_random_word()

with open('10-wordle/valid-wordle-words.txt', 'r') as f:
    valid_words = f.read().splitlines()

word_map = {}
for idx, char in enumerate(word):
    if char in word_map:
        word_map[char].append(idx)
    else:
        word_map[char] = [idx]

guesses = []
answered = False
attempts = 6
while len(guesses) < attempts:
    print(f'Attempts remaining: {attempts - len(guesses)}')
    input_word = get_valid_input(valid_words)

    word_map_copy = copy.deepcopy(word_map)
    printls = []
    for idx, char in enumerate(input_word):
        if char in word_map_copy and word_map_copy[char]:  # Handling matching positions
            for pos in word_map_copy.get(char):
                if pos == idx:
                    printls.append(Back.BLUE + f' {char.upper()} ')  # Changed GREEN to BLUE
                    word_map_copy[char].remove(pos)  # Correct position
                    break
            else:
                word_map_copy[char].remove(pos)  # Incorrect position
                printls.append(Back.MAGENTA + f' {char.upper()} ')  # Changed YELLOW to MAGENTA
        else:
            printls.append(Back.WHITE + f' {char.upper()} ')  # Incorrect character

    guesses.append(printls)
    print("\nYour Guesses So Far:")
    for guess in guesses:
        print(''.join(guess))  # Print guesses in a single line for clarity
    print('------------------------------------------------------------')

    if input_word == word.lower():
        print("\n🎉 CONGRATULATIONS! You've guessed the correct word! 🎉")
        answered = True
        break

if not answered:
    print(f'\nThe correct word was: {Back.BLUE} {word.upper()}')
    print('Better luck next time! Thank you for playing. 😊')


