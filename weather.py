import geolocation
from geolocation import city
from geolocation import state
import json
import requests


api_key = "9d8cf41bd380ba4e11068bf06dbd321f"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 

city_name = city

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
 

x = response.json()
 


if x["cod"] != "404":
 

    y = x["main"]
 
    
    current_temperature = y["temp"]
 
   
    current_pressure = y["pressure"]
 

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]
 


curtemp=current_temperature-273.15
mindecimals="{:.1f}".format(curtemp)
str(mindecimals)

weatherspeak=("In", city,state ,"The temperature is",mindecimals,"Degrees Celsius") 