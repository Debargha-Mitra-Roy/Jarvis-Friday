import datetime
import speech_recognition as sr
import pyttsx3
import os

# import jarvis
# import friday

# Set the Speak Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)  # Voice of Zira


# Speak Function
def speak(audio):

    engine.say(audio)
    engine.runAndWait()


# Zira Start
def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am Zira. Please tell me how may I help you")


# # Run file
# def run(runfile):
#     with open(runfile, "r") as rnf:
#         exec(rnf.read())


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


# Logic for executing takes based on query
def logic():

    # Open Jarvis #
    if 'open jarvis' in query:
        print("Launching Jarvis...")
        speak("Launching Jarvis")
        os.system('python jarvis.py')

    # Open Friday
    elif 'my system is hacked' in query:
        print("Launching Friday...")
        speak("Don't worry sir, I am launching Friday")
        os.system('python friday.py')

    elif 'open friday' in query:
        print("Launching Friday...")
        speak("Launching Friday")
        os.system('python friday.py')

    # Identity
    elif 'who are you' in query:
        print("I am Zira. An AI Featured Destop Assistant")
        speak("I am Zira")

    # Checking health
    elif 'how are you' in query:
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
    elif 'exit zira' in query:
        print("Exiting...")
        exit()

    elif 'zira exit' in query:
        print("Exiting...")
        exit()

    # Quit
    elif 'quit zira' in query:
        print("Quitting...")
        quit()

    elif 'zira quit' in query:
        print("Quitting...")
        quit()

    else:
        print("Error 404!")
        speak("Sorry sir I can not do this.")


# Main Function
if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing takes
        logic()
