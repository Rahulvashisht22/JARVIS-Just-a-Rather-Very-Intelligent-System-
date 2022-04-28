import operator
import random
import smtplib
import time
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from googletrans import Translator
import webbrowser
import os
import cv2
import pywhatkit as kit
import pyjokes
from requests import get
import requests
from bs4 import BeautifulSoup
from weather import weather
import psutil
import instaloader
import PyPDF2
from pywikihow import search_wikihow
import sys



print("initializing jarvis")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)
#speak function will produce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage + "usage")

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def wishme():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir. it's {strTime}")
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir . it's {strTime}")
    else:
        speak(f"good Evening Sir . it's {strTime}")
    weather()
    cpu()
    speak("i am Jarvis . Please tell me how can I help you SIR??")

# this function take commands from the microphone

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(Source)

        #r.adjust_for_ambient_noise(Source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query


def takehindi():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening...")
        r.adjust_for_ambient_noise(Source)
        r.pause_threshold = 2
        audio = r.listen(Source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query

def Translate():
    while True:
        speak("tell me the line to translate!")
        line = takehindi()
        if "एग्जिट" in line or "क्लोज" in line:
            speak("Ok SIR , translator is closed")
            break
        else:
            translate = Translator()
            result = translate.translate(line)
            Text = result.text
            speak("The translation for this line is:" +Text)

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("yourmail@gmail.com", "password")
    server.sendmail("mail@gamil.com",to, content)
    server.close()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=a3b197d1f68e48a9826ca475b5d1d025'
    main_page = requests.get(main_url).json()
    #print(main_page)
    articles = main_page["articles"]
    head = []
    day = ["first","secound","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        engine.setProperty('rate', 180)

        print(f"today's {day[i]} news is: ", {head[i]})
        speak(f"today's {day[i]} news is: {head[i]}")



def taskexecution():
    speak(" initializing jarvis")
    wishme()
    while True:
        query = takecommand().lower()

        #logic for executing basic task
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("OK SIR , opening youtube")
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open_new("youtube.com")

        elif 'open facebook' in query:
            speak("OK SIR , opening facebook")
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open_new("facebook.com")


        elif 'open google' in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open_new("google.com")
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open_new(f"{cm}")

        elif 'open whatsapp' in query:
            speak("OK SIR , opening whatsapp")
            chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome).open_new("whatsapp.com")

        elif 'open notepad' in query:
            speak("OK SIR , opening notepad")
            path = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(path)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open chrome' in query:
            speak("OK SIR , opening chrome")
            path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path)

        elif 'open camera' in query:
            speak(" Ok SIR, opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img =cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(ip)

        elif 'play music' in query:
            speak("OK SIR , playing music")
            songs_dir = "C:\music"
            songs = os.listdir(songs_dir)
            d=random.choice(songs)
            os.startfile(os.path.join(songs_dir, d))

            while True:
                condi = takecommand().lower()
                if 'unique' in condi or 'special' in condi:
                    speak("Should i play Back in Black")
                    condi1 = takecommand().lower()
                    if 'yes' in condi1 or 'ok' in condi1:
                        os.startfile(os.path.join(songs_dir,songs[1]))
                    if 'no' in condi1:
                        speak("what should i play sir")
                if 'choice' in condi or 'want' in condi:
                    os.startfile(os.path.join(songs_dir, d))
                if 'exit' in condi or 'close' in condi:
                    speak("ok sir closing music")
                    break



        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'email to rahul' in query:
            try:
                speak("what should i send")
                content = takecommand()
                to = "rahul@gmail.com"
                sendmail(to, content)
                speak("email has been sent successfully")
            except Exception as e:
                print(e)

        elif "send message" in query:
            kit.sendwhatmsg("xxxxxxxxx","demo message",19,00 )

        elif 'no thanks' in query:
            speak("thanks for using me Sir, have a good day")
            sys.exit()

        elif 'alarm' in query:
            speak("Sir please tell me the time to set alarm. for example, set alarm to 5:30 am")
            al = takecommand()
            al = al.replace("set alarm to ","")
            al = al.replace(".","")
            al = al.upper()
            import MyAlarm
            MyAlarm.alarm(al)
            speak("Ok sir, the alarm is set")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)

#closing application
        elif 'close notepad' in query:
            speak("Sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close chrome' in query:
            speak("Sir, closing Chrome  `1")
            os.system("taskkill /f /im Chrome.exe")

        elif 'close browser' in query:
            speak("Sir, closing this browser")
            os.system("taskkill /f /im msedge.exe")

        elif 'stop music' in query:
            speak("Sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'restart' in query:
            speak("do you want to restart the computer?")
            take = takecommand()
            choices = take
            if choices == 'yes':
                print("Restarting the computer")
                speak("Restarting the computer")
                os.system("shutdown /r /t 1")
            if choices == 'no':
                print("ok Sir")
                speak("ok Sir")

        elif 'shutdown' in query:
            speak("do you want to shutdown the computer?")
            take = takecommand()
            choices = take
            if choices == 'yes':
                print("Shut down the computer")
                speak("Shut the computer")
                os.system("shutdown /s /t 1")
            if choices == 'no':
                print("ok Sir")
                speak("ok Sir")

        elif 'switch the window' in query:
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif "temperature" in query:
            search = "temperature in solan"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get("https://api.ipify.org").text
                print(ipAdd)
                url = "https://get.geojs.io/v1/ip/geo/"+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                region =geo_data['region']
                speak(f"Sir i am not sure, but i think we are in {city} city of {region} {country} ")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass

        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user{name}")
            time.sleep(5)
            speak("Sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition :
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready to take another command")
            else:
                pass

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("sir please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder, now i am ready for taking another command")

        elif "read" in query or "read book" in query:
            book = open('opp.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"total numbers of pages in this book {pages}")
            speak("Sir please enter the page number i have to read")
            pg = int(input("please enter the page number:"))
            page = pdfReader.getPage(pg).extractText()
            speak(page)

        elif "how are you" in query:
            speak("I am good SIR. and what about you.")
        elif "are you there" in query:
            speak("YES SIR. i am always at your service.")

        elif 'voice to female' in query:
            speak("OK SIR , i am changing my voice")
            engine.setProperty('voice', voices[2].id)
            speak("Hello Sir, I am the Female version of jarvis")

        elif 'voice to male' in query:
            engine.setProperty('voice',voices[0].id)
            speak("ok sir , i have changed my voice . now is it ok?")

        elif 'activate how to do mode' in query:
            speak("How to do mode is activated. please tell me what you want to know ")
            while True:
                engine.setProperty('rate',170)
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        engine.setProperty('rate',200)
                        speak("Ok SIR , how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry Sir, I am not able to find this")

        elif 'your master' in query:
            speak('Rahul is my master. He created me couple of days ago')

        elif 'news' in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "translate" in query or "translator" in query:
            Translate()

        elif "remember that" in query:
            remember = query.replace("remember that","")
            remember = remember.replace("jarvis","")
            speak("you tell me to remind you that:" +remember)
            remembermsg = open('data.txt','w')
            remembermsg.write(remember)
            remembermsg.close()

        elif "remember" in query:
            remembermsg = open('data.txt','r')
            speak(f"you tell me that {remembermsg.read()}")

        elif "you need a break" in query or "sleep" in query or "goodbye" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif "do some calculation" in query or "calculate" in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as Source:
                    speak("Say what you want to calculate, example 3 plus 3")
                    print("listening...")
                    r.adjust_for_ambient_noise(Source)
                    audio = r.listen(Source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        "+" : operator.add,
                        "-" : operator.sub,
                        "x" : operator.mul,
                        "divided" : operator.__truediv__,
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                print(e)
                print("say that again please")
                return "None"
            return my_string



     




if __name__ == "__main__":
    taskexecution()



