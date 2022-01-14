import math
import speech_recognition as sr
from gtts import gTTS
import pyaudio
        
e=sr.Recognizer()
with sr.Microphone() as sourced:
        math1= e.listen(sourced)

        math2= e.recognize_google(math1)
        math3=math2.replace(" ","")
        num1 = math3[0]
        op = math3[1]
        num2=math3[2]
        print(op)
def calculate(op,num1,num2):
    if "+" in op:
        a=num1+num2
    return a

