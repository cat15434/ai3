import datetime as dt
import inflect
p=inflect.engine()
today= dt.date.today()
todays_date=f"{today:%A, %B %d, %Y}"
print(todays_date)
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
print(datespeak)
rightnow=dt.datetime.now()

curtime=f"{rightnow:%I %M %p}"
curtime2=curtime.lstrip('0')
print(curtime2)

timespeak="The Current Time is", curtime2
print(timespeak)