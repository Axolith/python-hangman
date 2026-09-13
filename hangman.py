import random
def main():
    while True:
        guessed_letters = []
        letter = ""
        option = input("""How would you like to choose the word?
1. Pick a word from the word list 
2. Enter my own word 
        Choice: """)
        if option == "2":
            word = input("Please enter a word for the other player to guess:\n")
        if option == "1":
            words = [
            "APPLE",
            "PYTHON",
            "ELEPHANT",
            "COMPUTER",
            "VOLCANO",
            "JAZZ",
            "QUIZ",
            "XYLOPHONE",
            "BASKETBALL",
            "OXYGEN",
            "CANDLE",
            "MIRROR",
            "CASTLE",
            "SHADOW",
            "COFFEE",
            "DRAGON",
            "GALAXY",
            "WHISPER",
            "PUZZLE",
            "LIGHTNING"
            ]
            word = random.choice(words)

        if word == "QUIT":
            break

        initial_guess = int(input("Please enter the number of guesses (4 - 10):\n"))
        no_of_guesses = initial_guess

        while no_of_guesses != 0:
            print(stick_figure(no_of_guesses, initial_guess))
            letter = ask_user(letter, no_of_guesses, guessed_letters, word)
            if is_won(word, guessed_letters):
                won_statement(letter, no_of_guesses, guessed_letters, word, initial_guess)
                break
            if not is_valid(letter, word):
                if not duplicate(letter, no_of_guesses, guessed_letters, word):
            if no_of_guesses == 0:
                lost_statement(letter, no_of_guesses, guessed_letters, word, initial_guess)
                break

def dash(guessed_letters, word):
    result = ["-"] * len(word)
    display = ""
    for index, letter in enumerate(word):
        for item in guessed_letters:
            if letter == item:
                result[index] = letter
    for l in result:
        display += l
    return display
            
def is_valid(letter, word):
    for element in word:
        if element == letter:
            return True
    return False

def duplicate(letter, no_of_guesses, guessed_letters, word):
    for element in guessed_letters:
        if element != letter:
            no_of_guesses -= 1
            return False
    return True

def is_won(word, guessed_letters):
    display = dash(guessed_letters, word)
    for items in display:
        if items == "-":
            return False
    return True
        
def alphabet_update(word, guessed_letters):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    update = ""
    for letters in alphabet:
        found = False
        for elements in guessed_letters:
            if letters == elements:
                found = True
        if not found:
            update += letters
    return update

def won_statement(letter, no_of_guesses, guessed_letters, word, initial_guess):
    print(f"""{stick_figure(no_of_guesses, initial_guess)}\nGuess the word, {no_of_guesses} guess(es) left: {dash(guessed_letters, word)} 
Unused letters: {alphabet_update(word, guessed_letters)} CONGRATULATIONS! You Win!""")


def lost_statement(letter, no_of_guesses, guessed_letters, word, initial_guess):
    print(f"""{stick_figure(no_of_guesses, initial_guess)}\nGuess the word, {no_of_guesses} guess(es) left: {dash(guessed_letters, word)} 
Unused letters: {alphabet_update(word, guessed_letters)} SORRY YOU ARE HANGED!""")



def ask_user(letter, no_of_guesses, guessed_letters, word):
    letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: {dash(guessed_letters, word)} 
Unused letters: {alphabet_update(word, guessed_letters)}\n""")
    guessed_letters.append(letter)
    return letter

def stick_figure(no_of_guesses, initial_guess):
    incorrect_guesses = initial_guess - no_of_guesses
    figure = ""
    if incorrect_guesses == 0:
        figure = """
      _______
     |/      
     |      
     |      
     |      
     |      
     |
    _|___
    """
    elif incorrect_guesses == 1:
        figure = """
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
    """
    elif incorrect_guesses == 2:
        figure = """
      _______
     |/      |
     |      (_)
     |       
     |      
     |      
     |
    _|___
    """
    elif incorrect_guesses == 3:
        figure = """
      _______
     |/      |
     |      (_)
     |       |
     |      
     |      
     |
    _|___
    """

    elif incorrect_guesses == 4:
        figure = """
      _______
     |/      |
     |      (_)
     |      /|
     |       
     |      
     |
    _|___
    """
    elif incorrect_guesses == 5:
        figure = """
      _______
     |/      |
     |      (_)
     |      /|\\
     |       
     |      
     |
    _|___
    """

    elif incorrect_guesses == 6:
        figure = """
      _______
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      
     |
    _|___
    """
    elif incorrect_guesses == 7:
        figure = """
      _______
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      /
     |
    _|___
    """
    elif incorrect_guesses == 8:
        figure = """
      _______
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / \\
     |
    _|___
    """
    elif incorrect_guesses == 9:
        figure = """
      _______
     |/      |
     |      (_)
     |      \\|/
     |       |
     |      / \\
     |
    _|___
    """
    if no_of_guesses == 0:
        figure = """
      _______
     |/      |
     |       ☠️
     |      \\|/
     |       |
     |      / \\ 
     |
    _|___
    """
    return figure

main()


