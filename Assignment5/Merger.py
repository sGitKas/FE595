# Merge all of the various files from people posted on the discussion board into a single file with a Python script.

# Synopsis
# The Merger script will scan given a directory for files and merge them into a single file.

#Check the current directory

import fileinput
import glob
import os
cwd = os.getcwd()
print("Looking for files in - "+cwd)

file_list = glob.glob("data/*.*")

print("Found " + str(len(file_list)) + " Files")

with open('combined.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)