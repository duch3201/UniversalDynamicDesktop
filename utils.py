import json
import os


def discovery():
    
    path = os.getcwd()+"//Themes"

    directories = []
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)) and directory.endswith(".udd"):
            directories.append(directory)
    return directories

