import random
from pathlib import Path
from tkinter import E

import pyttsx3
import speech_recognition as sr

with open ((Path(__file__).parent / "gamehighscore.txt").resolve(), "r") as f:
    highscore=f.read()

speaker=pyttsx3.init()



def playagain(count):
    print("Congrants on winning in",count,"guesses would you like to play again?")
    playagaindecide=getaudiomath()
    if "yes" in playagaindecide:
        rangeofgame()
    elif "no" in playagaindecide:
        e=1


def playagainlost():
    print("unfourtunetly you didnt guess the number would you like to try again?")
    playagaindecide=getaudiomath()
    if "yes" in playagaindecide:
        rangeofgame()
    elif "no" in playagaindecide:
        e=1




def getaudiomath():
    print("Listening")
    r=sr.Recognizer()
    with sr.Microphone() as source:

        audio=r.listen(source)
        said=""

        
        try:    
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            e=1+1
        return said.lower()


def game(a,y,guessesallowed):
    a=a
    count=1
    while True:
        guesses_remaning="You currently have",guessesallowed-count,"Guesses remaining"
        speaker.say (guesses_remaning)
        speaker.runAndWait()
        guess=getaudiomath()
        try:
            guess=int(guess)
        except ValueError:
            invalidentry1="I think you said", guess ,"which is invalid please say a number and try again"
            speaker.say(invalidentry1)
            speaker.runAndWait()
            continue
        if guess > a and guess <y:
            count=count+1
            speaker.say("too high")
            speaker.runAndWait()
        elif guess< a and  guess >= 1 :
            speaker.say("too low")
            speaker.runAndWait()
            count=count+1
        elif guess>y:
            invalidentry="That number is over",y, "please say numbers under",y
            speaker.say(invalidentry)
            speaker.runAndWait()
        elif guess < 1:
            speaker.say("That number is lower than 1 please enter a number that is 1 or higher")
            speaker.runAndWait()
        elif guess == a:
            speaker.say("Congrats thats correct")
            speaker.runAndWait()
            if y==10:
                with open ( "gamehighscore.txt", "r") as f:
                    highscore=f.read()
                print (highscore)


                if count < int(highscore):
                        score=count
                        newhighscoretext="New highscore the previous highscore was",highscore,"guesses, you got it in",count,"guesses"
                        speaker.say(newhighscoretext)
                        speaker.runAndWait()
                        highscore=score
                   
                   

                with open ("gamehighscore.txt", "w") as f:
                        f.write(str(highscore))
                   
                   

            if y== 100:
                with open ( "gamehighscore1.txt", "r") as f:
                    highscore=f.read()
                if count <   int(highscore):
                    score=count
                    newhighscoretext="New highscore the previous highscore was",highscore,"guesses, you got it in",count,"guesses"
                    speaker.say(newhighscoretext)
                    highscore=score
                    with open ("gamehighscore1.txt", "w") as f:
                        f.write(str(highscore))
                   
                   


           
           

           
           
            else:
                playagain(count)

            return count
       
       
        elif guesses_remaning==0 and guess != a:
            speaker.say("You have no remaining guesses")
            speaker.runAndWait()
            playagainlost()
        
        

        print(count)
        




def randint(y,rangetext,guessesallowed):
     print(rangetext)
     a=random.randint(1,y)

     game(a,y,guessesallowed)
     return (a)



def rangeofgame():
    
    speaker.say("Welcome to guess that number please select your range 1 to 100 or 1 to 10")
    speaker.runAndWait()
    input1=getaudiomath()
    
    if "100" in input1:
        y=100
        
        rangetext="you have chosen a range of 1 to",y
        guessesallowed=25
        randint(y,rangetext,guessesallowed)
    elif "1210" in input1:
        y=10
        rangetext="You have chosen a range of 1 to" ,y
        guessesallowed=5
        randint(y,rangetext,guessesallowed)
    return y , rangetext,guessesallowed



rangeofgame()
