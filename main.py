import datetime
from datetime import datetime
import json
import os
import platform
import sys
import time
import utils

import pytz
from astral.location import LocationInfo
from astral.sun import sun


def get_sunrise_sunset(location_name):
    import datetime
    location = LocationInfo(location_name)
    s = sun(location.observer, date=datetime.datetime.now().date())
    sunrise = s['sunrise']
    sunset = s['sunset']
    return sunrise, sunset


def string_to_time(time_string, sunrise_time, sunset_time):
    import datetime
    if time_string == "sunRise":
        return sunrise_time
    elif time_string == "noon":
        return datetime.time(12,0,0)
    elif time_string == "sunSet":
        return sunset_time
    elif time_string == "startSunSet":
        return sunset_time - datetime.timedelta(hours=1)
    elif time_string == "night":
        return datetime.datetime.now().time()
    else:
        raise ValueError(f"Invalid time string: {time_string}")


def Darwin():
    import datetime
    from AppKit import NSWorkspace, NSScreen
    from Foundation import NSURL

    SelectedWalp = utils.GetSelectedWallpaper()
    path = os.getcwd() + "/Themes/" + SelectedWalp
    with open(path+"/Wallpaper.json") as f:
        jsonTheme = json.load(f)

    path_to_image = path + jsonTheme["Night"][0]
    print(path_to_image)
    workspace = NSWorkspace.sharedWorkspace()

    workspace.setDesktopImageURL_forScreen_options_error_(path_to_image, None, {}, None)



def Windowswalp():
    import ctypes
    os.chdir("MCwalp.pdd")
    with open("Walpaper.json", "r") as f:
        themejson = json.load(f)

    num_images_day = len(themejson["Day"])
    num_images_night = len(themejson["Night"])
    first_image_day = themejson["Day"][0]
    first_image_night = themejson["Night"][0]

    print(first_image_day)
    #sys.exit()

    #if not os.path.exists("images/"+first_image_day):
     #   print("Error: The path to the image file does not exist.")
    #sys.exit()


    SPI_SETDESKWALLPAPER = 20 
    os.chdir("images")
    #print(os.getcwd()+first_image_day)
    path_to_image = os.getcwd()+"\\" + first_image_day
    if not os.path.exists(path_to_image):
        print("Error: The file does not exist.")
    #sys.exit()

    ctypes.windll.user32.SystemParametersInfoW(20, 0, path_to_image , 0)


def main():

    os_name = platform.system()

    if os_name == "Windows":
        Windowswalp()
    elif os_name == "Linux":
        print("sorry, Linux is not supported yet!")
    elif os_name == "Darwin":
        Darwin()


main()
