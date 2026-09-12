import random
def main():
	while True:
		guessed_letters = []
		letter = ""
		word = input("Please enter a word for the other player to guess:\n")
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
				no_of_guesses -= 1
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
			
def is_valid(letter,word):
	for element in word:
		if element == letter:
			return True
	return False


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
	difference = 10 // (initial_guess - 1)
	for stage in range(0, 10, difference):
		if stage == 0:
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
		elif stage == 1:
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
		elif stage == 2:
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
		elif stage == 3:
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

		elif stage == 4:
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
		elif stage == 5:
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

		elif stage == 6:
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
		elif stage == 7:
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
		elif stage == 8:
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
		elif stage == 9:
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
		elif stage >= 10:
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


