import geolocation
from geolocation import city,country
from geolocation import state
import json
import requests
import webbrowser

api_key = "9d8cf41bd380ba4e11068bf06dbd321f"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
countrycode=country[:2]
countrycode1=countrycode.strip()
city_name = city
print(countrycode1)
complete_url = base_url + "appid=" + api_key + "&q=" + city_name+","+countrycode1

response = requests.get(complete_url)


x = response.json()
 


if x["cod"] != "404":
 

    y = x["main"]
 
    
    current_temperature = y["temp"]
 
   
    current_pressure = y["pressure"]
 

    current_humidity = y["humidity"]
    feel_like = y["feels_like"]
    z = x["weather"]

    weather_description = z[0]["description"]
 

feelslike=feel_like-273.15
curtemp=current_temperature-273.15
mindecimals="{:.1f}".format(curtemp)
mindecimals1="{:.1f}".format(feelslike)
str(mindecimals)
str(mindecimals1)





def goodspeech1(mindecimals1):
        mindecimals1.startswith('-')
        x=mindecimals1
        y = x[0]
        z = x[1:]
        mindecimals1="negative",z
        return mindecimals1


mindecimals1=goodspeech1(mindecimals1)

def goodspeech(mindecimals):
    mindecimals.startswith('-')
    x=mindecimals
    y = x[0]
    z = x[1:]
    mindecimals="negative",z
    return mindecimals
mindecimals=goodspeech(mindecimals)


weatherspeak=("In", city,state ,"The temperature is",mindecimals,"Degrees Celsius","but it feels like",mindecimals1,"Degrees Celsius")