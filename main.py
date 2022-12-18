import random
from stages import stages
import os

difficulty_levels = {
    'easy': 8,
    'medium': 6,
    'hard': 4,
    'expert': 2
}


# Helper functions
def choose_difficulty():
    print("Select a difficulty level:")
    print("1. Easy (8 lives)")
    print("2. Medium (6 lives)")
    print("3. Hard (4 lives)")
    print("4. Expert (2 lives)")
    print("5. Custom (Enter your own number of lives)")
    while True:
        selection = input("Selecte a difficulty level (1-5) or enter your own number of lives: ")
        if selection == '1':
            return 'easy'
        elif selection == '2':
            return 'medium'
        elif selection == '3':
            return 'hard'
        elif selection == '4':
            return 'expert'
        elif selection == '5':
            print("Enter the number of lives:")
            return input()
        print("Invalid selection. Please enter a number between 1 and 5.")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title_screen():
    print(get_logo())
    print("Welcome to Hangman!")


def get_game(difficulty):
    return (get_lives(difficulty), random.choice(get_words()))


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
    print(stages[min(misses, len(stages) - 1)])
    print(' '.join(display))
    display_guesses(guesses)
    display_lives(lives)


def play_game(game):
    lives, word = game
    display = ['_'] * len(word)
    guesses = set()
    clear_screen()
    print(stages[0])
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
            if '_' not in display:
                print("You win!")
                print(stages[0])
            else:
                print("You lose!")
                print(stages[-1])


def main():
    display_title_screen()
    input('Press any key to continue...')
    clear_screen()
    difficulty = choose_difficulty()
    game = get_game(difficulty)
    play_game(game)


if __name__ == '__main__':
    main()
