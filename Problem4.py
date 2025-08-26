import os

# Specify the directory path
directory_path = "."  # "." means current directory. Change it to any path you like

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of the directory '{directory_path}':")
for item in contents:
    print(item)
