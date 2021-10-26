import pyttsx3
import speech_recognition as sr
import datetime
import os
import os.path
import cv2
import ipaddress
import psutil
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import speedtest
import time
import pyautogui
import PyPDF2
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders
import instaloader
import operator
import geocoder
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from JarvisUI import Ui_JarvisUi







engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print('voice',voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

#speak function
def speak(audio):
        print(audio)
        engine.say(audio)
        engine.runAndWait()

def wish():

        hour = int(datetime.datetime.now().hour)

        tt = time.strftime("%I:%M %p")


        if hour>=0 and hour<=12:
            speak(f'Good morning. its  {tt}')
        elif hour>12 and hour<18:
            speak(f'Good afternoon. its  {tt}')
        else:
            speak(f'Good evening. its {tt}')    

        speak('I am online sir . May i help you with something') 

def pdf_reader():
        book = open('Python-cheat-sheet-April-2021.pdf','rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        speak(f'sir total number of pages in this book are{pages}')
        speak('sir please enter the page no. that i should read')
        pg = int(input("please enter the page number that i should read: "))
        page = pdfReader.getPage(pg)
        text = page.extractText()
        speak(text)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manurajthyparambil@gmail.com','Next@123')
    server.sendmail('manurajthyparambil@gmail.com' ,to, content)
    server.close()

def news():
        main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e683e2b6bff345ea83c7f5b28649311d"
        main_page = requests.get(main_url).json()
        articles = main_page["articles"]
        head = []
        day = ["first","second","third","fourth" ,"fifth"]
        for ar in articles:
            head.append(ar['title'])
        for i in range(len(day)):
            speak(f"today's {day[i]} news is:{head[i]}")

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
       while True:
           self.query = self.takeCommand()
           if 'activate' in self.query:
               self.TaskExecution()
        

    def takeCommand(self):

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print('Listening...')
                r.pause_threshold = 1
                # r.adjust_for_ambient_noise(source)
                # audio = r.listen(source)
                audio = r.listen(source, timeout=4, phrase_time_limit=7)

            try:
                print('Recognizing...')
                query = r.recognize_google(audio, language='en-in')
                print(f'User Said: {query}')

            except Exception as e:
                #speak('say that again please...')
                return "none"
            query = query.lower()
            return query
        
    def TaskExecution(self):
        # speak('manu is a good boy')
        wish()
        while True:
        # if 1:
                self.query = self.takeCommand()

                #Logic for building the whole jarvis

                if 'open notepad' in self.query:
                    speak('opening notepad')
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")

                elif 'how are you' in self.query:
                    speak('I am perfectly fine sir. What about you?')

                elif 'fine' in self.query:
                    speak('ohh great pleasure sir')

                elif 'how is it going on' in self.query:
                    speak('greate going on sir. What about you')  

                elif 'close notepad' in self.query:
                    speak('okay sir,closing notepad')
                    os.system('taskkill /f /im notepad.exe')
                
                elif 'open code' in self.query:
                    speak('opening code')
                    os.startfile("C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk")
                
                elif 'close code' in self.query:
                    speak('Okay sir , closing code')
                    os.system('taskkill /f /im Code.exe')

                elif 'open command prompt' in self.query:
                    speak('opening comand prompt')
                    os.startfile("C:\\Users\\Dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk")
                
                elif 'close command prompt' in self.query:
                    speak('okay sir closing cmd')
                    os.system('taskkill /f /im cmd.exe')

                elif 'open pycharm' in self.query:
                    speak('Opening pycharm')
                    os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\pycharm\\PyCharm Community Edition 2021.1.2.lnk")

                elif 'close pycharm' in self.query:
                    speak('closing pycharm')
                    os.system('taskkill /f /im pycharm64.exe')
                
                elif 'open camera' in self.query:
                    speak('opening camera')
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k==27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif 'ip address' in self.query:
                    ip = get('http://api.ipify.org').text
                    speak(f"your IP address is {ip}")

                elif 'tell me the news' in self.query:
                    speak('wait sir fetching todays latest news')
                    news()

                elif 'wikipedia' in self.query:
                    speak('searching wikipedia....')
                    query = query.replace("wikipedia" , "")
                    results = wikipedia.summary(query , sentences=2)
                    speak('According to wikipedia...')
                    speak(results)
                    print(results)

                elif 'open youtube' in self.query:
                    webbrowser.open('https://www.youtube.com/')

                elif 'open facebook' in self.query:
                    webbrowser.open('https://www.facebook.com/')

                elif 'open stackoverflow' in self.query:
                    webbrowser.open('https://www.stakoverflow.com/')

                elif 'open school' in self.query:
                    webbrowser.open('hhttps://nlp.nexterp.in/nlp/nlp/v1/student/student-dashboard#//')

                elif 'open google' in self.query:
                    speak('Sir, what should i search on google')
                    cm = self.takeCommand()
                    webbrowser.open(f'https://www.google.com/search?q={cm}')

                elif 'play'in self.query:
                    query = self.query.replace("play","")
                    speak(f"playing {query}")
                    kit.playonyt(query)

                elif 'switch the window' in self.query:
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.keyUp('alt')

                elif 'email' in self.query:
                    speak('sir what should i say')
                    self.query = self.takeCommand()
                    try:
                        if 'send a file' in self.query:
                            email = 'manurajthyparambil@gmail.com'
                            password = 'Next@123'
                            send_to_email = 'manurajthyparambil@gmail.com'
                            speak('okay sir, what is the subject of this email?')
                            self.query = self.takeCommand()
                            subject = self.query
                            speak('and sir, what is the message for this email')
                            self.query2 = self.takeCommand()
                            message = self.query2
                            speak('sir please enter the correct file path into the  shell ')
                            file_location = input('please enter file path')

                            speak('please wait sir. I am sending email now')
                            speak('processing email')
                            speak('encodind file .. decoding process going on please corperate')

                            msg = MIMEMultipart()
                            msg['From']= email
                            msg['To'] = send_to_email
                            msg['Subject'] = subject

                            msg.attach(MIMEText(message, 'plain'))

                            filename = os.path.basename(file_location)
                            attacment = open(file_location, "rb")
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attacment.read())
                            encoders.encode_base64(part)
                            part.add_header("Content-Disposition", "attacment; filename= %s" % filename)

                            msg.attach(part)

                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(email, password)
                            text = msg.as_string()
                            server.sendmail(email, send_to_email, text)
                            server.quit()
                            speak('sir email has benn sent to recipient')

                        else:
                            email = 'manurajthyparambil@gmail.com'
                            password = 'Next@123'
                            send_to_email = 'manurajthyparambil@gmail.com'
                            message = self.query

                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(email, password)
                            server.sendmail(email, send_to_email, message)
                            server.quit()
                            speak('sir email has benn sent to recipient')
                    
                    except Exception as e:
                        print(e)
                        speak('sir i am not able to send email')

                elif 'temperature' in self.query:
                    search = "Temperature in Kerala"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_="BNeawe").text
                    speak(f'current{search} is {temp}')

                elif 'set alarm' in self.query:        
                    speak('work going on')

                elif 'tell me joke' in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif 'shutdown the system' in self.query:
                    os.system('shutdown /s /t 5')

                elif 'restart the system' in self.query:
                    os.system('shutdown /r /t 5')

                elif 'where am i' in self.query or 'where are we' in self.query :
                    speak('wait sir, let me check')    
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    url = "https://get.geojs.io/v1/ip/geo/"+ip+".json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    print(city,country)
                    speak(f"sir i think we are in {city} in {country} country")
                        

                elif 'take screenshot' in self.query or 'take a screenshot' in self.query:
                    speak('sir please tell me the name for the screenshot file')
                    name = takeCommand().lower()
                    speak('sir please hold the screen for few second i am taking a screenshot')
                    time.sleep(3)
                    img = pyautogui.screenshot()
                    img.save(f'{name}.png')
                    speak('i am done sir , i have automatically saved the screenshot in the folder')                    


                elif 'you can sleep'in self.query:
                    speak("okay sir i am going to sleep now, you can call me any time")
                    break

                elif 'goodbye' in self.query:
                    speak('thanks for using me sir have a nice day')
                    sys.exit()

                elif 'read the python pdf' in self.query:
                    pdf_reader()

                elif 'show stock market details' in self.query:
                    kit.playonyt('https://youtu.be/Kxwrqig5UV4')

                elif 'do some calculations' in self.query:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak('sir what should i calculate. for example 3 plus 3')
                        print('listening.....')
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string=r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):
                        return {
                            '+': operator.add,
                            '-': operator.sub,
                            '*': operator.mul,
                            '/':operator.__truediv__,
                        }[op]
                    def eval_binary_expr(op1,oper,op2):
                        op1,op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak('sir your result is')
                    speak(eval_binary_expr(*(my_string.split())))

                elif 'thank you' in self.query:
                    speak('Great pleasure sir')

                elif 'hide my files' in self.query or 'make them visible' in self.query:
                    speak("sir should i hide these files or make then visible")
                    condition = self.takeCommand()
                    if 'hide' in condition:
                        speak('yes sir all these files are being hidden please wait')
                        os.system('attrib +h /s /d')

                    elif 'visible' in condition:
                        speak('now all files will be visible in few seconds. I wish that you ar doing it in your own peace')
                        os.system('attrib -h /s /d')

                    elif 'leave it' in condition or 'leaveit for now' in condition:
                        speak('Ok sir')

                elif 'activate how to mod' in self.query:
                    # from pywikihow import search_wikihow
                    speak('how to do mod is activated.')
                    while True:
                        speak('please tell me what should i search')
                        how = self.takeCommand()
                        try:
                            if 'exit' in how or 'close' in how:
                                speak('how to do mod is closed')
                                break
                            else:
                                max_result = 1
                                how_to = search_wikihow(how, max_result)
                                assert len(how_to) == 1
                                how_to[0].print()
                                speak(how_to[0].summary)
                        except Exception as e:
                            speak('sorry sir i am not able to find it')

                elif 'show battery percentage' in self.query:
                    battery = psutil.sensors_battery()
                    persentage = battery.percent
                    speak(f'sir the computer have {persentage} percentage battery')
                    if persentage>= 75:
                        speak('sir we have enough battrey power to continue ourwork')
                    elif persentage>=40 and persentage<=75:
                        speak('Please connect to charging point')
                    elif persentage>=15 and persentage<=35:
                        speak('we dont have enough battery to continue')
                    elif persentage<15:
                        speak('sir connect to charger as fast as possible. the system will shut down soon')
                
                elif 'internet speed' in self.query:
                    speak('wait sir checking internet speed it will take a while almost 10 seconds')
                    st = speedtest.Speedtest()
                    dl = st.download()
                    ul = st.upload()
                    speak(f'sir we have {dl} bit per secon downloading speed and {ul} bit per second uploading speed')
                
                elif 'send message' in self.query:
                    speak('sir what is the message to be sent')
                    msz = self.takeCommand()


                    from twilio.rest import Client


                    account_sid = 'AC51a09880743913718945eaffdec3ba66'
                    auth_token = '415f4354ac928fbe71c2dd6779df2574'
                    client = Client(account_sid, auth_token)

                    message = client.messages \
                        .create(
                            body=msz,
                            from_='+12242528286',
                            to='+919544369296'
                        )

                    print(message.sid)
                    speak('sir the message has been sent')

                elif 'make a phone call' in self.query:
                        speak('sir what is the message to be sent')
                        msz = self.takeCommand()


                        from twilio.rest import Client


                        account_sid = 'AC51a09880743913718945eaffdec3ba66'
                        auth_token = '415f4354ac928fbe71c2dd6779df2574'
                        client = Client(account_sid, auth_token)

                        message = client.calls \
                            .create(
                                twiml=msz,
                                from_='+12242528286',
                                to='+919544369296'
                            )

                        print(message.sid)
                        speak('sir the message has been sent')

                elif 'volume up' in self.query:
                    pyautogui.press("volumeup")

                elif 'volume down' in self.query:
                    pyautogui.press("volumedown")   
                
                elif 'volume mute' in self.query:
                    pyautogui.press("volumemute")



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../jarvis/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../jarvis/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_Time = QTime.currentTime()
        current_Date = QDate.currentDate()
        label_time = current_Time.toString("hh:mm:ss")
        label_date = current_Date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
    
    def showindic(self):
        indic = MainThread.takeCommand()
        self.ui.textBrowser_3.setText(indic)
    

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())