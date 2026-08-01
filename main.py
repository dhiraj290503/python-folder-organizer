import os
import shutil   

#folder path you want to organize
FOLDER_PATH = os.getcwd()  # Current working directory

#file type mapping constants
FILE_TYPE={
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.html', '.css', '.php'],
    'Others': []  # For files that don't match any of the above types
}

#create folders for each file type if they don't exist
for folder in FILE_TYPE.keys():     #create folders for each file type if they don't exist
    folder_path = os.path.join(FOLDER_PATH, folder) #create folder path
    if not os.path.exists(folder_path): #check if folder exists
        os.makedirs(folder_path)    #create folder if it doesn't exist


#organise files
for file in os.listdir(FOLDER_PATH):  #list all files in the folder
    file_path = os.path.join(FOLDER_PATH, file)  #get full file path

    #skip folders
    if os.path.isdir(file_path):
        continue

    #get file extension
    file_extension = os.path.splitext(file)[1].lower()  #get file extension and convert to lowercase

    for folder, extensions in FILE_TYPE.items():  #iterate through file types
        if file_extension in extensions:  #check if file extension matches any of the types
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))  #move file to corresponding folder
            break 

print("Files have been organized successfully✅")