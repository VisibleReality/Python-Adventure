# PythonGame hash tool.
# It is recommended to hash your game data file, and store that hash in pythonGame.py to improve security.

# Import the hashlib module
import hashlib

# Define some variables
fileLocation = "pythonGameData.py"

file = open(fileLocation, "rb")
fileHash = hashlib.sha256(file.read()).hexdigest()

print("This is the sha256 hash of pythonGameData.py.")
print("Please place this at the start of pythonGame.py, where it says fileHash =")
print(fileHash)
input("Press enter to exit.")