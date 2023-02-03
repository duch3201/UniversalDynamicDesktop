https://i.imgur.com/5aBZoC9.png

# UniversalDynamicDesktop (UDD)

UDD is a cross-platform dynamic desktop wallpaper application written in Python. It works on macOS, Windows, and Linux. The application allows users to create and use custom wallpaper themes that change throughout the day based on the time.

## Creating a new theme

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
    "name":"Theme title",
    "desc":"Theme desc",
    "Day":[
       {
          "file":"1.png",
          "tag":"dawn"
       },
       {
          "file":"2.png",
          "tag":"day"
       }
    ],
    "Night":[
       {
          "file":"3.png",
          "tag":"sunset"
       },
       {
          "file":"4.png",
          "tag":"night"
       }
    ]
 }
```


UDD automatically detects new themes in the .udd/Themes directory and allows for easy management of themes, including adding, deleting, and changing them.