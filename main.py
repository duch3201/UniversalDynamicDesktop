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
    s = sun(location.observer, date=datetime.date.today())
    sunrise = s['sunrise'].time()
    sunset = s['sunset'].time()
    return sunrise, sunset


def get_milestone_time(milestone, sunrise, sunset):
    if milestone == "sunRise":
        return sunrise
    elif milestone == "noon":
        return datetime.time(12, 0, 0)
    elif milestone == "sunSet":
        return sunset
    elif milestone == "night":
        return datetime.time(23, 59, 59)
    else:
        raise ValueError("Invalid milestone")



def Darwin():
    import datetime
    import AppKit 
    from AppKit import NSWorkspace, NSURL, NSScreen

    os.chdir("Themes/MCwalp.pdd")
    with open("Walpaper.json", "r") as f:
        themejson = json.load(f)
    
    sunrise, sunset = get_sunrise_sunset("your_location")
    current_time = datetime.datetime.now().time()
    if current_time > sunrise and current_time < sunset:
        # Daytime
        path = os.getcwd()+"/images/"+themejson["Day"][0]
        workspace = NSWorkspace.sharedWorkspace()
        image_url = NSURL.fileURLWithPath_(path)
        options = {}
        screen = NSScreen.mainScreen()
        workspace.setDesktopImageURL_forScreen_options_error_(image_url, screen, options, None)
    else:
        # Nighttime
        path = os.getcwd()+"/images/"+themejson["Night"][0]
        workspace = NSWorkspace.sharedWorkspace()
        image_url = NSURL.fileURLWithPath_(path)
        options = {}
        screen = NSScreen.mainScreen()
        workspace.setDesktopImageURL_forScreen_options_error_(image_url, screen, options, None)





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

    #timezone = pytz.timezone(pytz.country_timezones['in'][0])
    #location_name = timezone._tzname
    #sunrise, sunset = get_sunrise_sunset(location_name)

    #print(f"Sunrise: {sunrise}")
    #print(f"Sunset: {sunset}")

    

    os_name = platform.system()
    print(os_name)

    #sys.exit()

    if os_name == "Windows":
        #print("hetet")

        Windowswalp()
    elif os_name == "Linux":
        print("sorry, Linux is not supported yet!")
    elif os_name == "Darwin":
        Darwin()


main()
