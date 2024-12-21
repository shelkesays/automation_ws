import os
import shutil


# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List all files and folders in the directory
items = os.listdir(cwd)
print("Contents of Directory:", items)

# Create a new folder
new_folder = os.path.join(cwd, "TestFolder")
os.makedirs(new_folder, exist_ok=True)
print(f"Folder '{new_folder}' created.")

# Copy a file (example.txt) to the new folder
source_file = os.path.join(cwd, "example.txt")  # Replace with an actual file
destination_file = os.path.join(new_folder, "example_copy.txt")
shutil.copy(source_file, destination_file)
print(f"Copied '{source_file}' to '{destination_file}'.")

shutil.move(destination_file, os.path.join(cwd, "example_copy.txt"))

print("Python Executable Path:", shutil.which("python"))
# print(shutil.which("python"))

