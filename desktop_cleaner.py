import os
import shutil
from pathlib import Path

desktop_dir = Path.home() / "Desktop"

#Create a dictionary to map file extensions to the various folder names
FILE_TYPE_MAP = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents" : [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx"],
    "Music" : [".mp3", ".wav", ".aac"],
    "Videos" : [".mp4", ".mov", ".avi", ".mkv"],
    "Archives" : [".zip", ".rar", ".tar", ".gz"],
    "Code" : [".py", ".html", ".js", ".css", ".cpp", ".java"],
}

#This function to create folders for the various file types if they don't exist
def create_folders (): 
    for folder in FILE_TYPE_MAP: 
        folder_path = desktop_dir / folder
        if not folder_path.exists():
            folder_path.mkdir()

#This function to move files to respective folder based on their extension
def move_files():
    for item in desktop_dir.iterdir():
        if item.is_file(): #This checks if it's a file
            file_extension = item.suffix.lower() #Get file extention

            #This is to find the correct folder for this file type
            for folder, extensions in FILE_TYPE_MAP.items():
                if file_extension in extensions:
                    dest_folder = desktop_dir / folder
                    shutil.move(str(item), dest_folder / item.name)
                    print(f"Moved {item.name} to {folder}")
                    break

#This function is to organize the desktop 
def organize_desktop():
    create_folders() 
    move_files() 

if __name__ == "__main__":
    organize_desktop()

