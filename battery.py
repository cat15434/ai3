import psutil
battery = psutil.sensors_battery()
  

if battery.power_plugged is False:
    batterytalk="your battery is currently at",battery.percent,"and is not charging"
elif battery.power_plugged is True:
    batterytalk="your battery is currently at",battery.percent,"and is currently charging"

batterytalk=batterytalk