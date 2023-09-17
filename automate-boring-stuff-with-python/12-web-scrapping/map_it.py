#! python3
"""map-it.py - Launches a map in the browser using an address from the command line or clipboard."""
import webbrowser
import sys # sys.argv - The list of command line arguments passed to a Python script.
import pyperclip # https://pypi.org/project/paperclip/

#The sys.argv variable stores a list of the program s filename and command line arguments.
# If this list has more than just the filename in it, then len(sys.argv) evaluates to
# an integer greater than 1, meaning that command line arguments have indeed been provided.
if len(sys.argv) > 1:
    # Get address from command line. argv[0] is the script name (full path).
    ADDRESS = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    ADDRESS = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + ADDRESS)

print(ADDRESS)