from time1 import datespeak,timespeak,greeting
from geolocation import location_text
from weather import weatherspeak
from geolocation import city,country
with open ("name.txt","r") as f:
    named=f.read()
greeting=greeting
say_location=location_text
say_weather=weatherspeak
say_time=timespeak
say_date=datespeak
goodbyetext="Goodbye"+named+"I'll Stop listening now, But, You can turn me on any time by saying any phrase with, pat in it"