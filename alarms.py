import datetime as dt
import time
import os
import speech_recognition as sr
import pyttsx3 
import multiprocessing
import playsound





def getaudioalarms():
    r=sr.Recognizer()
    with sr.Microphone() as source4:
     audio4=r.listen(source4)
     said4=""   
    try:
            
            said4=r.recognize_google(audio4)
            print(said4)
        
    except Exception as e:
           
                print("Sorry I didnt catch that")


    return said4.lower()


def alarmsset():
    timeset=getaudioalarms()
    if "p.m." in timeset:
        timeset1=timeset.replace(':',' ')
        timeset2=timeset1.split(' ')
        timesethour=timeset2[0]
        print(timesethour)
        timesetminute=timeset2[1]
        print(timesetminute)
        alarmampm="PM"
    if "a.m." in timeset:
        timeset1=timeset.replace(':',' ')
        timeset2=timeset1.split(' ')
        timesethour=timeset2[0]
        print(timesethour)
        timesetminute=timeset2[1]
        print(timesetminute)
        alarmampm="AM"
    alarm=timesethour,':',timesetminute,alarmampm
    alarm1=str(alarm).replace("'",'')
    alarm1=str(alarm1).replace(",",'')
    alarm1=str(alarm1).replace("(",'')
    alarm1=str(alarm1).replace(")",'')
    alarm1=str(alarm1).replace(" ",'')
    alarm1=str(alarm1).replace("PM",' PM')
    alarm1=str(alarm1).replace("AM",' AM')
    checktime(alarm1)
def checktime(alarm1):
    while True:
        time3=dt.datetime.now()
        time1=f"{time3:%I:%M %p}"
        time1=time1.lstrip('0')
        
        
        if alarm1 == time1:
            print("yes")
            
            playsound.playsound('alarm.mp3')
            break
        else:
            pass
def alarmsfunc():
    alarmsset()