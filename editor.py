'''
Python Adventure Game Editor
by VisibleReality

Todo: Documentation
'''

# Import required modules
import os

import math

# This code has been taken from https://stackoverflow.com/questions/1524126/how-to-print-a-list-more-nicely/
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
	print printer

def chooseFile():
	cwd = os.getcwd() # Get the current working directory
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
		while True:
			command = input(cwd + "> ")
			if command != "":
				break
		commandSplit = command.split(" ")
		if commandSplit[0] == "cd"
			commandArgument = " ".join(commandSplit[1:])
			if os.path.isdir

		fileList = os.listdir(cwd)
		newFileList = []
		for file in fileList: # Add file description to each file listing.
			fullPath = os.path.abspath(file)
			if os.path.isfile(fullPath):
				newFileList.append("f>" + file)
			elif os.path.isfile(fullPath):
				newFileList.append("d>" + file)
			else:
				newFileList.append("o>" + file)
		columnList(newFileList)
