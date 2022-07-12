from datetime import datetime
from webbrowser import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import random
import smtplib


# Create a Dictionary to send email
# Import from Gmail Contact List and save it in a dictionary
dict = {'dad': 'dad@gmail.com', 'college': 'college@gmail.com',
        'person': 'person@gmail.com'}


# Set the Speak Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)  # Voice of Friday


# Speak Function
def speak(audio):

    engine.say(audio)
    engine.runAndWait()


# Friday Start
def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am Friday. Please tell me how may I help you")


# Taking command from user
def takeCommand():

    # It takes microphone input from user and returns string Output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("listening")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)  # Print the exception for debugging
        print("Didn't recognize! Say that again...")
        speak("Please say that again")

        return "none"

    return query


# Send Email function
def sendEmail(to, content):  # First you have to enable "Less secure Apps"

    # Create a SMTP object for connection with server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()  # to identify itself when connecting to another email server to start the process of sending an email

    # TLS connection required by gmail
    server.starttls()  # to turn an existing insecure connection into a secure one

    server.login(input("Enter your Email : "), input(
        "Enter your Password : "))  # Your Email and Password

    server.sendmail(input("Enter sender Email : "),
                    to, content)  # Sender Email

    server.close()  # Close the server


# Logic for executing takes based on query
def logic():

    ### Opening in Webbrowser ###

    # Wikipedia
    if 'wikipedia' in query:
        print("Searching Wikipedia...")
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    # Google
    elif 'open google' in query:
        print("Opening Google...")
        speak("Opening Google")
        webbrowser.open("google.com")

    # Youtube
    elif 'open youtube' in query:
        print("Opening Youtube...")
        speak("Opening Youtube")
        webbrowser.open("youtube.com")

    # Stack Overflow
    elif 'open stackoverflow' in query:
        print("Opening Stack Overflow...")
        speak("Opening Stack Overflow")
        webbrowser.open("stackoverflow.com")

    ### Work on OS ###

    # Playing a random music
    elif 'play music' in query:
        music_dir = ''  # Music directory of your system # Windows
        # music_dir = ''  # Music directory of your system # Linux
        songs = os.listdir(music_dir)
        print(songs)
        count = 0
        # Iterate directory
        for path in os.listdir(music_dir):
            # check if current path is a file
            if os.path.isfile(os.path.join(music_dir, path)):
                count += 1
        n = random.randint(0, (count - 1))
        print("Playing Music...")
        # Friday surprise you a random music
        os.startfile(os.path.join(music_dir, songs[n]))

    # Open Sportify
    elif 'open sportify' in query:
        sportify_path = ''  # Sportify path # Windows
        # sportify_path = ''  # Spority path # Linux
        print("Opening Spority...")
        os.startfile(sportify_path)

    # Open VSCode
    elif 'open vscode' in query:
        vscode_path = ''  # VSCode path # Windows
        # vscode_path = ''  # VSCode path # Linux
        print("Opening VSCode...")
        os.startfile(vscode_path)

    # Send Email
    elif 'email to' in query:
        try:
            name = list(query.split())  # extract receiver's name
            name = name[name.index('to') + 1]
            speak("What should I say sir?")
            content = takeCommand()
            to = dict[name]  # Your email address
            sendEmail(to, content)
            print("Email has been sent!")
            speak("Email has been sent!")
        except Exception as e:
            # print(e)  # Print the exception for debugging
            print("Failed to send Email!")
            speak("Sorry sir, I have failed to send the email")

    ### Ask me Anything ###

    # Time
    elif 'tell me the time' in query:
        # strTime = datetime.datetime.now().strftime("%H:%M:%S")  # 24-Hours Clock
        # 12-Hours Clock
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            strTime = datetime.datetime.now().strftime("%I:%M:%S AM")
        else:
            strTime = datetime.datetime.now().strftime("%I:%M:%S PM")
        print("Sir, the time is " + {strTime})
        speak(f"Sir, the time is {strTime}")

    # Date
    elif 'tell me the date' in query:
        strDate = datetime.datetime.now().strftime("%d/%m/%Y")  # DD/MM/YYYY format
        print("Sir, the date is " + {strDate})
        speak(f"Sir, the date is {strDate}")

        # Tommorow
    elif 'tomorrow' in query:
        date = str(int(datetime.datetime.now().day) + 1)
        speak(date)

    # Leap-Year
    elif 'is this a leap year' in query:
        year = int(datetime.datetime.now().year)
        l = year % 4
        if l == 0:
            print("Leap-Year")
            speak("Yes this is a leap year")
        else:

            print("Not a Leap-Year")
            speak("No this is not a leap year")

    # Identity
    elif 'who are you' in query:
        print("I am Friday. An AI Featured Destop Assistant")
        speak("I am Friday. An AI Featured Destop Assistant")

    # Checking health
    elif 'How are you' in query:
        print("I am well sir, How are you")
        speak("I am well sir, How are you")

    # Wise me
    elif 'i am well' in query:
        print("Have a nice day sir")
        speak("Have a nice day sir")

    # Apologize about me
    elif 'i am not well' in query:
        print("Sorry about that sir, may you recover soon")
        speak("Sorry about that sir, may you recover soon")

    # Exit
    elif 'exit' in query:
        print("Exiting...")
        exit()

    # Quit
    elif 'quit' in query:
        print("Quitting...")
        exit()


# Main Function
if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing takes
        logic()
