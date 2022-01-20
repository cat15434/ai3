import math
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import pyttsx3    
text_speech1=pyttsx3.init()


def getaudiocalc():
    r=sr.Recognizer()
    with sr.Microphone() as sourced:
        math1= r.listen(sourced)
        try:
         math2=r.recognize_google(math1)
         
        except Exception as e:
            print("Didnt catch that try again")
        return math2.lower()

def calculate(op,num1,num2):
    if "+" in op:
        a=int(num1)+int(num2)
        b=num1,"plus",num2,"equals",a
        
    elif "*" in op:
        a=int(num1)*int(num2)
        b=num1,"multiplied by",num2,"equals",a
    elif"-" in op:
        a=int(num1)-int(num2)
        b=num1,"subrtact",num2,"equals",a
    elif "/" in op:
        a=int(num1)/int(num2)
        b=num1,"divided by",num2,"equals",a
    elif "^":
        a=int(num1)**int(num2)
        b=num1,"to the power of",num2,"equals",a
    print(b)
def getnumbers():
    text_speech1.say("Sure what would you like to calculate")
    text_speech1.runAndWait()
    math4=getaudiocalc()
    math3=math4.split(" ")
    num1=math3[0]
    num2=math3[2]
    op=math3[1]
    print(num1,num2,op)
    calculate(op,num1,num2)
    return op,num1,num2


def calculator():
    getnumbers()
