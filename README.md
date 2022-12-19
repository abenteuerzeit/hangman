# Hangman

A classic hangman game where the player has to guess a country, capital, or both depending on the difficulty level.

## Dependencies

This code requires the codecs and ASCII_ART modules. ASCII_ART contains ASCII art for the hangman game.

## Modes

There are four difficulty levels:

1. Easy: Guess a country
2. Medium: Guess a capital
3. Hard: Guess both a country and its capital
4. Expert: Guess a country and its capital with only 2 lives

## How to play

To play, run the main.py file. Select a difficulty level by entering a number between 1 and 3. You will then see a list of underscores representing the letters of the word you have to guess. Enter a letter and the game will either reveal the letter in the word or reduce your lives if the letter is not present in the word. The game continues until you guess all the letters in the word or run out of lives.

## Customization

You can customize the game by adding or changing the words in the countries-and-capitals.txt file. Each line in the file should contain a country and its capital separated by a |.

Good luck!
