import pyttsx3
import os
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from weather import weatherspeak
import playsound
from time1 import datespeak,timespeak
from pathlib import Path
with open ("name.txt","r") as f:
    named=f.read()

text_speech=pyttsx3.init()
def setname():
    text_speech.say("What Would You like me to call you?")
    text_speech.runAndWait()
    with sr.Microphone() as nae:
        name=r.listen(nae)
        
        named=r.recognize_google(name)
        named1=str(named)
        print("You said your name is: {}".format(named))
        with open ("name.txt", "w") as f:
            f.write(str(named1))
    iwillcallyoutext="All right I Will call you",named1
    text_speech.say(iwillcallyoutext)
    text_speech.runAndWait()


T=True
F=False
r=sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("speak anything")
        audio= r.listen(source)

        text= r.recognize_google(audio)
        print("You said: {}".format(text))
    if"weather" in text:
        text_speech.say(weatherspeak)
        text_speech.runAndWait()
        True

    elif "date" in text:
        text_speech.say(datespeak)
        text_speech.runAndWait()
        True
    elif "time" in text:
        text_speech.say(timespeak)
        text_speech.runAndWait()
        True
    elif "beans" in text:
        
        
        playsound.playsound ('yummy.mp3')
        True

    elif "your name" in text:
        text_speech.say("My name is Python AI Technology, or Pat for short")
        text_speech.runAndWait()

    elif "set name" in text:
        setname()
    
    elif "what's my name" in text:
        yournameistext="You told me your name is",named
        text_speech.say(yournameistext)
        text_speech.runAndWait()

