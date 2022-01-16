import screen_brightness_control as sbc
import speech_recognition as sr
import pyttsx3
talk=pyttsx3.init()
current_brightness = sbc.get_brightness()
currentbrightnesstext="Your current brightness is",current_brightness,"percent"

def getaudiobright():
    r=sr.Recognizer()
    with sr.Microphone() as sourcebright:
        r.adjust_for_ambient_noise(sourcebright)
        brightness=r.listen(sourcebright)
        said=""

        try:
            
            said=r.recognize_google(brightness)
        except Exception as e:

                e=1+1
    return said.lower()

input=getaudiobright()

def adjustscreenbrightness():
    input = getaudiobright()
    sbc.set_brightness(int(input))
    current_brightness2 = sbc.get_brightness()
    brighttext="Ok your brightness is now set to",current_brightness2 , "percent"
    talk.say(brighttext)
      
