<img src="https://i.imgur.com/Osbva2c.png" width="200" height="200">

# UniversalDynamicDesktop

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

UDD is a cross-platform dynamic desktop wallpaper application written in Python. It works on macOS, Windows, and Linux. The application allows users to create and use custom wallpaper themes that change throughout the day based on the time.

this app is in early development, **EXPECT BUGS**

## OS support
---
Right now UDD only supports MacOS, the plans are to support all platforms such as Linux and windows


## User settings
---
TBD


## Creating a new Theme
---
To create a new theme for UDD, create a directory with the following structure:

```
Theme.udd/
├─ images/
  │  ├─ 1.jpg
  │  ├─ 2.jpg
  │  ├─ 3.jpg
  │  ├─ 4.jpg 
├─ Wallpaper.json
```
the Wallpaper.json should look something like this:
```json
{
   "name":"Title",
    "desc":"Description",
    "Day":[
       {
          "id":1,
          "file":"Image name",
          "tag":"tag",
          "title":"Image title, shown when showWallpaperInfo is true",
          "desc":"Image description, shown when showWallpaperInfo is true"
       },
       {
          "id":2,
          "file":"Image name",
          "tag":"tag",
          "title":"Image title, shown when showWallpaperInfo is true",
          "desc":"Image description, shown when showWallpaperInfo is true"
       },
    ],
    "Night":[
       {
          "id":3,
          "file":"Image name",
          "tag":"tag",
          "title":"Image title, shown when showWallpaperInfo is true",
          "desc":"Image description, shown when showWallpaperInfo is true"
       },
       {
          "id":4,
          "file":"Image name",
          "tag":"tag",
          "title":"Image title, shown when showWallpaperInfo is true",
          "desc":"Image description, shown when showWallpaperInfo is true"
       },
    ]
 }
 ```

UDD automatically detects new themes in the .udd/Themes directory and allows for easy management of themes, including adding, deleting, and changing them.