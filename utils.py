import json
import os
from AppKit import NSScreen, NSWindow, NSWorkspace, NSURL

def set_wallpaper(image_path):
    workspace = NSWorkspace.sharedWorkspace()
    desktop_image_url = NSURL.fileURLWithPath_(image_path)
    screens = NSScreen.screens()
    for screen in screens:
        workspace.setDesktopImageURL_forScreen_options_error_(desktop_image_url, screen, None, None)


def GetSelectedWallpaper():
    try:
        with open('./Themes/Themes.json') as Themes_file:
            data = json.load(Themes_file)
            selected = data["Selected"]
    except FileNotFoundError:
        return "Could not find Themes.json"
    return selected





def discovery():
    path = os.getcwd() + "/Themes"
    directories = []
    
    for filename in os.listdir(path):
        if filename.endswith(".udd"):
            directories.append(filename)
    
    with open('./Themes/Themes.json', 'r') as json_file:
        data = json.load(json_file)

    for directory in directories:
        theme_found = False
        for theme in data['Themes']:
            if theme['name'] == directory:
                theme_found = True
                break
        if not theme_found:
            new_theme = {"name": directory, "Location": "/Themes/" + directory}
            data['Themes'].append(new_theme)

    with open('./Themes/Themes.json', 'w') as json_file:
        json.dump(data, json_file)

    #return directories