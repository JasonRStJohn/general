#This will be code to create a character generator for the D20 role playing system
#We'll start out by creating an empty dictionary labeled character to hold the many vars

character = {}
races = [human, elf, dwarf, gnome, halfling]
classes = [fighter, 
charName = raw_input("What is your Character's name?")
character["name"] = charName
charRace = raw_input("What race is your Character?")
def checkRace(input):
	for race in races:
		if 