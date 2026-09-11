def main():
	while True:
		guessed_letters = []
		letter = ""
		word = input("Please enter a word for the other player to guess:\n")
		if word == "QUIT":
			break
		no_of_guesses = int(input("Please enter the number of guesses:\n"))



		ask_user(letter, no_of_guesses, guessed_letters, word)
		while no_of_guesses != 0:

			if is_valid(letter, no_of_guesses, guessed_letters, word) == True:
				ask_user(letter, no_of_guesses, guessed_letters, word)
				if is_won(word, guessed_letters):
					print("CONGRATULATIONS! You Win!")
					break
			else:
				no_of_guesses -= 1
				ask_user(letter, no_of_guesses, guessed_letters, word)

			if no_of_guesses == 0:
				print("SORRY YOU ARE HANGED!")
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
			
def is_valid(letter, no_of_guesses, guessed_letters, word):
	letter = ask_user(letter, no_of_guesses, guessed_letters, word)
	for element in word:
		if letter == element:
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

def is_won(word, guessed_letters):
	won = True
	display = alphabet_update(word, guessed_letters)
	for items in display:
		if items == "-":
			won = False
	return won


def ask_user(letter, no_of_guesses, guessed_letters, word):
	letter = input(f"""Guess the word, {no_of_guesses} guess(es) left: {dash(guessed_letters, word)} 
Unused letters: {alphabet_update(word, guessed_letters)}\n""")
	guessed_letters.append(letter)
	return letter

main()


