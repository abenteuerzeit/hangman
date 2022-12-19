import random
import os
from stages import stages as ASCII_ART

difficulty_levels = {
    'easy': 8,
    'medium': 6,
    'hard': 4,
    'expert': 2
}


# Helper functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title_screen():
    print(get_logo())
    print("Welcome to Hangman!")


def get_game(difficulty):
    return (get_lives(difficulty), get_secret(difficulty))


def get_lives(difficulty):
    if difficulty.isdigit():
        return int(difficulty)
    else:
        return difficulty_levels.get(difficulty)


def get_logo():
    with open('art.txt') as file:
        return file.read()


def get_words():
    with open('countries-and-capitals.txt') as file:
        return [line.strip() for line in file]


def choose_difficulty():
    print("Select a difficulty level:")
    print("1. Easy (guess a country)")
    print("2. Medium (guess a capital)")
    print("3. Hard (guess both a country and its capital)")
    while True:
        selection = input("Selecte a difficulty level (1-3): ")
        if selection == '1':
            return 'easy'
        elif selection == '2':
            return 'medium'
        elif selection == '3':
            return 'hard'
        print("Invalid selection. Please enter a number between 1 and 3.")


def get_secret(difficulty):
    words = get_words()
    word_index = random.randint(0, len(words) - 1)
    country, city = words[word_index].split(' | ')
    secret = {
        "easy": country,
        "medium": city,
        "hard": country + city
    }
    return secret[difficulty], words[word_index]


def is_valid_guess(guess, guesses):
    return len(guess) == 1 and guess.isalpha() and guess not in guesses


def display_guesses(guesses):
    print("Guesses: " + ', '.join(guesses))


def display_lives(lives):
    print(f"Lives: {' '.join([chr(9829) for _ in range(lives)])}")


def process_guess(guess, word, display, lives, guesses, misses):
    guesses.add(guess)
    if guess in word.lower():
        return [word[i] if word[i].lower() == guess else display[i] for i in range(len(word))], lives, guesses, misses
    else:
        return display, lives - 1, guesses, misses + 1


def is_game_over(display, lives):
    return '_' not in display or lives < 0


def display_game_state(display, misses, guesses, lives):
    clear_screen()
    print(ASCII_ART[min(misses, len(ASCII_ART) - 1)])
    print(' '.join(display))
    display_guesses(guesses)
    display_lives(lives)


def play_game(game):
    lives, (word, answer) = game
    display = ['_'] * len(word)
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
        display, lives, guesses, misses = process_guess(guess, word, display, lives, guesses, misses)
        if is_game_over(display, lives):
            running = False
            clear_screen()
            if '_' not in display:
                print("You win!")
                print(ASCII_ART[0])
            else:
                print("You lose!")
                print(ASCII_ART[-1])
            print(f"The secret word was {word} for the country and city: {answer}")


# Main program
if __name__ == '__main__':
    display_title_screen()
    input('Press any key to continue...')
    clear_screen()
    difficulty = choose_difficulty()
    game = get_game(difficulty)
    play_game(game)
