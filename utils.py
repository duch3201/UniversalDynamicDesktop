import json
import os
from AppKit import NSScreen, NSWindow, NSWorkspace, NSURL

def set_wallpaper(image_path):
    workspace = NSWorkspace.sharedWorkspace()
    desktop_image_url = NSURL.fileURLWithPath_(image_path)
    screens = NSScreen.screens()
    for screen in screens:
        workspace.setDesktopImageURL_forScreen_options_error_(desktop_image_url, screen, None, None)



def discovery():
    
    path = os.getcwd()+"//Themes"

    directories = []
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)) and directory.endswith(".udd"):
            directories.append(directory)
    return directories

