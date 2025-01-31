import os
import shutil

# Define folders for each file type
FOLDERS = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".tar", ".rar"]
}

# Function to organize files
def organize_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Move files based on their extensions
        for folder, extensions in FOLDERS.items():
            if any(file.endswith(ext) for ext in extensions):
                folder_path = os.path.join(directory, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} to {folder}")

# Run the function on the current directory
if __name__ == "__main__":
    organize_files(os.getcwd())
