import os
import shutil

# file path you want to organize
Folder_Path = os.getcwd()

file_types = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac', '.flac'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": [ '.py','.js', '.html', '.css', '.java', '.c', '.cpp']
}

for folder_name, extensions in file_types.items():  
    folder_path = os.path.join(Folder_Path, folder_name) 
    if not os.path.exists(folder_path): 
        os.makedirs(folder_path)

    for file in os.listdir(Folder_Path):
        file_path = os.path.join(Folder_Path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(folder_path, file))
print("Files have been organized successfully!")
