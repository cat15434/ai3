import pyttsx3
import os
import pyaudio
import speech_recognition as sr
from gtts import gTTS
from weather import weatherspeak
import playsound
from time1 import datespeak,timespeak




text_speech=pyttsx3.init()





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

    if "date" in text:
        text_speech.say(datespeak)
        text_speech.runAndWait()
        True
    if "time" in text:
        text_speech.say(timespeak)
        text_speech.runAndWait()
        True
    if "beans" in text:
        
        
        playsound.playsound ('yummy.mp3')
        True