'''
Python Adventure Game Editor
by VisibleReality

Todo: Documentation
'''

# Import required modules
import os
import sys
import math

# This code has been taken from https://stackoverflow.com/questions/1524126/how-to-print-a-list-more-nicely/
# I have no idea how it works.
def columnList(obj, cols=4, columnwise=True, gap=4):
	"""
	Print the given list in evenly-spaced columns.

	Parameters
	----------
	obj : list
		The list to be printed.
	cols : int
		The number of columns in which the list should be printed.
	columnwise : bool, default=True
		If True, the items in the list will be printed column-wise.
		If False the items in the list will be printed row-wise.
	gap : int
		The number of spaces that should separate the longest column
		item/s from the next column. This is the effective spacing
		between columns based on the maximum len() of the list items.
	"""
	sobj = [str(item) for item in obj]
	if cols > len(sobj): cols = len(sobj)
	max_len = max([len(item) for item in sobj])
	if columnwise: cols = int(math.ceil(float(len(sobj)) / float(cols)))
	plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
	if columnwise:
		if not len(plist[-1]) == cols:
			plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
		plist = zip(*plist)
	printer = '\n'.join([
		''.join([c.ljust(max_len + gap) for c in p])
		for p in plist])
	print(printer)

def cd(directory):
	'''Changes the current directory, checks if it is a directory first.'''
	if os.path.isdir(directory):
		os.chdir(directory)
	else:
		print(directory + " is not a directory")

def ls(cwd):
	fileList = os.listdir(cwd)
	newFileList = []
	for file in fileList: # Add file description to each file listing.
		fullPath = os.path.abspath(file)
		if len(file) >= 40:
			file = file[:37] + "..."
		if os.path.isfile(fullPath):
			newFileList.append("f>" + file)
		elif os.path.isdir(fullPath):
			newFileList.append("d>" + file)
		else:
			newFileList.append(" >" + file)
	columnList(newFileList)

def chooseFile():
	# Define the help message
	helpString = '''Opening Python-Adventure Game File.
Commands:
 - ls
   Lists the current directory.
 - cd <directory>
   Changes the current directory to <directory>.
   Can be relative or absolute path.
   .. refrences a directory 1 level up.
 - open <file>
   Opens <dile> for editing.
 - help
   Shows this message again.
 - exit
   Cancels choosing a file and goes back.
'''
	print(helpString)
	while True:
		cwd = os.getcwd() # Get the current working directory
		while True:
			command = input(cwd + "> ")
			if command != "":
				break
		# Check what the command is
		if command[:2] == "cd":
			cd(command[3:])
		elif command[:2] == "ls":
			ls(cwd)
		elif command[:4] == "open":
			if os.path.isfile(command[5:]):
				return command[5:]
			else:
				print(command[5:] + " is not a file.")
		elif command[:4] == "help":
			print(helpString)
		elif command[:4] == "exit":
			return None
		else:
			print(command + " is not a valid command. Type 'help' for help.")

def editor():
	

def main():
	while True:
		print("Welcome to Python Adventure Creator.")
		print("Please choose an option.")
		print("1. Edit an existing game.")
		print("2. Create a new game.")
		print("3. Exit.")
		choice = input("> ").strip().lower()
		if choice[0] == "1" or choice[:4] == "edit":
			fileName = chooseFile()
			editor(fileName)
		elif choice[0] == "2" or choice[:5] == "create" or choice[:3] == "new":
			editor(None)
		elif choice[0] == "3" or choice[:4] == "exit" or choice[:4] == "quit" or choice[0] == q:
			sys.exit()
		else:
			print("That is not a valid choice. Please try again.")
