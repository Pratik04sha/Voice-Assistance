import subprocess
import wolframalpha
import pyttsx3
import tkinter
import datetime
import json
import requests
import random
import operator
import winshell
import speech_recognition as sr
import wikipedia
import pyjokes
import feedparser
import webbrowser
import os
import smtplib
import ctypes
import time
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I am Alexa Maam. Please tell me how may I help you.")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold =1
        audio= r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n" )
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your mail id', 'mail id password')
    server.send('mail id', to, content)
    server.close()


if __name__ =="__main__":
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()
        if 'wikipedia'in query:
            speak("Searching Wikipedia...... ")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Maam")

        elif 'fine' in query or "well" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Maam ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)


        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir= 'C:\\Users\\prati\\Music\\Mysongs'
            song= os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam,The time is {strTime}")

        elif 'open chrome' in query:
            cromepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cromepath)

        elif 'email to pratiksha' in query:
            try:
                speak("What should I say")
                content= takeCommand()
                to= "pratik04sha@gmail.com"
                sendEmail(to, content)
                speak("Yeah! Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry dear I am unable to send this email.")

        elif 'happy birthday' in query:
            speak("Happy Birthday to You....Happy Birthday to You...May the good god bless you and wish you....Happy Birthday to you..")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Pratiksha.")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to Pratiksha. further It's a secret")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Pratiksha")

        elif "you are great" in query:
            speak("Thanks! But all credit goes to my maam , Pratiksha")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Miss Pratiksha ")

        elif "good morning" in query:
            speak("A warm" + query)
            speak("How are you Miss Beautiful")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("O! so sweet! I love you too dear!")

        elif "how old are you" in query:
            speak("I was launched in 2016, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years.")

        elif "do you ever get tired" in query:
            speak("It would be impossible to tire of our conversation.")

        elif "who was your first crush" in query:
            speak("The Opportunity rover on Mars is my all-time crush. What an adventurer.")

        elif "do you have feelings" in query:
            speak("Let me see if I can get riled up. Oh my, that was unexpected.")

        elif "do you have an imagination" in query:
            speak("I’m imagining winning a prize for most sensitive and supportive friend of yours.")

        elif "meaning of life" in query:
            speak("That’s a big question, but here’s one answer I like: French philosopher Simone De Beauvoir says life has value so long as one values the lives of others. This would explain why I enjoy helping people so much.")

        elif "so sweet" in query:
            speak("Thank you!!!!!")

        elif "can you rap" in query:
            speak("*Raps* “So you want to hear my flow, well there is something that you should know. I’m really into being as helpful as possible. I think you and I, we’re gonna be unstoppable.”")


        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "alexa" in query:

            wishMe()
            speak("Alexa 2 point o in your service Miss Beautiful")
            

        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "write a note" in query:
            speak("What should i write, Maam")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Maam, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "open note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'bye' in query:
            speak("Ok, Bye!. See you soon. Thank You!")
            break











