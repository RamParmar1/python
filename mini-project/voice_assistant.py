#voice recognition and assisting

import pyttsx3 #text to speech
import speech_recognition as sr # this will listen our voice when program run
import webbrowser # to search in web
import datetime
import pyjokes #to generate a random joke
import os #in this to play a song form our system in-built
import time
import smtp # addition for mailing

#1.SPEECH TO TEXT FUNCTION()
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            #changes 3.return data
        except sr.UnknownValueError:
            print("Not Understand")

sptext() #call the function sptext() if want

#2.TEXT TO SPEECH FUNCTION()
def speechtx():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') '''First get and then set through the voice & engine.
Male and Female Voice Selector also speed ,volume increase-decrease property'''
    engine.setProperty('voice',voices[0].id) #0 male,1 female,2female

    rate = engine.getProperty('rate') #speed setting.runtime speed change through the rate
    engine.setProperty('rate',120) #also we can do default value if nt type integer

    engine.say(x) #variable x for say to get data from x . to receive message 
    engine.runAndWait()
speechtx("hello, welcome here techy . how can i assist you?") #through the function call text is becoming speech by function itself

#IF WE WANT in second function to add external voice just set in get property voices to own     
    
#3.VOICE ASSISTANT NAME TO SPLITTING THE PROGRAM.WHEN NAME CALLED IT FUNCTION WORK. 
#TO USE OF import pyjokes MODULE.#USE OF THIS IS TO SPLIT THE PROGRAM means when call function it called.
if __name__ == '__main__':

     
    #if sptext().lower() == "hey jarvis" :
    #if "hey jarvis" == sptext().lower(): 
    #after while that we give more indent so note down.
        while True:
                data1 = sptext().lower()

                if "your name" in data1:
                    name = " my name is jarvis"
                    speechtx(name)

                elif "old are you" in data1:
                    age = "i am two years old"
                    speechtx(age)

                elif 'time' in data1:
                    time = datatime.datetime.now().strftime("%I%M%p")
                    speechtx(time)

                elif 'youtube' in data1: #In webbrowser module has open function which open system default browser item in tab
                    webbrowser.open("https://www.youtube.com/")

                elif "joke" in data1: #pyjokes function has random number jokes
                    joke_1  = pyjokes.get_joke(language = "en" , category = "neutral") #though the get_joke function random joke listen,language & different category
                    print(joke_1)
                    speechtx(joke_1)

                elif 'play song' in data1:
                    add = "" #add is used for address.after give the path of music.
                    listsong =  os.listdir(add)
                    print(listsong) #first add list of song and then print how many available.after that we can give start which play song when we assist
                    os.startfile(os.path.join(add , listsong[0])) #to play a song from list by index number(integer).
                    
                elif "exit" in data1:
                    speechtx("thank you")
                    break

                time.sleep(5)
              
        
    else:
        print("thanks")

#4.
    #last step is adding while before  data1 note it.
#5.
    #time delay for delaying time to some secondds otherwise it will listen all. import time function through the elif function. time.sleep like thread work.
#6.
    #change in first if condion if we say voice assistant's name then only it goes to loop otherwise it will not work.
        #just change name beforeand then condition. after one more indentation for don't getting error.
#7.
    #last step if we dont speak for a second in delay then it will do the try exception so add while in try except in sptext() function.
        #also we can add more good and reliable assistant and also add some other extra module like facebook and whatsapp functionality.

#we can also add an music for play in direct youtube and also we can play from our system in-built with adding o.s.(operating system) module.

#you are able to change in function and can add more functionality for getting better results.

