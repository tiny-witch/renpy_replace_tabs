# renpy_replace_tabs
A python script for .rpy files to replace tabs with spaces
USE INSTRUCTIONS:
1. place "renpy_replace_tabs.py" in your game directory. 
2. navigate to your game directory in the terminal. You can do this by copying the file path to your script (ie. user/game/path/) and typing in terminal:
cd "user/game/path/"

Check if you're in the right folder by typing ls , which will return a list of files in the folder, ie:
script.rpy
options.rpy 
etc.. 
3. run "renpy_replace_tabs.py" in your terminal with :

python renpy_replace_tabs.py

The terminal should print something like this: 
options.rpy has been corrected for tabs
script.rpy has been corrected for tabs
etc..
And that's it!
