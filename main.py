import speech_recognition as sr
import pywhatkit as pwt
import pyttsx3
import subprocess
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')
pro=True
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
#Apps
    elif speech=="open":
        print("What do you want me to open?")
        engine.say("What do you want me to open")
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
        if speech=="chrome"or"google"or"google chrome":
            subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
    
while pro==True:
    print("Hello i am infinite your personal voice assistant")
    engine.say("Hello i am infinite your personal voice assistant")
    engine.runAndWait()
    print("What do you want me to do?")
    engine.say("What do you want me to do")
    engine.runAndWait()
    task() 



        


