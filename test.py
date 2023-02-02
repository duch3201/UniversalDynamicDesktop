import utils
import platform
import os
import json
import sys
from pathlib import Path

def Darwin():
    import datetime
    from AppKit import NSWorkspace, NSScreen
    from Foundation import NSURL
    import objc

    SelectedWalp = utils.GetSelectedWallpaper()
    path = os.getcwd() + "/Themes/" + SelectedWalp
    with open(path+"/Wallpaper.json") as f:
        jsonTheme = json.load(f)

    time = datetime.datetime.now().hour
    if time >= 18 or time <= 6:
        img = jsonTheme["Night"][0]["file"]
    else:
        img = jsonTheme["Day"][0]["file"]

    path_to_image = path + "/images/" + str(img)
    path = path_to_image
    workspace = NSWorkspace.sharedWorkspace()
    screens = NSScreen.screens()
    for screen in screens:
        workspace.setDesktopImageURL_forScreen_options_error_(NSURL.fileURLWithPath_(path), screen, None, None)




def main():

    os_name = platform.system()

    if os_name == "Windows":
        #Windowswalp()
        print("lol")
    elif os_name == "Linux":
        print("sorry, Linux is not supported yet!")
    elif os_name == "Darwin":
        Darwin()


main()