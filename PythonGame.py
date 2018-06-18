#!/usr/bin/env python3

'''
Python text based adventure game engine.
By VisibleReality
Version 1.01
'''


# Define the hash of pythonGameData.py for security.
fileHashVerification = True # Set to false to disable hash verification. Only recommended for testing purposes.
fileHash = "5cc742e43f1fec88dca9e83faa0a8a639a59635bc60e2175cedb0502557a9d9c" # Place the sha256 hash of pythonGameData.py here.
import hashlib

import sys

# Define the 'room' class which holds all room info
class Room:
	'''
	The Room class defines a room in the game.
	A room has a prompt, which is text that will be printed to the user,
	some options, which is a list of options which will be printed to the user,
	some desinations, which is where the options will go,
	and, optionally, some actions, which will be custom code to be executed if a corresponding option is chosen.
	'''
	# Define the room attributes
	prompt = ""
	options = []
	destinations = []
	actions = []

	# Define the __init__ method which means you can easily set all required attributes
	def __init__(self, prompt, options, destinations, actions = None):
		self.prompt = prompt
		self.options = options
		self.destinations = destinations
		if actions == None:
			self.actions = [None] * (len(destinations))
		else:
			self.actions = actions
		assert len(self.options) == len(self.destinations) == len(self.actions)

	# Define a method which allows you to add an option to an existing room
	def addOption(self, option, destination, action = None):
		self.options = self.options + [option]
		self.destinations = self.destinations + [destination]
		self.actions = self.actions + [action]

	# Define a method which allows you to remove an option from an existing room.
	def removeOption(self, option):
		index = self.options.index(option)
		self.options.pop(index)
		self.destinations.pop(index)
		self.actions.pop(index)


# This isnt my code, it's copied from https://stackoverflow.com/questions/3627784/case-insensitive-in-python
# inb4 "programmers are interfaces between stackoverflow and a keyboard" joke
class CaseInsensitively(object):
	def __init__(self, s):
		self.__s = s.lower()
	def __hash__(self):
		return hash(self.__s)
	def __eq__(self, other):
		# ensure proper comparison between instances of this class
		try:
			other = other.__s
		except (TypeError, AttributeError):
			try:
				other = other.lower()
			except:
				pass
		return self.__s == other
# End of copied code

# Define the starting values for the game
gameOverText = "Game Over."
currentRoom = "start"
gameEnded = False

# Read the game data file and execute it
def readData():
	fileHashCheck = open("pythonGameData.py", "rb")
	actualFileHash = hashlib.sha256(fileHashCheck.read()).hexdigest()
	fileHashCheck.close()
	if fileHashVerification == False:
		print("Warning! FileHashVerification is off!")
		print("pythonGameData.py may have been modified.")
		print("FileHashVerification should be on unless testing.")
		answer = input("Are you sure you wish to run the game! (y/n) > ")
		if answer[0].lower() != "y":
			sys.exit()
	if (actualFileHash == fileHash) or (fileHashVerification == False):
		roomDefinitions = open("pythonGameData.py", "r")
		exec(roomDefinitions.read(), globals())
		roomDefinitions.close()
	else:
		print("Game data verificaton failed!")
		print("Game data file may have been tampered with!")
		print("Please check pythonGameData.py. If you trust it, set fileHashVerification to False.")
		input("Press enter to exit.")
		sys.exit()


# Gets user input and verifies that it is a valid option.
def getInput(currentRoom):
	while True:
		if currentRoom.options == []: # If the room has no options, just print the prompt and return None
			print(currentRoom.prompt)
			return None
		optionText = "" # Reset the optionText string
		for individualOption in currentRoom.options: # Create a nice numbered list for the options
			optionText = optionText + str(currentRoom.options.index(individualOption) + 1) + ". " + individualOption + ", "
		optionText = optionText[:-2] # Trim off the last two characters
		response = input(currentRoom.prompt + "\n(" + optionText + ")\n> ") # Ask for user input
		if response.isdigit(): # If they've picked a number, use the option that had that number
			response = int(response)
			if response <= len(currentRoom.options):
				return currentRoom.options[response - 1].lower()
		elif CaseInsensitively(response.strip()) in currentRoom.options: # Then, we check if the response is a valid option, ignoring case.
			return response.strip().lower() # Return the response in all lowercase. This helps with comparisons later.
		print("Sorry, that was not a valid option. Try again.") # If that wasn't a valid response, print a message prompting the user to try again.

# Handles setting the proper value for the current room
def handleDestination(currentRoom, index):
	if currentRoom.destinations[index] in list(globals().keys()): # If the string is the name of a variable, return a refrence to that variable
		if currentRoom.actions[index] != None: # If that destination has an action associated, run that action.
			exec(currentRoom.actions[index], globals())
		return eval(currentRoom.destinations[index])
	else: # Do the same, except return a string.
		if currentRoom.actions[index] != None:
			exec(currentRoom.actions[index], globals())
		return currentRoom.destinations[index]

# Groups the other two functions together/
def handleRoom(currentRoom):
	response = getInput(currentRoom)
	if response == None: # If response is None, then choose a default action.
		return handleDestination(currentRoom, 0)
	optionsLower = [option.lower() for option in currentRoom.options] # Create a lowercase version of the list of options for comparing with the response.
	if response in optionsLower: # choose the destination that corresponds to the action.
		responseIndex = optionsLower.index(response)
		return handleDestination(currentRoom, responseIndex)

# gameOver will run when the game ends.
def gameOver():
	print(gameOverText)

# Main game loop.
def game():
	global currentRoom
	while True:
		currentRoom = handleRoom(currentRoom) # Run the code for the current room and set the new room.
		if gameEnded: # If the game has ended, stop the game
			gameOver()
			break

# Read game data
readData()
currentRoom = eval(currentRoom)

# Run the game
game()
input("Press enter to exit.")
