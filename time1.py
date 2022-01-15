
import datetime as dt
from time import time
import inflect

p=inflect.engine()
today= dt.date.today()
todays_date=f"{today:%A, %B %d, %Y}"

today.day


def day_suffix(day):
    if day<40:
        last_digit = day % 10
        if last_digit == 1 and day<10 and day <20:
            suffix="st"
        elif last_digit == 2 and day<10 and day <20:
            suffix="nd"
        elif last_digit == 3 and day<10 and day <20:
            suffix="rd"
        else:
            suffix="th"
    return suffix
  


day_suffix(today.day)
weekday=f"{today:%A}"
month=f"{today:%B}"
year=f"{today:%Y}"
daywords=p.number_to_words(today.day)

suffix=day_suffix(today.day)
suffixedday=daywords+suffix

datespeak="Todays Date is: ",weekday,month,"The",suffixedday,year

rightnow=dt.datetime.now()
hour=rightnow.strftime ("%H")
hourminute=rightnow.strftime("%H""%M")

def greetingdecide(hour,hourminute):
    if int(hour)<12 and int(hour)>6 and int(hour)!=0 and int(hour)!=1 and int(hour)!=2 and int(hour)!=3 and int(hour)!=4 and int(hour)!=5:
        greeting="Good Morning"
    if int(hour) >= 12 and int(hour)<17:
        greeting="Good Afternoon"
    if int(hour)>= 17 and int(hourminute) <2359:
        greeting = "Good evening"
    if int(hour) == 0:
        greeting="Its Midnight! Think about getting some sleep smiley face"
    if int(hour)>0 and int(hour)<6:
        greeting="You should really get some sleep zzz face"
    return greeting

greeting=greetingdecide(hour,hourminute)

curtime=f"{rightnow:%I %M %p}"
curtime2=curtime.lstrip('0')


timespeak="The Current Time is", curtime2
