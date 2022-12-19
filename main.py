import os
import subprocess
import random
import re
import codecs
from ASCII_ART import ASCII_ART

difficulty_levels = [
    ('easy', 8),
    ('medium', 6),
    ('hard', 4),
    ('expert', 2)
]


def clear_screen():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


def display_title_screen():
    print(get_logo())
    print("Welcome to Hangman!")


def display_guesses(guesses):
    print("Guesses: " + ', '.join(guesses))


def display_lives(lives):
    print(f"Lives: {' '.join([chr(9829) for _ in range(lives)])}")


def get_game(difficulty):
    return (get_lives(difficulty), get_secret(difficulty))


def get_lives(difficulty):
    for level, lives in difficulty_levels:
        if level == difficulty:
            return lives
    return int(difficulty) if difficulty.isdigit() else None


def get_logo():
    with open('art.txt') as file:
        return file.read()


def get_words():
    with codecs.open('countries-and-capitals.txt', encoding='utf-8') as file:
        return [line.strip() for line in file]


def choose_difficulty():
    print("Select a difficulty level:")
    print("1. Easy (guess a country)")
    print("2. Medium (guess a capital)")
    print("3. Hard (guess both a country and its capital)")
    while True:
        selection = input("Select a difficulty level (1-3): ")
        if selection in {'1', '2', '3'}:
            return difficulty_levels[int(selection) - 1][0]
        print("Invalid selection. Please enter a number between 1 and 3.")


def get_secret(difficulty):
    words = get_words()
    word_index = random.randint(0, len(words) - 1)
    country, city = words[word_index].split(' | ')
    secrets = {
        "easy": (country, words[word_index]),
        "medium": (city, words[word_index]),
        "hard": (country + city, words[word_index])
    }
    secret_word, full_answer = secrets[difficulty]
    secret_word = ''.join(c for c in secret_word if c.isalpha())
    return secret_word, full_answer


def is_valid_guess(guess, guesses):
    return len(guess) == 1 and guess.isalpha() and guess not in guesses


def display_game_state(display, misses, guesses, lives):
    # TODO The output is not displaying properly. THere are bugs. Need to consider the difficulty settings
    clear_screen()
    print(ASCII_ART[min(misses, len(ASCII_ART) - 1)])

    if len(display) > 1:
        city = display[0]
        country = display[1]
        # print the city and country strings separately
        output = "\n" + ' '.join(c if c.lower() in guesses else '_' for c in city) + '\n'
        output += ' '.join(c if c.lower() in guesses else '_' for c in country)
    elif len(display) == 1:
        city = display[0]
        output = "\n" + ' '.join(c if c.lower() in guesses else '_' for c in city)
    else:
        output = "\n"
    print(f"\t{output}\n")
    display_guesses(guesses)
    display_lives(lives)


def process_guess(guess, answer_key, display, lives, guesses, misses):
    if guess not in answer_key:
        guesses.add(guess)
    result_chars = []
    for c in answer_key:
        if c.lower() == guess:
            result_chars.append(c)
        else:
            result_chars.append('_')
    if guess not in answer_key.lower():
        lives -= 1
        misses += 1
    return lives, guesses, misses, result_chars


def is_game_over(hidden, lives):
    return '_' not in hidden or lives < 0


def play_game(game):
    lives, (answer_key, answer_formatted) = game
    pattern = r"([A-Z][a-zA-Z ]+)|([A-Z][a-zA-Z ]+)"
    display = [match.group() for match in re.finditer(pattern, answer_formatted)]
    guesses = set()
    clear_screen()
    print(ASCII_ART[0])
    print("Secret: " + ' '.join(display))
    misses = 0
    running = True
    while running:
        display_game_state(display, misses, guesses, lives)
        guess = input("Guess a letter: ").lower()
        if guess == 'quit':
            print("Goodbye!")
            return
        if not is_valid_guess(guess, guesses):
            misses += 1
            print("Invalid guess. Please try again.")
            continue
        lives, guesses, misses, hidden = process_guess(guess, answer_key, display, lives, guesses, misses)
        if is_game_over(hidden, lives):
            running = False
            clear_screen()
            if '_' not in hidden:
                print("You win!")
                print(ASCII_ART[0])
            else:
                print("You lose!")
                print(ASCII_ART[-1])
            print(f"The secret word was {answer_key} for the country and city: {answer_formatted}")


def run_game():
    display_title_screen()
    input('Press any key to continue...')
    clear_screen()
    difficulty = choose_difficulty()
    game = get_game(difficulty)
    play_game(game)


# Main program
if __name__ == '__main__':
    run_game()
