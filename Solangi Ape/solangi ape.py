import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from pygame import *
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def voiceUR():
    mixer.init()
    # load the mp3 file into pygame mixer
    mixer.music.load('va.mp3')

    # play the audio
    mixer.music.play()

    # wait until the audio has finished playing
    while mixer.music.get_busy():
        continue


    # release the mixer resources
    mixer.quit()


###############################################################################################################################################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Solangee Ape Voice Assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    voiceUR()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open spotify' in query:
            #webbrowser.open('https://open.spotify.com/playlist/4Phc7qScGy98kCDyvllRiB?si=1f3804653bb94251&pt=3ca8d2c4dfa65d9c5ee50f18f0f6250f')
            os.startfile("C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.216.947.0_x64__zpdnekdrzrea0\\Spotify.exe")

        elif 'open code' in query:
            codePath = "C:\\Users\\syedaFatimaAltaf\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ahsan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ahsan bhai. I am not able to send this email")    
