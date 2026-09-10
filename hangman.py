def hangman():
	while True:
		guessed_letters = []
		letter = ""
		i = 0
		word = input("Please enter a word for the other player to guess:\n")
		no_of_guesses = int(input("Number of guesses:\n"))

		ask_user(letter, no_of_guesses, guessed_letters, word)

		if word == "QUIT":
			break
		
		else:
			while no_of_guesses != 0:
				if is_valid(word, letter):
					ask_user(letter, no_of_guesses, guessed_letters, word)
					if is_won:
						won_statement(letter, no_of_guesses, guessed_letters, word)
				else:
					i += 1
					ask_user(letter, no_of_guesses, guessed_letters, word)
					if no_of_guesses == i:
						lose_statement(letter, no_of_guesses, guessed_letters, word)

def dash(guessed_letters, word):
	display = ""
	dashes = ["-"] * len(word)
	for index, letter in enumerate(word):
		for items in guessed_letters:
			if letter == items:




def alphabet_update(word, guessed_letters):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	update = ""


def ask_user(letter, no_of_guesses, guessed_letters, word):
	guessed_letters.append(letter)
	letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: dash(guessed_letters, word)
	Unused letters: alphabet_update(word, guessed_letters)""")

hangman()
