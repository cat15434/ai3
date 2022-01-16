from urllib import response
from black import re
import pyttsx3
import os,sys
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import ttstexts as tts
import webbrowser
import playsound
import requests
from urls import mathclassurl
from urls import indigenousstudiesurl
import time
import simplejson
from bs4 import BeautifulSoup
from lxml import html
import wikipedia
import psutil
from battery import batterytalk
from screenbrightness import currentbrightnesstext
from screenbrightness import adjustscreenbrightness
from playgame import rangeofgame
\

goodbye=tts.goodbyetext
class HiddenPrints:
   
   
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

   
   
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

with open ("name.txt","r") as f:
    named=f.read()

text_speech=pyttsx3.init()


def getaudio():
    r=sr.Recognizer()
  
  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        said=""

        try:
            
            said=r.recognize_google(audio)
        
        
        except Exception as e:
           
           
            with HiddenPrints():
                e=1+1
    
    
    return said.lower()




def setname():
    text_speech.say("What Would You like me to call you?")
    text_speech.runAndWait()
    r=sr.Recognizer()
    
    
    with sr.Microphone() as nae:
        name=r.listen(nae)
    
        named=r.recognize_google(name)
        named1=str(named)
       
       
        with HiddenPrints():
            print("You said your name is: {}".format(named))
      
      
        with open ("name.txt", "w") as f:
            f.write(str(named1))
    iwillcallyoutext="All right I Will call you",named1
    text_speech.say(iwillcallyoutext)
    text_speech.runAndWait()



def calculator():
    text_speech.say("What would you like me to calculate?")
    text_speech.runAndWait()

    r=sr.Recognizer()
    with sr.Microphone() as sourced:
        math1= r.listen(sourced)

    math2= r.recognize_google(math1)

    print (math2)
    num1 = math2[0]
    op = math2[2]
    num2= math2[4]
    print(num1,num2,op)
   
   
    def calculate(op,num1,num2):
        if "+" in op:
            a=int(num1)+int(num2)
            
        elif "*" in op:
            a=int(num1)*int(num2)
        elif"-" in op:
            a=int(num1)-int(num2)
        elif "/" in op:
            a=int(num1)/int(num2)
        elif "^":
            a=int(num1)**int(num2)
            b=num1,"to the power of",num2,"equals",a
        return b
    a=calculate(op,num1,num2)
    print(a)


greeting1=tts.greeting,named
T=True
F=False


            
    
def choices():
      

 while True:       
        
        text=getaudio()
        print("You said: {}".format(text))
        if"weather" in text:
            text_speech.say(tts.weatherspeak)
            text_speech.runAndWait()
            continue

        
        elif "date" in text:
            text_speech.say(tts.datespeak)
            text_speech.runAndWait()
            continue
      
      
        elif "time" in text:
            text_speech.say(tts.timespeak)
            text_speech.runAndWait()
            text_speech.say(greeting1)
            text_speech.runAndWait()
            continue
       
       
        elif "beans" in text:
            
            
            playsound.playsound ('yummy.mp3')
            continue

        elif "your name" in text:
            text_speech.say("My name is Python AI Technology, or Pat for short")
            text_speech.runAndWait()
            continue
       
       
        elif "set my name" in text:
            setname()
            continue
      
      
        elif "what's my name" in text:
            yournameistext="You told me your name is",named
            text_speech.say(yournameistext)
            text_speech.runAndWait()
            continue
       
       
        elif "calculate" in text:

            calculator() 
     
     
        elif "where am i" in text:
            text_speech.say(tts.location_text)   
            text_speech.runAndWait()
            continue
            

        elif "google" in text:
           webbrowser.open('https://www.google.com')
           continue
      
      
        elif "marketplace" in text:
            webbrowser.open('https://www.facebook.com/marketplace/')
            continue
      
      
        elif "look up" in text:
            keyword='look up'
            before_keyword, keyword, after_keyword = text.partition(keyword)
            searchobj=after_keyword
            googleurl='https://www.google.com/search?q='+ searchobj
            text_speech.say("Opening your query on your default browser")
            text_speech.runAndWait()
            webbrowser.open(googleurl)

            continue
       
       
        elif "tell me a joke" in text:
            text_speech.say("What did the babyboard say to the mother board")
            text_speech.runAndWait()
            time.sleep(5)
            text_speech.say("I want my data")
            text_speech.runAndWait()


            continue
       
       
        elif "what is the meaning of life" in text:
            text_speech.say("unlike other assistants i know this one drum roll please")
            text_speech.runAndWait()
            playsound.playsound('drum-roll-sound-effect.mp3')
            time.sleep(6)
            text_speech.say("its 42!")
            text_speech.runAndWait()
            continue
       
       
        elif "netflix" in text:
            webbrowser.open('www.netflix.com')
            continue
        
        
        elif "youtube" in text:
            webbrowser.open('www.youtube.com')
            continue
        
        
        elif "whats my brightness" in text:
                text_speech.say(currentbrightnesstext)
                text_speech.runAndWait()
                time.sleep(2)
                text_speech.say("You can ask me to adjust your brightness by saying adjust brightness")
        
        
        elif "adjust brightness" in text:
                adjustscreenbrightness()

        
        

        
        elif "whats my battery at" in text:
            text_speech.say(batterytalk)
            text_speech.runAndWait()
            continue


        elif "play a game" in text:
            rangeofgame()
## put all commands wanted before goodbye as wake() will not work otherwise
        elif "goodbye" in text:
            text_speech.say(goodbye)
            text_speech.runAndWait()
            wake()




activatemsg=greeting1,"how may i help you"      


def wake():
    WAKE='pat'
    while  True:
        
        
        text=getaudio()
        print(text)
        if text.count(WAKE) > 0:
            text_speech.say(activatemsg)
            text_speech.runAndWait()
            choices()

wake()

           

