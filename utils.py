import json
import os
from AppKit import NSScreen, NSWindow, NSWorkspace, NSURL
import datetime
from PIL import Image, ImageDraw, ImageFont

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

def CheckTime(time):
    pass

def FirstRun():
    os.mkdir("Themes")

def init():
    pass


def add_text(position, img):

     SelectedWalp = GetSelectedWallpaper()
     path = os.getcwd() + "/Themes/" + SelectedWalp 
     with open(path + "/Wallpaper.json") as f:
         jsonTheme = json.load(f)

     img = Image.open(path + "/images/" + jsonTheme["Night"][0]["file"])
     d1 = ImageDraw.Draw(img)
     myFont = ImageFont.truetype('./Fonts/Raleway-Medium.ttf', 40)
     myFontt = ImageFont.truetype('./Fonts/Raleway-Medium.ttf', 25)

     # Get the font size
     font_size = 40

     # Get the width and height of the image
     width, height = img.size

     img_title = jsonTheme["Night"][0]["file"].split(".")
     img_desc = jsonTheme["Night"][0]["desc"]


     if position == 'bottom_left':
         x = 50
         y = height - font_size - 80

         xx = 50
         yy = height - font_size - 30

         d1.text((x, y), img_title[0], font=myFont, fill=(71, 71, 71))
         d1.text((xx, yy), img_desc, font=myFontt, fill=(71, 71, 71))
         img.show()
         return img
         img.save("image_text.png")
     elif position == 'bottom_right':
         x = width - font_size * len(img_title[0]) - 50
         y = height - font_size - 80

         xx = width - font_size * len(img_desc) + 645
         yy = height - font_size - 30

         d1.text((x, y), img_title[0], font=myFont, fill=(71, 71, 71))
         d1.text((xx, yy), img_desc, font=myFontt, fill=(71, 71, 71))
         img.show()
         img.save("image_text.png")
     elif position == 'top_left':
         x = 50
         y = 50

         xx = 50
         yy = 100

         d1.text((x, y), img_title[0], font=myFont, fill=(71, 71, 71))
         d1.text((xx, yy), img_desc, font=myFontt, fill=(71, 71, 71))
         img.show()
         img.save("image_text.png")
     elif position == 'top_right':
         x = width - font_size * len(img_title[0]) - 50
         y = 50

         xx = width - font_size * len(img_desc) + 645
         d1.text((x, y), img_title[0], font=myFont, fill=(71, 71, 71))
         yy = 100
         d1.text((xx, yy), img_desc, font=myFontt, fill=(71, 71, 71))
         img.show()
         img.save("image_text.png")


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

def get_settings(setting):
     with open("settings.json", "r") as f:
         settings = json.load(f)

         Wallpaper_interval = settings["wallpaperRefreshInterval"]
         Wallpaper_info = settings["showWallpaperInfo"]
         Info_position = settings["showWallpaperInfo"]
         City = settings["city"]
         Country = settings["country"]

         if setting == "null":

             return  Wallpaper_info, Wallpaper_interval, Info_position, City, Country
         elif setting == "Wallpaper_info":
             return Wallpaper_info
         elif setting == "Wallpaper_interval":
             return Wallpaper_interval
         elif setting == "Info_position":
             return Info_position
         elif setting == "City":
             return City
         elif setting == "Country":
             return Country
         else:
             return "Invalid setting"

def get_current_time():
    now = datetime.datetime.now().time()
    return now

def discovery():
    path = os.getcwd() + "/Themes"
    directories = []
    
    for filename in os.listdir(path):
        if filename.endswith(".udd"):
            directories.append(filename)
    
    try:
        with open('./Themes/Themes.json', 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        open('./Themes/Themes.json')

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