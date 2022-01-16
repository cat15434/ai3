import random
from tkinter import E
from matplotlib.pyplot import text
import speech_recognition as sr
import pyttsx3
from ai3 import wake
from pathlib import Path
with open ((Path(__file__).parent / "gamehighscore.txt").resolve(), "r") as f:
    highscore=f.read()

speaker=pyttsx3.init()



def playagain(count):
    print("Congrants on winning in",count,"guesses would you like to play again?")
    playagaindecide=input()
    if "yes" in playagaindecide:
        rangeofgame()
    elif "no" in playagaindecide:
        wake()


def playagainlost():
    print("unfourtunetly you didnt guess the number would you like to try again?")
    playagaindecide=input()
    if "yes" in playagaindecide:
        rangeofgame()
    elif "no" in playagaindecide:
        wake()

















def getaudiomath():
    r=sr.Recognizer
    with sr.Microphone as source:
        r.adjust_for_ambient_noise(source)
        audioguess=r.listen(source)
        spoken=r.recognize_google(audioguess)
        return spoken.lower()



def game(a,y,guessesallowed):
    a=a
    count=1
    while True:
        guesses_remaning=guessesallowed-count
        print (guesses_remaning)
        guess=int(input())
        if guess > a and guess <y:
            count=count+1
            print("too high")
        elif guess< a and  guess >= 1 :
            print("too low")
            count=count+1
        elif guess>y:
            print("That number is over",y, "please say numbers under",y)
        elif guess < 1:
            print("That number is lower than 1 please enter a number that is 1 or higher")
        elif guess == a:
            print("Congrats thats correct")
            if y==10:
                with open ( "gamehighscore.txt", "r") as f:
                    highscore=f.read()
                print (highscore)


                if count > int(highscore):
                        score=count
                        print("New highscore the previous highscore was",highscore,"guesses, you got it in",count,"guesses")
                        highscore=score
                   
                   

                with open ("gamehighscore.txt", "w") as f:
                        f.write(str(highscore))
                   
                   

            if y== 100:
                with open ( "gamehighscore1.txt", "r") as f:
                    highscore=f.read()
                if count > int(highscore):
                    score=count
                    print("New highscore the previous highscore was",highscore,"guesses, you got it in",count,"guesses")
                    highscore=score
                    with open ("gamehighscore1.txt", "w") as f:
                        f.write(str(highscore))
                   
                   


           
           

           
           
            else:
                playagain(count)

            return count
       
       
        elif guesses_remaning==0:
            print("You have no remaining guesses")
            playagainlost()
        
        

        print(count)
        




def randint(y,rangetext,guessesallowed):
     print(rangetext)
     a=random.randint(1,y)
     print(a)
     game(a,y,guessesallowed)
     return (a)



def rangeofgame():
    input1=input()
    speaker.say("Welcome to guess that number please select your range 1 to 100 or 1 to 10")
    speaker.runAndWait()
    if "1 to 100" in input1:
        y=100
        
        rangetext="you have chosen a range of 1 to",y
        guessesallowed=25
        randint(y,rangetext,guessesallowed)
    elif "1 to 10" in input1:
        y=10
        rangetext="You have chosen a range of 1 to" ,y
        guessesallowed=5
        randint(y,rangetext,guessesallowed)
    return y , rangetext,guessesallowed

y=rangeofgame()



