import os.path
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))

# Setup variables for future computation.
filepath = current_directory + '\\Resources\\Tuning_Trouble_Input.txt'
counter = 0
character_lists = []
window = []

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

# Construct a list of characters from the lines in the file.
for line in lines:
    character_lists.append([])
    for character in line:
        character_lists[counter].append(character.strip())
    character_lists[counter].pop()
    counter += 1

# 4 is the smallest number we could possibly return.
counter = 4

# Go through our character lists and inspect a 4 character window.
for character_list in character_lists:
    # Setup the window, if the elements are unique then we are done.
    for i in range(0, 4):
        window.append(character_list[i])
    if len(set(window)) == len(window):
        print(f'Character\'s processed: {counter}')
        break
    # Slide the window over the rest of the list, looking for a unique set of 4 characters.
    for i in range(4, len(character_list)):
        window.pop(0)
        window.append(character_list[i])
        counter += 1
        if len(set(window)) == len(window):
            print(f'Character\'s processed: {counter}')
            break
    # Setup the variables for the next list, should one exist.
    window.clear()
    counter = 4

file.close()
