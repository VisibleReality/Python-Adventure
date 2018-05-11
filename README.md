# Python-Adventure

Really basic text based adventure game engine I made in python.

Probably has a bunch of bugs, and is a security risk, but I'm not planning for anyone to actually use this for anything serious.

## "Documentation" (if you could even call it that)

The data in pythonGame.py is a starting point. You should add data and your own functions in pythonGameData.py.
You can define your own functions and variables in pythonGameData.py

### Rooms

```python
Room(prompt, options, destinations, actions = None)
```
`prompt` should be a string. It is printed whenever the player enters the room.

`options` should be a list of strings. This will also be printed whenever the player enters a room. `options` can also be empty, which will make the game print the prompt, then move onto the destination.

`destinations` is a list of strings the same length as options. If options is empty, this must have 1 string in it which will be the automatically chosen destination. Destination strings should be names of other room variables.

`actions` is a list of strings the same length as destinations. If left out, it will default to be empty. The strings should be python code that will be executed upon choosing the corresponding destination.

You can also use the methods
```python
Room.addOption(option, destination, action = None)
```
and
```python
Room.removeOption(option)
```
which allow you to add and remove options.

`removeOption` takes the option's text as the value to remove.

### Ending the game

To end the game, just set `gameEnded` to `True`. This means that the game will end once the current room has finished. You can set custom game over text by writing `gameOverText = <your message>` in pythonGameData.py.

### File Hash Verification

By default, the game verifies the sha256 hash of the data file to improve security. You can disable this by setting `fileHashVerification` to `False`. This will create a warning when the game runs. You can generate a hash of `pythonGameData.py` by running `pythonGameHashTool.py` and adding the generated hash to `pythonGame.py`.