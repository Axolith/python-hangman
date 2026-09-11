def main():
	while True:
		guessed_letters = []
		letter = ""
		count = 0
		word = input("Please enter a word for the other player to guess:\n")
		no_of_guesses = int(input("Please enter the number of guesses:\n"))

		ask_user(letter, no_of_guesses, guessed_letters, word)

		if word == "QUIT":
			break
		
		else:
			while no_of_guesses >= count:
				if is_valid(word, letter):
					ask_user(letter, no_of_guesses, guessed_letters, word)
					if is_won:
						won_statement(letter, no_of_guesses, guessed_letters, word)
				else:
					count += 1
					ask_user(letter, no_of_guesses, guessed_letters, word)
					if no_of_guesses == count:
						lose_statement(letter, no_of_guesses, guessed_letters, word)


def dash(guessed_letters, word):
	result = ["-"] * len(word)
	display = ""
	for index, letter in enumerate(word):
		for item in guessed_letters:
			if letter == item:
				result[index] = letter
	for l in result:
		display += result
	return display
			
def is_valid(word, letter):
	for element in word:
		if letter == element:
			return True
		else:
			return False


def alphabet_update(word, guessed_letters):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	update = ""
	for letters in alphabet:
		found = False
		for elements in word:
			if letters == elements:
				found = True
		if not found:
			update += letters
	return update

def is_won(word, guessed_letters):
	display = alphabet_update(word, guessed_letters)
	for items in display:
			if items == "-":
				return False
			else:
				return True
def lose_statement(letter, no_of_guesses, guessed_letters,word):
	letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: dash(guessed_letters, word)
	Unused letters: alphabet_update(word, guessed_letters)
	SORRY YOU ARE HANGED!""")

def wom_statement(letter, no_of_guesses, guessed_letters,word):
	letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: dash(guessed_letters, word)
	Unused letters: alphabet_update(word, guessed_letters)
	CONGRATULATIONS! You Win!""")

def ask_user(letter, no_of_guesses, guessed_letters, word):
	guessed_letters.append(letter)
	letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: dash(guessed_letters, word)
	Unused letters: alphabet_update(word, guessed_letters)""")
	return letter

main()
