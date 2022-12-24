import os.path
import sys

def signal_processor(ch_list, window_size):
    window = []
    count = window_size
    # Setup the window, if the elements are unique then we are done.
    for i in range(0, window_size):
        window.append(ch_list[i])
    if len(set(window)) == len(window):
        print(f'Character\'s processed: {count}')
        return
    # Slide the window over the rest of the list, looking for a unique set of characters.
    for i in range(window_size, len(ch_list)):
        window.pop(0)
        window.append(ch_list[i])
        count += 1
        if len(set(window)) == len(window):
            print(f'Character\'s processed: {count}')
            break
    # Setup the variables for the next list, should one exist.
    window.clear()
    count = window_size


current_directory = os.path.dirname(os.path.realpath(__file__))

# Setup variables for future computation.
filepath = current_directory + '\\Resources\\Tuning_Trouble_Input.txt'
counter = 0
character_lists = []
###window = []

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

# Go through our character lists and inspect a designated character window.
# PART 1
for character_list in character_lists:
    signal_processor(character_list, 4)
# PART 2
for character_list in character_lists:
    signal_processor(character_list, 14)

file.close()
