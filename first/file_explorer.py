import os

# Directory to search
search_dir = os.getcwd()

# Search for files with a specific extension
extension = ".txt"
print(f"Searching for files with '{extension}' extension in '{search_dir}'...")
for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(extension):
            print(f"Found: {os.path.join(root, file)}")

# Search for files with a specific name
search_name = "example.txt"
flag = False
print(f"\nSearching for '{search_name}' in '{search_dir}'...")
for root, dirs, files in os.walk(search_dir):
    if search_name in files:
        flag = True
        print(f"Found: {os.path.join(root, search_name)}")

if not flag:
    print(f"File '{search_name}' not found in '{search_dir}'.")
