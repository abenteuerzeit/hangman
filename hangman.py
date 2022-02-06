import random

INDEX_CAPITAL = 1
INDEX_COUNTRY = 0

def random_word():
    # TODO try to rewrite this and use 'with' keywords to open file

    countries_and_capitals_file = open("countries-and-capitals.txt", "r")
    content_list = countries_and_capitals_file.readlines()
    countries_and_capitals_file.close()
    random.shuffle(content_list)
    line = content_list[0].strip()
    words = line.split(" | ")
    return words

def display_hangman_step(count):
      # TODO try to rewrite this and use 'with' keywords to open file
      new_count = count + 1
      f = open(f"gallows_{new_count}.txt", "r")
      print(f.read())
      f.close() 
      print(f"guess {new_count}")
      return new_count

def hangman_game(word):
      # Stores the letters to be displayed
      word_display = []
      # Stores the correct letters in the word
      correct_letters = []
      # Stores the incorrect guesses made by the player
      incorrect = []
      for char in word:
            if char.isalpha(): 
                  word_display.append("_")
                  correct_letters.append(char.upper())
            else:
                  word_display.append(char)

def select_difficulty(user_entry):
      levels = {'e': 'EASY', 'n': 'NORMAL', 'h': 'HARD', "g": "GODMODE", "l": "LEGEND"}
      levels_limits = {'e': 7, 'n': 6, 'h': 4, "g": 2, "l": 1}
      if user_entry == "e" or "n" or "h" or "g" or "l":
            print(f"\nYou selected: {levels[user_entry][0]}. \nYou will have {levels_limits[user_entry]} tries. Correct guesses do not count. \n")
      else: 
            print("invalid input")
      return user_entry, levels_limits

#Main Menu
def start_game(user_input):
    start = False
    end = False
    game_over = False
    guess = ""
    secret_word = ""
    out_of_guesses = False
    count = 0
    country_and_capital = random_word()
    menu = input("What do you want to do?: " ) 
    while (str.lower(menu) == "quit" or 1):
        if menu == "quit":
                end == True
                if end:
                    print("You have quit the game. ")
                break
        elif menu == "1" and not(out_of_guesses):
                #Logo
                f = open("art.txt", "r")
                print(f.read())
                f = f.close()   

                #User Input
                name = input("What's your name?: ")
                if name == "quit":
                    #TODO check, sth is wrong here ;-)
                    end = True
                    if end: 
                            print("You have quit the game. ")
                            break
                else:
                    print(f"I need to know your age, {name}. No kids allowed! ")
                    age = (input("How old are you?: "))
                    try:
                            if int(age) < 18:
                                print("You are too young. Go away!")
                                print(f"{name} has quit the game. ")
                                break
                            elif int(age) == False:
                                print("Wrong input")
                    except ValueError: 
                            if str(age) == "quit":
                                print(f"{name} quit the game." )
                                break
                    else:
                            difficulty_choice = f"Thanks {name}! \nPlease choose the difficulty level: \ne - Easy, \nn - Normal, \nh - Hard, \ng - Godmode, \nl - Legend"
                            print(difficulty_choice) 
                            difficulty = select_difficulty(str.lower(input("Please choose a difficulty level: ")))
                            guess_limit = difficulty[1]
                            #TODO read sth about python magic
                            capital = country_and_capital[INDEX_CAPITAL]
                            country = country_and_capital[INDEX_COUNTRY]
                            secret_word = str.lower(capital)            
                            tablica = list(secret_word) # tworzymy tablice
                                # tablica sluzy do wyswietlania _ _ _ _
                            for i in range(len(secret_word)):
                                tablica[i] = "_"
                            guess = ""
                            guess_count = guess_limit
                            print(f"Welcome to the gallows {name}! \nWe will hang your buddy unless you can tell us the capital of {country}\n ")
                    while guess_count > "0":
                            guess = str.lower(input("Enter guess: "))
                            # guess != secret_word and not(out_of_guesses): # Lists, dodaj kreski      
                            if guess == "quit":
                                        print(f"{name} has quit the game. ")
                                        break
                            if guess in secret_word:
                                print("\n Good guess! \n")
                                for i in range(len(secret_word)):
                                        if(secret_word[i] == guess):
                                            tablica[i] = guess
                                print("".join(tablica))
                                if "".join(map(str, tablica)) == secret_word:
                                        print(f"You win! \n The capital of {country} is {capital}")
                                        break
                            else:
                                print("\n Wrong!\n Keep trying... \n")
                                count = display_hangman_step(count)
                                print("".join(tablica))
                                guess_count -= 1
                                        
                            if guess_count == 0:
                                out_of_guesses = True
                            if out_of_guesses: 
                                game_over = True   
                                break
        if game_over == True:
                print("game over") 
                print(f"Sorry, {name}.\nYour buddy is dead.\nThe correct answer was {capital}.\nYou lose!")
                break
        elif guess == "quit":
                break
        elif not game_over == True:
                print("Good job, cowboy! You saved your pal. Now, get outta here!")
                break
        else:             
                print("That's not on the menu.")
                menu = input("What do you want to do?: " )

if __name__ == "__main__":
    start = "Enter '1' to start playing Hangman. \n"
    end = "Type 'quit' to exit the game anytime. \n"
    print("\n [------------- MAIN MENU -------------] \n" + "\n COMMANDS:  \n" + start + end + " \n [--------------------------------------] \n")
    start_game(input("Enter a value: " ))