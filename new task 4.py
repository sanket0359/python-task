import os
import shutil

# Define the source directory (e.g., Downloads folder)
source_dir = os.path.expanduser("~/Downloads")

# Define the destination directories for different file types
dest_dirs = {
    "Documents": ["pdf", "doc", "docx", "txt"],
    "Images": ["jpg", "jpeg", "png", "gif", "bmp"],
    "Videos": ["mp4", "avi", "mov", "mkv"],
    "Music": ["mp3", "wav", "aac"],
    "Archives": ["zip", "tar", "gz", "rar"]
}

def organize_files():
    for filename in os.listdir(source_dir):
        # Get the file extension
        ext = filename.split('.')[-1].lower()
        
        # Find the right folder for the file based on its extension
        for folder, extensions in dest_dirs.items():
            if ext in extensions:
                # Create the folder if it doesn't exist
                folder_path = os.path.join(source_dir, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Move the file to the destination folder
                shutil.move(os.path.join(source_dir, filename), folder_path)
                print(f"Moved {filename} to {folder_path}")
                break

if __name__ == "__main__":
    organize_files()
