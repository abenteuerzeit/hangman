import random
from stages import stages


def get_words():
    with open('countries-and-capitals.txt') as file:
        return [line.strip() for line in file]


def get_hangman_art():
    return stages


def get_logo():
    with open('art.txt') as file:
        return file.read()


def generate_hangman_art(difficulty):
    num_stages = min(int(difficulty / 100 * len(stages)), len(stages))
    hangman_art = []
    for i in range(num_stages):
        hangman_art.append(stages[i])
    hangman_art.append('GAME OVER')
    return hangman_art


def display_title_screen():
    print(get_logo())
    print("Welcome to Hangman!")


def get_game(difficulty):
    words = get_words()
    word = random.choice(words)
    if difficulty == 'easy':
        lives = 8
    elif difficulty == 'medium':
        lives = 6
    elif difficulty == 'hard':
        lives = 4
    elif difficulty == 'expert':
        lives = 2
    else:
        lives = int(difficulty)
    hangman_art = get_hangman_art()
    return (lives, word, hangman_art)


def play_game(game):
    lives, word, hangman_art = game
    display = ['_'] * len(word)
    guesses = set()
    print(get_logo())
    print(' '.join(display))
    print(hangman_art[0])
    while True:
        guess = input("Guess a letter: ").lower()

        if guess == 'quit':
            print("Goodbye!")
            return

        if len(guess) != 1 or not guess.isalpha() or guess in guesses:
            print("Invalid guess. Please try again.")
            continue
        guesses.add(guess)

        if guess in word.lower():
            for i in range(len(word)):
                if word[i].lower() == guess:
                    display[i] = word[i]
        else:
            lives -= 1

        if '_' not in display:
            print("You win!")
            return
        elif lives < 0:
            print(hangman_art[-1])
            return

        print(' '.join(display))
        print(hangman_art[len(hangman_art) - lives - 1])


def play_hangman():
    print(get_logo())
    difficulty = choose_difficulty()
    game = get_game(difficulty)
    play_game(game)


def main():
    display_title_screen()
    difficulty = choose_difficulty()
    game = get_game(difficulty)
    play_game(game)


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


if __name__ == '__main__':
    main()
