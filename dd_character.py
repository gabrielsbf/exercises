from random import randint
from math import floor

class Character:
	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()
		self.hitpoints = 10 + modifier(self.constitution)

	def	ability(self):
		results = [randint(1, 6) for i in range(0,4)]
		results.remove(min(results))
		return sum(results)

def modifier(char_const):
	return floor((char_const - 10)/2)

score = Character().ability()
print(score >= 3 and score <= 18)
