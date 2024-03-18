import os

directory = os.getcwd()  # Get the current working directory

# List all files in the directory
files = os.listdir(directory)

# Iterate over each file
for filename in files:
    # Split the file name and extension
    name, ext = os.path.splitext(filename)
    # Rename the file by appending '_d' to the name
    new_name = name + '_d' + ext
    # Rename the file
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

print("All files in the current directory renamed successfully.")
