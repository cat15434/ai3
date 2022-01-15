from black import re
import pyttsx3
import os,sys
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import ttstexts as tts
import webbrowser
import playsound

import time
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
      

        
        
        text=getaudio()
        print("You said: {}".format(text))
        if"weather" in text:
            text_speech.say(tts.weatherspeak)
            text_speech.runAndWait()
            choices()

        elif "date" in text:
            text_speech.say(tts.datespeak)
            text_speech.runAndWait()
            choices()
        elif "time" in text:
            text_speech.say(tts.timespeak)
            text_speech.runAndWait()
            text_speech.say(greeting1)
            text_speech.runAndWait()
            choices()
        elif "beans" in text:
            
            
            playsound.playsound ('yummy.mp3')
            choices()

        elif "your name" in text:
            text_speech.say("My name is Python AI Technology, or Pat for short")
            text_speech.runAndWait()
            choices()
        elif "set name" in text:
            setname()
            
        elif "what's my name" in text:
            yournameistext="You told me your name is",named
            text_speech.say(yournameistext)
            text_speech.runAndWait()
            choices()
        elif "calculate" in text:

            calculator() 
        elif "where am i" in text:
            text_speech.say(tts.location_text)   
            text_speech.runAndWait()
            choices()
            

        elif "google" in text:
           webbrowser.open('https://www.google.com')
        elif "marketplace" in text:
            webbrowser.open('https://www.facebook.com/marketplace/')
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

           

