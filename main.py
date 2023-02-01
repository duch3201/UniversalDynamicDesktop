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
    location = LocationInfo(location_name)
    s = sun(location.observer, date=datetime.date.today())
    return s['sunrise'], s['sunset']


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

    timezone = pytz.timezone(pytz.country_timezones['in'][0])
    location_name = timezone._tzname
    sunrise, sunset = get_sunrise_sunset(location_name)

    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")

    sys.exit()

    os_name = platform.system()
    #print(os_name)

    if os_name == "Windows":
        #print("hetet")

        Windowswalp()
    elif os_name == "Linux":
        print("sorry, Linux is not supported yet!")


print(utils.discovery())
