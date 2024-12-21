import os
from pathlib import Path
import shutil

def organize_folder(target_dir):
    # File categories and their extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx", ".pptx", ".md", ".html", ".xls"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Archives": [".zip", ".tar", ".gz"],
    }
    
    # Ensure target folder exists
    if not os.path.exists(target_dir):
        print(f"Directory '{target_dir}' does not exist.")
        return

    # Organize files
    for file in os.listdir(target_dir):
        file_path = os.path.join(target_dir, file)
        if os.path.isfile(file_path):
            # Find the category of the file
            for category, extensions in file_categories.items():
                if file.endswith(tuple(extensions)):
                    category_folder = os.path.join(target_dir, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    print(f"Moved '{file}' to '{category_folder}'.")
                    break
    print("Folder organization completed.")

# Example usage
path = Path("/").joinpath("Users", "rahulshelke", "Downloads")
organize_folder(path)
