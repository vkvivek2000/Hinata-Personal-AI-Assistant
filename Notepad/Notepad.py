import os
from datetime import datetime
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init() 
voice = engine.getProperty('voices') 
engine.setProperty('voice', voice[2].id)
engine.setProperty('rate',170)

def Say(Text):
    print("    ")
    print(f"Hinata : {Text}")
    engine.say(text= Text) 
    engine.runAndWait()
    print("    ")

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}\n")

    except:
        return ""

    query = str(query)
    return query.lower()

def Notepad():
    Say("What do you want to name the file?")
    file_name = Listen()

    Say("What do you want to write?")
    content = Listen()

    time = datetime.now().strftime("%H-%M-%S")

    file_path = f"C:\\Users\\vkviv\\OneDrive\\Desktop\\Ai assistant\\Notepad\\Notepad_files\\{file_name}-{time}.txt"

    with open(file_path, "w") as file:
        file.write(content)

    Say(f"The file {file_name} has been saved successfully.")
    
    Say("Do you want to open the file?")
    query = Listen().lower()

    if "yes" in query:
        os.startfile(file_path)
    elif "no" in query:
        Say("Ok. The file has been saved.")
    else:
        Say("I did not understand your response.")

    Say("Do you want me to close the Notepad?")
    query = Listen().lower()

    if "yes" in query:
        os.system("TASKKILL /F /IM notepad.exe")
        Say("Notepad has been closed.")
    elif "no" in query:
        Say("Ok. Notepad is still open.")
    else:
        Say("I did not understand your response.")

