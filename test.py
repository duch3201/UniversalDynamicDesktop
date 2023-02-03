import utils
import platform
import os
import json
import sys
from pathlib import Path

import datetime

def get_milestones():
    from astral.sun import sun
    from astral.location import LocationInfo
    from datetime import datetime, time

    city = LocationInfo("Bydgoszcz", "Poland")
    s = sun(city.observer, date=datetime.now())
    dawn = s['dawn']
    sunrise = s['sunrise']
    sunset = s['sunset']
    dusk = s['dusk']

    return dawn, sunrise, sunset, dusk

def get_current_time():
    now = datetime.datetime.now().time()
    return now

def astraltest():
    dawn, sunrise, sunset, dusk = get_milestones()
    current_time = get_current_time()

    if dawn.time() <= current_time < sunrise.time():
        print("dawn")
    elif sunrise.time() <= current_time < sunset.time():
        print("day")
    elif sunset.time() <= current_time < dusk.time():
        print("sunset")
    else:
        print("night")





def dastraltest():
    from astral.sun import sun
    from astral.location import LocationInfo
    from datetime import datetime, time

    city = LocationInfo("Bydgoszcz", "Poland")
    s = sun(city.observer, date=datetime.now())

    dawn = time(s['dawn'].hour, s['dawn'].minute).strftime('%H:%M')
    sunrise = time(s['sunrise'].hour, s['sunrise'].minute).strftime('%H:%M')
    noon = time(s['noon'].hour, s['noon'].minute).strftime('%H:%M')
    sunset = time(s['sunset'].hour, s['sunset'].minute).strftime('%H:%M')
    dusk = time(s['dusk'].hour, s['dusk'].minute).strftime('%H:%M')

    print(dawn, sunrise, noon, sunset, dusk)

def Darwin():
    import datetime
    from AppKit import NSWorkspace, NSScreen
    from Foundation import NSURL
    import objc
    import datetime
    from astral.sun import sun
    from astral.location import LocationInfo
    from datetime import datetime, time

    city = LocationInfo("warsaw", "Poland")
    s = sun(city.observer, date=datetime.now())

    dawn = time(s['dawn'].hour, s['dawn'].minute).strftime('%H:%M')
    sunrise = time(s['sunrise'].hour, s['sunrise'].minute).strftime('%H:%M')
    noon = time(s['noon'].hour, s['noon'].minute).strftime('%H:%M')
    sunset = time(s['sunset'].hour, s['sunset'].minute).strftime('%H:%M')
    dusk = time(s['dusk'].hour, s['dusk'].minute).strftime('%H:%M')
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print(current_time)

    

    SelectedWalp = utils.GetSelectedWallpaper()
    path = os.getcwd() + "/Themes/" + SelectedWalp
    with open(path + "/Wallpaper.json") as f:
        jsonTheme = json.load(f)

    dawn, sunrise, sunset, dusk = get_milestones()
    current_time = get_current_time()

    if dawn.time() <= current_time < sunrise.time():
        print("dawn")
        img = jsonTheme["Day"][0]["file"]
    elif sunrise.time() <= current_time < sunset.time():
        print("day")
        img = jsonTheme["Day"][1]["file"]
    elif sunset.time() <= current_time < dusk.time():
        img = jsonTheme["Night"][0]["file"]
        print("sunset")
    else:
        img = jsonTheme["Night"][1]["file"]
        print("night")
        
    path_to_image = path + "/images/" + str(img)
    path = NSURL.fileURLWithPath_(path_to_image)
    workspace = NSWorkspace.sharedWorkspace()
    screen = NSScreen.screens()
    workspace.setDesktopImageURL_forScreen_options_error_(path, screen[0], {}, None)

    print("\n\n dawn", dawn, "\n\n noon", noon, "\n\n sunset", sunset, "\n\n dusk", dusk, "\n\n current time", current_time, "\n\n img", img, "\n\n path", path_to_image )



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