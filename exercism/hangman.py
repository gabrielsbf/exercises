# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		self.word = word
		self.masked_word = '_' * len(self.word)

	def guess(self, char):
		self.get_status()
		if self.status == STATUS_ONGOING :
			if char in self.word and not char in self.masked_word:
				arr_masked_word = list(self.masked_word)
				repeats = []
				i = 0
				for c in self.word:
					if c == char:
						repeats.append(i)
					i += 1
				for index in repeats:
					arr_masked_word[index] = char
				final_word = ''.join(arr_masked_word)
				self.masked_word = final_word
				return True
			else:
				self.remaining_guesses-=1
				return False
		else :
			raise ValueError("The game has already ended.")

	def get_masked_word(self):
		return self.masked_word

	def get_status(self):
		if self.masked_word.find("_") == -1:
			self.status = STATUS_WIN
		elif self.remaining_guesses < 0:
			self.status = STATUS_LOSE
		else:
			self.status = STATUS_ONGOING
		return self.status

