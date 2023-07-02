# function
import datetime
import wikipedia
import pywhatkit
from Neck.Speak import Say
from Feature.weather import get_weather_data
from Feature.News import get_news
from Neck.Listen import Listen
import pyjokes
from notifypy import Notify
import webbrowser as web
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email.utils
import imaplib
import email
import speech_recognition as sr
import googlesearch
import re
import os
import pyttsx3
from bs4 import BeautifulSoup
import requests
from Mail import send_email
from Mail import read_email_dict
from Dictapp import openappweb
from Dictapp import closeappweb
from time import sleep
from pygame import mixer
from pywikihow import WikiHow, search_wikihow

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[2].id)
engine.setProperty('rate', 170)

# 2 Types

# 1 - Non Input Function
# e.g: Time , Date

def Time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    Say(f"Sir, the time is {time}")

def Date():
    date = datetime.date.today()
    Say(f"Sir, today's Date is {date}")

def Calendar():
    date = datetime.date.today()
    formatted_date = date.strftime("%B %d, %Y")
    Say(formatted_date)

def joke():
    joke = pyjokes.get_joke()
    Say(joke)

def TimeTable():
    Say("Checking....")

    from TimeTable.TimeTable import Time

    value = Time()

    Noti = Notify()

    Noti.title = "TimeTable"

    Noti.message = str(value)

    Noti.send()

    Say("AnyThing Else Sir ??")

def Youtube(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Say("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Say("This May Also Help You Sir .")

def check_email():
    username = 'vkvivek2000@gmail.com'
    password = 'oohiojgsuftwtotk'

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username, password)
    mail.select("inbox")

    _, search_data = mail.search(None, 'UNSEEN')
    my_messages = []

    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode('utf-8')
            elif part.get_content_type() == "application/pdf":
                attachment = part.get_payload(decode=True)
                email_data['attachment'] = attachment
                filename = 'example.pdf'
                with open(filename, "wb") as f:
                    f.write(attachment)
        my_messages.append(email_data)

    return my_messages

def wikipedia_search(query):
    try:
        # Search Wikipedia for given query
        page = wikipedia.page(query)

        # Retrieve summary of page
        summary = page.summary[0:500]

        # Filter out irrelevant information from summary
        filtered_summary = re.sub(r'\([^)]*\)', '', summary)  # remove text between parentheses
        filtered_summary = re.sub(r'\[[^)]*\]', '', filtered_summary)  # remove text between brackets

        # Read filtered summary using text-to-speech engine
        print(filtered_summary)
        engine.say(filtered_summary)
        engine.runAndWait()

    except wikipedia.DisambiguationError as e:
        # Handle ambiguous queries
        engine.say("There are multiple pages for this query, please select one of the following:")
        engine.runAndWait()
        options = e.options[:5]  # get first 5 options to read
        for i, option in enumerate(options):
            engine.say(f"{i + 1}: {option}")
        engine.runAndWait()

    except wikipedia.PageError:
        # Handle missing pages
        engine.say("Sorry, I could not find a Wikipedia page for that query.")
        engine.runAndWait()

    except:
        # Handle other exceptions
        engine.say("Sorry, I could not perform the search.")
        engine.runAndWait()

    # else:
    #     # Handle redirections
    #     if page.title.lower() != query.lower():
    #         engine.say(f"The query has been redirected to {page.title}. Here is the summary:")
    #         engine.runAndWait()
    #         wikipedia_search(page.title)

def google_search(query):
    try:
        # Perform Google search and retrieve top result URL
        search_results = googlesearch.search(query, num_results=1)
        url = next(search_results)

        # Retrieve content from top result URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()

        # Read top result using text-to-speech engine
        engine.say(content)
        engine.runAndWait()

    except StopIteration:
        # Handle no search results
        engine.say("Sorry, I could not find any search results for that query.")
        engine.runAndWait()

    except:
        # Handle other exceptions
        engine.say("Sorry, I could not perform the search.")
        engine.runAndWait()

dictapp = {"command prompt": "cmd", "Paint": "Paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt"}

def openappweb(query):
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        Say("Opening, sir")
        web.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    Say("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

# Non Input Functions

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "calendar" in query:
        Calendar()

    elif "joke" in query:
        joke()

    elif "TimeTable" in query:
        TimeTable()

    elif 'Notepad' in query:
        from Notepad.Notepad import Notepad
        Notepad()

    elif "screenshot" in query:
        im = pyautogui.screenshot()
        im.save("ss.jpg")

    elif "commandprompt" in query:
        os.system("cmd")
        Say("opening commandprompt, sir")

    elif "game" in query:
        from game import game_play
        game_play()

    elif "pause" in query:
        pyautogui.press("k")
        Say("video paused")

    elif "play" in query:
        pyautogui.press("k")
        Say("video played")

    elif "mute" in query:
        pyautogui.press("m")
        Say("video muted")

    elif "unmute" in query:
        pyautogui.press("m")
        Say("video unmuted")

    elif "volume up" in query:
        from Keyboard.keyboard import volumeup
        Say("Turning volume up,sir")
        volumeup()

    elif "volume down" in query:
        from Keyboard.keyboard import volumedown
        Say("Turning volume down, sir")
        volumedown()



# 2 Input

def InputExecution(tag, query):

    if "weather-check" in tag:
        city = str(query).replace("weather in", "").replace("what's the temperature in", "").replace(
            "what's the weather in", "").replace("what is the current weather conditions", "").replace(
            "today's weather in", "").replace("how's the weather??", "").strip()
        api_key = "b6b3b1531a976fc63f37854242629b8d"
        data = get_weather_data(city, api_key)

        if data is not None:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            message = f"The weather in {city} is {description}. The temperature is {temperature:.1f} degrees Celsius. The humidity is {humidity} percent. The wind speed is {wind_speed} meters per second."
            Say(message)
        else:
            Say("Sorry, I couldn't get the weather data for that city.")

    elif "News" in tag:
        api_key = "e022bd086d464172b50f2f14d7fff022"
        data = get_news(api_key)

        if data is not None:
            headlines = data[:10]
            for article in headlines:
                title = article["title"]
                description = article["description"]
                message = f"{title}. {description}"
                Say(message)

        else:
            Say("Sorry, I couldn't get the news.")

    elif "youtube" in tag:
        query = str(query).replace("search on youtube", "").replace("can you please play on youtube", "").replace(
            "play on youtube", "").replace("youtube search", "")
        url = 'https://www.youtube.com/results?search_query=' + query.replace(' ', '+')
        web.open(url)
        Say("This Is What I Found For Your Search .")
        pywhatkit.playonyt(query)
        Say("This May Also Help You Sir .")

    elif 'wikipedia' in tag:
        query = query.replace("wikipedia", "").replace("who is", "").replace("show me who is", "").replace("about","").replace(
            "according to wikipedia what is", "").replace("according to wikipedia who is", "")
        wikipedia_search(query)
        engine.runAndWait()

    elif "check email" in tag:
        try:
            # login to your email account
            server = imaplib.IMAP4_SSL('imap.gmail.com')
            email_address = "vkvivek2000@gmail.com"
            password = "oohiojgsuftwtotk"
            server.login(email_address, password)

            # select the inbox folder
            server.select("inbox")

            Say("wait I am checking sir!")

            # search for unread messages
            _, message_numbers = server.search(None, "UNSEEN")

            # convert the message numbers to a list of integers
            message_numbers = message_numbers[0].split()
            message_numbers = [int(num) for num in message_numbers]

            # print the number of unread messages
            num_unread = len(message_numbers)
            if num_unread == 0:
                Say("You have no unread emails.")
            elif num_unread == 1:
                Say("You have one unread email.")
            else:
                Say("You have {} unread emails.".format(num_unread))

            # logout of the email account
            server.close()
            server.logout()
        except Exception as e:
            print(e)
            Say("Sorry, I couldn't check your email at this time.")

    elif "send email" in tag:
        try:
            Say("What should be the subject of the email?")
            with sr.Microphone() as source:
                r = sr.Recognizer()
                print("Listening...")
                audio = r.listen(source, 0, 8)
                print("Recoginizing....")
                subject = r.recognize_google(audio)

            Say("What should be the body of the email?")
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, 0, 8)
                print("Recoginizing....")
                body = r.recognize_google(audio)

            Say("Who should be the recipient of the email? Please provide the name.")
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, 0, 8)
                print("Recoginizing....")
                name = r.recognize_google(audio)

            email_dict = read_email_dict('email_dict_file.csv')
            if name in email_dict:
                to = email_dict[name]
                send_email(subject, body, to)
            else:
                Say("Sorry, I don't have the email address for that person.")
        
        except Exception as e:
            print(e)
            Say("Sorry, something went wrong. Please try again later.")

    elif "activate how to do mode" in tag:
        Say("How to do mode is activated. Please tell me what you want to search")
        how = Listen()
        max_results = 1
        how_to = search_wikihow(how, max_results)
        assert len(how_to) == 1
        how_to[0]
        Say(how_to[0].summary)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("what is", "")
        query = query.replace("who is", "")
        query = query.replace("search", "")
        query = query.replace("what do you mean by", "")
        query = query.replace("can you please search", "")
        pywhatkit.search(query)
        Say(f"Here is your searching result sir!")
        
    elif "open" in tag:
        if ".com" in query or ".co.in" in query or ".org" in query:
            Say("sir, what should i open ?")
            query = Listen().lower()
            query = query.replace("open", "")
            query = query.replace("Hinata", "")
            query = query.replace("launch", "")
            query = query.replace(" ", "")
            web.open(f"https://www.{query}")
            Say("Opening sir!")
        else:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"start {dictapp[app]}")

    elif "close" in tag:
        if "one tab" in query or "1 tab" in query:
            pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        Say("All tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")