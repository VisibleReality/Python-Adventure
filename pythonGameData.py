# Python game definition file.
# These lines will be executed before the game runs.

start = Room("Starting story element", ["room1", "room2"], ["room1", "room2"])
room1 = Room("Room1", ["room2", "room3"], ["room2", "room3"])
room2 = Room("Room2", [], ["endGame"], ["gameEnded = True"])
room3 = Room("Room3", [], ["room2"])

#EndFile
# The program will stop reading at that line.
# If you don't include that, the program will hang.