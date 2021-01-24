import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning!")
    elif hour >= 12 and hour <=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(" I am Alex Sir. Please tell me how may I help you")
   
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
        
    try:
        print("Recongnizning...")
        query = r.recognize_google(audio , language='en-Tr')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("anlayamadım lütfen tekrarlayın...")
        
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('your email' , to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while 1:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("https://google.com/search?q=")
            
        elif 'search' in query:
            speak('searching...')
            query = query.replace("https://google.com/search?q=", "")
            result = "https://google.com/search?q="
            webbrowser.open("https://google.com/search?q="+ query)
            print(result + ' for you sir!')
     
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open twitch' in query:
            webbrowser.open("twitch.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"efendim , saat {strTime}")   
        
        elif 'email to me' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "Other Person email"
                sendEmail(to , content)
                speak("email has been sent:)")
            except Exception as e:
                print(e)
                speak("Sorry, sir I don't send the email! ")
        elif "stop" in query:
            exit()        
        