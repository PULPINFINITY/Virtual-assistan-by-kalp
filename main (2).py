import speech_recognition as sr
import pywhatkit as pwt
import pyttsx3
import subprocess
import datetime
import random
jokes = [ "What do you call a boomerang that won’t come back. A stick","Why wasnt the bike working. because it was two tired","why dont pirates shower before they walk up the plank. they just wash up on shore" , "i threw a boomerang a few years ago now i live in constant fear","parelel lines have so much in commomn. its a shame they'll never meet","someone stole my mood ring, i dont know how i feel about that","my granpa has the heart of a lion and a lifetime ban at the zoo"]                                 
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def task():
#SEARCH
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        engine.runAndWait()
        audio = r.listen(source)
        speech= r.recognize_google(audio)
        speech.lower()
        try:
            print("You have said: \n"+speech)
    
        except Exception as e:
            print("Error"+ str(e))
    if speech=="search":
        print("what do you want to search?")
        engine.runAndWait()
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Please say something...")
            engine.runAndWait()
            audio = r.listen(source)
            speech= r.recognize_google(audio)
            speech.lower()
            try:
                print("You have said: \n"+speech)
                engine.runAndWait()

            except Exception as e:
                print("Error"+ str(e))
        pwt.search(speech)
#SEARCH CLOSE
    if speech=="tell me a joke":
       
        joke= random.choice(jokes)
        print(joke)
        
    
#end

    
print("Hello i am infinite your personal voice assistant")
engine.say("Hello i am infinite your personal voice assistant")
engine.runAndWait()
print("What do you want me to do?")
engine.say("What do you want me to do")
engine.runAndWait()
task()




        


