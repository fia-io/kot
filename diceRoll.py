import math
import random
rolls = 3
faces = [1, 2, 3, "Claw", "Heart", "Bolt"]
yourDice = [0, 0, 0, 0, 0, 0]
toKeep = [-1]
while rolls != 0:
	position = 0
	while position < len(yourDice):
		if (position in toKeep):
			yourDice[position] = yourDice[position]
		else:
			yourDice[position] = faces[random.randint(0,5)];
		position = position + 1
	rolls = rolls - 1
	print(yourDice)
	keep = input("Keep any dice? Y/N")
	if (keep == 'Y'):
		toKeep.extend((input("Type dice to keep with commas [start at 0], like so: \"0, 4, 3\": ")).split(','))
		ind = 0
		while ind < len(toKeep):
			toKeep[ind] = int(toKeep[ind])
			ind = ind + 1
		print("You said: " + str(toKeep))
print("finished: ", yourDice)