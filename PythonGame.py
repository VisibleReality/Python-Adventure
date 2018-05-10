# Define the 'room' class which holds all room info
class Room:
	prompt = ""
	options = []
	destinations = []
	actions = []

	def __init__(self, prompt, options, destinations, actions = None):
		self.prompt = prompt
		self.options = options
		self.destinations = destinations
		if actions == None:
			self.actions = [None] * (len(destinations))
		else:
			self.actions = actions

	def addOption(self, option, destination, action = None):
		self.options = self.options + [option]
		self.destinations = self.destinations + [destination]
		self.actions = self.actions + [action]

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

roomDefinitions = open("pythonGameData.py", "r")

while True:
	line = roomDefinitions.readline()
	if line.strip() == "#EndFile":
		break
	else:
		exec(line.strip())

roomDefinitions.close()

# # Rooms. Format is (Prompt, Options, Destinations, Actions (actions is a snippet of python code that will be evaluated))
# # You could make this read from a file if you would prefer.
# start = Room("Starting story element", ["room1", "room2"], ["room1", "room2"])
# room1 = Room("Room1", ["room2", "room3"], ["room2", "room3"])
# room2 = Room("Room2", [], ["endGame"], ["gameEnded = True"])
# room3 = Room("Room3", [], ["room2"])

# Define the starting values for the game
currentRoom = start
gameEnded = False

# Gets user input and verifies that it is a valid option.
def getInput(currentRoom):
	while True:
		if currentRoom.options == []: # If the room has no options, just print the prompt and return None
			print(currentRoom.prompt)
			return None
		# This looks horrible but all it does is ask for input with the prompt in the format <prompt> (<options>) > _
		response = input(currentRoom.prompt + " (" + ", ".join(currentRoom.options) + ")> ")
		if CaseInsensitively(response.strip()) in currentRoom.options: # Then, we check if the response is a valid option, ignoring case.
			return response.strip().lower() # Return the response in all lowercase. This helps with comparisons later.
		else: print("Sorry, that was not a valid option. Try again.") # If that wasn't a valid response, print a message prompting the user to try again.

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
	print("Game Over.")

# Main game loop.
def game():
	global currentRoom
	while True:
		currentRoom = handleRoom(currentRoom) # Run the code for the current room and set the new room.
		if gameEnded == True: # If the game has ended, stop the game
			gameOver()
			break

# Run the game
game()
