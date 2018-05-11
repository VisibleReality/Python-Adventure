# Python game definition file.
# These lines will be executed before the game runs.

gameOverText = "Game Over.\nHi Tim, I'm finally finished with this 'game engine'. What do you think?"

import time

start = Room("You are at the front door of a castle. What do you do?", 
	["Try to enter the front door", "Knock Politely", "Run away"], 
	["castleFrontDoorLocked", "castleFrontDoorKnock", "castleRunAway"])
castleFrontDoorLocked = Room("You try to open the front door, but it seems that it is locked.\nA thundering noise is heard inside.", 
	[], 
	["start"])
castleFrontDoorKnock = Room("You almost knock on the front door, but you get a feeling that you shouldn't.", 
	["Try something else", "Overcome your fear and knock anyway"], 
	["start", "castleFrontDoorReallyKnock"])
castleRunAway = Room("You run away from the castle, into the woods.", 
	[], 
	["woods1"], 
	["time.sleep(3)"])
woods1 = Room("You are running, and you hear a growling noise behind you.", 
	["Keep running", "Freeze"],
	["woodsKeepRunning", "woodsFreeze"])
woodsKeepRunning = Room("You keep running, but the source of the growling noise seems to get closer and closer.",
	[],
	["woodsLouder"],
	["time.sleep(3)"])
woodsFreeze = Room("You freeze in your tracks but the growling sound gets louder and louder very slowly.",
	[],
	["woodsLouder"],
	["time.sleep(3)"])
woodsLouder = Room("The growling sound suddenly gets very loud, almost deafening.",
	[],
	["woodsKill"],
	["time.sleep(3)"])
woodsKill = Room("Suddenly your vision goes black and everything becomes silent...",
	[],
	["woodsKilled"],
	["time.sleep(3)"])
woodsKilled = Room("You were killed by a monster.",
	[],
	["gameOver"],
	["gameEnded = True"])
castleFrontDoorReallyKnock = Room("You knock on the front door. A thundering sound is heard inside, getting closer.",
	[],
	["castleFrontDoorKnockWait"],
	["time.sleep(3)"])
castleFrontDoorKnockWait = Room("The front door finally opens, and there is a giant monster.",
	["Run away", "Charge at the monster"],
	["castleRunAway", "castleKilled"])
castleKilled = Room("You charge at the monster.\nYou very quickly realise your mistake as you are killed by the monster.",
	[],
	["gameOver"],
	["gameEnded = True"])
