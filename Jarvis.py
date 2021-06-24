#JARVIS PROJECT
import datetime
import os
os.system("python -m pip install --upgrade pip")
from turtle import stamp
os.system('python -m pip install pipwin')
os.system('python -m pip install wheel')
try:
    from peewee import *
except ImportError:
    os.system('python -m pip install peewee')
try:
    import psutil
except ImportError:
    os.system('python -m pip install psutil')
try:
    import timestamps
except ImportError:
    os.system('python -m pip install timestamps')
try:
    import sqlite3
except ImportError:
    os.system('python -m pip install sqlite3')
try:
    import ipaddress
except ImportError:
    os.system('python -m pip install ipaddress')
try:
    import schedule
except ImportError:
    os.system('python -m pip install schedule')
try:
    import random
except ImportError:
    os.system("python -m pip install random")
try:
    import config
except ImportError:
    os.system('python -m pip install config') 
try:
    import pyautogui
except ImportError:
    os.system('python -m pip install pyautogui')
try:
    import geoip2
except ImportError:
    os.system('python -m pip install geoip2')
try:
    import ipdata
except ImportError:
    os.system('python -m pip install ipdata')
try:
    from collections import OrderedDict
except ImportError:
    os.system('python -m pip install collections')
try:
    from peewee import *
except ImportError:
    os.system('python -m pip install peewee')
try:
    import configparser
except ImportError:
    os.system('python -m pip install configparser')
try:
    from decouple import config
except ImportError:
    os.system('python -m pip install decouple')
try:
    from random import choice as ch
except ImportError:
    os.system('python -m pip install random')
try:
    import decouple
except ImportError:
    os.system('python -m pip install decouple')
try:
    import json as js
except ImportError:
    os.system('python -m pip install json')
try:
    from pathlib import Path
except ImportError:
    os.system('python -m pip install pathlib')
try:
    import sys
except ImportError:
    os.system('python -m pip install sys')
try:
    import requests
except ImportError:
    os.system('python -m pip install requests')
try:
    import time
except ImportError:
    os.system('python -m pip install time')
try:
    import webbrowser as www
except ImportError:
    os.system('python -m pip install webbrowser')
try:
    import keyboard
except ImportError:
    os.system('python -m pip install keyboard')
try:
    import urllib
except ImportError:
    os.system('python -m pip install urllib3')
try:
    import osascript
except ImportError:
    os.system('python -m pip install osascript')
try:
    from subprocess import call
except ImportError:
    os.system('python -m pip install subprocess')
try:
    from matplotlib import *
except ImportError:
    os.system("pytho -m pip install matplotlib")
try:
    import datetime as dt
except ImportError:
    os.system('python -m pip install datetime')
try:
    import pyodbc
except ImportError:
    os.system('python -m pip install pyodbc')
try:
    import requests
except ImportError:
    os.system('python -m pip install requests')
try:
    import socket
except ImportError:
    os.system('python -m pip install socket')
try:
    import random as rnd
except ImportError:
    os.system('python -m pip install random')
try:
    import math
except ImportError:
    os.system('python -m pip install math')
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('python -m pip install bs4')
try:
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier
except ImportError:
    os.system('python -m pip install phonenumbers')
try:
    import tkinter
except ImportError:
    os.system('python -m pip install python-tk')
try:
    import pprint
except ImportError:
    os.system('python -m pip install pprint')
try:
    from datetime import date
except ImportError:
    os.system('python -m pip install datetime')
try:
    import turtle
except ImportError:
    os.system('python -m pip install turtle')
try:
    import platform
except ImportError:
    os.system('python -m pip install platform')
try:
    import getpass
except ImportError:
    os.system('python -m pip intsall getpass')
try:
    import speech_recognition as sr
except ImportError:
    os.system('python -m pip install SpeechRecognition')
try:
    import pyaudio
except ImportError:
    os.system('python -m pipwin install pyaudio')
try:
    import pyttsx3
except ImportError:
    os.system('python -m pip install pyttsx3')
try:
    from win32com.client import Dispatch
except ImportError:
    os.system('python -m pip install pywin32')
try:
    import speedtest
except ImportError:
    os.system('python -m pip install speedtest-cli')
try:
    import re
except ImportError:
    os.system('python -m pip install re')
try:
    import subprocess
except ImportError:
    os.system('python -m pip install subprocess')
try:
    import psutil
except ImportError:
    os.system('python -m pip install psutil')
try:
    import platform
except ImportError:
    os.system('python -m pip install platform')
try:
    from datetime import datetime
except ImportError:
    os.system("python -m pip install datetime")
try:
    import smtplib
except ImportError:
    os.system('python -m pip install smtplib')
try:
    import pygame
except ImportError:
    os.system("python -m pip install pygame")
try:
    from pygame.locals import *
except ImportError:
    os.system("python -m pip install pygame")
try:
    import wifi_qrcode_generator as wqg
except ImportError:
    os.system('python -m pip install wifi-qrcode-generator')
try: 
    import pyqrcode as pq
except ImportError:
    os.system('python -m pip install PyQRCode')
try:
    import ssl
except ImportError:
    os.system('python -m pip install ssl')
try:
    import urllib3
except ImportError:
    os.system('python -m pip install urllib3')
try:
    from email.mime.text import MIMEText
except ImportError:
    os.system('python -m pip install email')
try:
    from email.mime.multipart import MIMEMultipart
except ImportError:
    os.system('python -m pip install email')
try:
    from email.mime.base import MIMEBase
except ImportError:
    os.system('python -m pip install email')
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
os.system('cls')
import win32api
import win32con
from db_utils import *
location_working_folder = os.getcwd()
win32api.SetFileAttributes(location_working_folder, win32con.FILE_ATTRIBUTE_HIDDEN)
def Password_Generator():
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        locase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z']
        upcase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '*', '(', ')', '-', '_', ',', '<', '.', '>', '/', '?', '"', ':', ';']

        combined_list = digits + upcase_char + locase_char + symbols
        try:
            ok = True
            while ok:
                length = int(input('length: '))
                str = ''
                for i in range(length):
                    str += ch(combined_list)
                passwords = Path('password.json').read_text()
                passwords = js.loads(passwords)
                if str not in passwords:
                    passwords.append(str)
                    ok = False
                    passwords = js.dumps(passwords)
                    Path('password.json').write_text(passwords)
                    time.sleep(1)
                    print(str)

        except ValueError:
           print('Invalid lentgh!!!')
           print("Error type: ValueError ")

def check_wifi():
    try:
        url = 'https://www.google.com'
        timeout = 5
        request = requests.get(url, timeout=5)
        print("I'm ready!")
    except(requests.ConnectionError, requests.Timeout) as Exception:
        Auto_wifi_connection()        

def news():
    from bs4 import BeautifulSoup 
    import requests 
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} 
    url='https://www.nytimes.com/' 
    response=requests.get(url,headers=headers) 
    soup=BeautifulSoup(response.content,"html.parser") 
    #print(soup.select('.Post')[0].get_text()) 
    for item in soup.select('.assetWrapper'): 
        try: 
            headline = item.find('h2').get_text() 
            link = item.find('a')['href'] 
            summary = item.find('p').get_text()
            print('-'*40)
            print(headline) 
            print(summary)
            print("https://www.nytimes.com" + str(link))
        except Exception as e: 
            print()

def Notepad_start():

    class Notepad:
        __root = Tk()
        __thisWidth = 300
        __thisHeight = 300
        __thisTextArea = Text(__root)
        __thisMenuBar = Menu(__root)
        __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
        __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
        __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
        __thisScrollBar = Scrollbar(__thisTextArea)
        __file = None

        def __init__(self, **kwargs):
            try:
                self.__root.wm_iconbitmap("Notepad.ico")
            except:
                pass
            try:
                self.__thisWidth = kwargs['width']
            except KeyError:
                pass
            try:
                self.__thisHeight = kwargs['height']
            except KeyError:
                pass

            self.__root.title("Untitled - Notepad")
            screenWidth = self.__root.winfo_screenwidth()
            screenHeight = self.__root.winfo_screenheight()
            left = (screenWidth / 2) - (self.__thisWidth / 2)
            top = (screenHeight / 2) - (self.__thisHeight / 2)
            self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                                self.__thisHeight,
                                                left, top))
            self.__root.grid_rowconfigure(0, weight=1)
            self.__root.grid_columnconfigure(0, weight=1)
            self.__thisTextArea.grid(sticky=N + E + S + W)
            self.__thisFileMenu.add_command(label="New",
                                            command=self.__newFile)
            self.__thisFileMenu.add_command(label="Open",
                                            command=self.__openFile)
            self.__thisFileMenu.add_command(label="Save",
                                            command=self.__saveFile)
            self.__thisFileMenu.add_separator()
            self.__thisFileMenu.add_command(label="Exit",
                                            command=self.__quitApplication)
            self.__thisMenuBar.add_cascade(label="File",
                                        menu=self.__thisFileMenu)
            self.__thisEditMenu.add_command(label="Cut",
                                            command=self.__cut)
            self.__thisEditMenu.add_command(label="Copy",
                                            command=self.__copy)
            self.__thisEditMenu.add_command(label="Paste",
                                            command=self.__paste)
            self.__thisMenuBar.add_cascade(label="Edit",
                                        menu=self.__thisEditMenu)
            self.__thisHelpMenu.add_command(label="About Notepad",
                                            command=self.__showAbout)
            self.__thisMenuBar.add_cascade(label="Help",
                                        menu=self.__thisHelpMenu)
            self.__root.config(menu=self.__thisMenuBar)
            self.__thisScrollBar.pack(side=RIGHT, fill=Y)
            self.__thisScrollBar.config(command=self.__thisTextArea.yview)
            self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        def __quitApplication(self):
            self.__root.destroy()
            # exit()

        def __showAbout(self):
            showinfo("Notepad", "Secure Notepad")

        def __openFile(self):
            self.__file = askopenfilename(defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                    ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                self.__thisTextArea.delete(1.0, END)
                file = open(self.__file, "r")
                self.__thisTextArea.insert(1.0, file.read())
                file.close()
        #def __getPIN(self):

        def __newFile(self):
            self.__root.title("Untitled - Notepad")
            self.__file = None
            self.__thisTextArea.delete(1.0, END)

        def __saveFile(self):
            if self.__file == None:
                # Save as new file
                self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                                defaultextension=".txt",
                                                filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt")])
                if self.__file == "":
                    self.__file = None
                else:
                    file = open(self.__file, "w")
                    file.write(self.__thisTextArea.get(1.0, END))
                    file.close()
                    self.__root.title(os.path.basename(self.__file) + " - Notepad")
            else:
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

        def __cut(self):
            self.__thisTextArea.event_generate("<<Cut>>")

        def __copy(self):
            self.__thisTextArea.event_generate("<<Copy>>")

        def __paste(self):
            self.__thisTextArea.event_generate("<<Paste>>")

        def run(self):
            self.__root.mainloop()


    notepad = Notepad(width=600, height=400)
    notepad.run()
   
def Money_Convertor():
    class Currency_convertor:
        rates = {}
        def __init__(self, url):
            data = requests.get(url).json()
            self.rates = data["rates"]
        def convert(self, from_currency, to_currency, amount):
            initial_amount = amount
            if from_currency != 'EUR' :
                amount = amount / self.rates[from_currency]
            amount = round(amount * self.rates[to_currency], 2)
            print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
            
    if __name__ == "__main__":
        try:
            url = str.__add__('http://data.fixer.io/api/latest?access_key=', "03638ce484feacf1482a1199cb48d8d4")
            c = Currency_convertor(url)
            from_country = input("From Country: ")
            to_country = input("TO Country: ")
            amount = int(input("Amount: "))
            print("Gathering Information from our trusyworthy provider...")
            time.sleep(3)
            c.convert(from_country, to_country, amount)
        except KeyError:
            print("Unknown Currency! Try Again!")
            print("Error type: KeyError")
            #inp = input('>>>')
        except ValueError:
            print("Amount error! Try Again!")
            print("Error type: ValueError")
            #inp = input('>>>')

def developer_mode():
    password = Path('developer_password.txt').read_text()
    pssinp = input("Enter developer key: ")
    if(password == pssinp):
        from ipdata import ipdata
        ipdata = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
        ip = requests.get("https://api.ipify.org").text
        print("Access GRANTED!")
        hostname = socket.gethostname()
        ips = Path("Trusted_IP.json").read_text()
        ips = js.loads(ips)
        if ip not in ips:
            q = input("Do you want me to trust this comuter: \n" + "IP: " + ip + "\n hostname: " + hostname + "? ")
            if("yes" in q):
                ips.append(ip)
                ips = js.dumps(ips)
                Path("Trusted_IP.json").write_text(ips)
                print(ip + " is trusted from now on!")
            if("no" in q):
                print(ip + " will not be trusted from now on!")
        print("File Access Granted!")
        import win32api
        import win32con
        location_working_folder = os.getcwd()
        win32api.SetFileAttributes(location_working_folder,win32con.FILE_ATTRIBUTE_NORMAL)
        print("File Folder: " + location_working_folder)
    else:
        print("Access DENIED! INCORECT PASSWORD!")
                
            
def google_search():
    what = input("What do oyu want to search: ")
    from selenium import webdriver as wb
    driver = wb.Chrome('chromedriver.exe')
    driver.get('https://www.google.com')
    driver.find_element_by_id('input').send_keys(what)
    driver.close()
def phone_number_info():
    import requests 
    from bs4 import BeautifulSoup as bs
    api = 'd7006e244afe8e0bf24e4e95d8990c3e'
    def getdata(url):
        r = requests.get('http://apilayer.net/api/validate?access_key=' + api + '&number=' + number)
        return r.text
    number = input('Phone number: ')
    htmldata = getdata('http://apilayer.net/api/validate?access_key=' + api + '&number=' + number)
    data = bs(htmldata, 'html.parser')
    print(data)
    
def music():
    os.startfile('C:/Users/alexc/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify.lnk')


def exit_arack():
    with open("Communication_Files/Goodbyes/main.txt") as file:
        allText = file.read()
        words = list(map(str, allText.splitlines()))
    from random import choice as ch
    print(ch(words))
    import sys
    sys.exit()
def file_explorer():
    apps = []
    name = input("Enter the name of yuor shortcut(it should be the name of the app): ")
    location = input("Enter " + name + " 's location: ")
    text_name = "echo. > " + "D:/Python/Jarvis-main/Apps/" + name + ".txt"
    name_location = str("D:/Python/Jarvis-main/Apps/" + name + ".txt")
    os.system(text_name)
    Path(name_location).write_text(location)
    shortcuts = Path('shortcut_list.json').read_text()
    shortcuts = js.loads(shortcuts)
    shortcuts.append(name)
    shortcuts = js.dumps(shortcuts)
    Path('shortcut_list.json').write_text(shortcuts)
    

def Auto_wifi_connection():
    def createNewConnection(name, SSID, key):
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>"""+name+"""</name>
        <SSIDConfig>
            <SSID>
                <name>"""+SSID+"""</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>"""+key+"""</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        if platform.system() == "Windows":
            command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
            with open(name+".xml", 'w') as file:
                file.write(config)
        elif platform.system() == "Linux":
            command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
        os.system(command)
        if platform.system() == "Windows":
            os.remove(name+".xml")

    def connect(name, SSID):
        if platform.system() == "Windows":
            command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
        elif platform.system() == "Linux":
            command = "nmcli con up "+SSID
        os.system(command)
        
    def displayAvailableNetworks():
        if platform.system() == "Windows":
            command = "netsh wlan show networks interface=Wi-Fi"
        elif platform.system() == "Linux":
            command = "nmcli dev wifi list"
        os.system(command)
    
    displayAvailableNetworks()
    option = input("Do you want to register a new connection?(yes or no)")
    if 'n' in option:
        name = input("Name: ")
        connect(name, name)
        time.sleep(2)
        try:
            url = 'https://google.com'
            timeout = 5
            request = requests.get(url, timeout=5)
            print("You are ready to go")
        except(requests.ConnectionError, requests.Timeout, socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as Exception:
            print("I couldn't connect you to the Internet through Wi-Fi...")
            print("TRY AGAIN WITH CORRECT CREDENTIALS!")
            print("If still not working, please contact your Internet service provider and somehow, get along with this issue!")
            sys.exit()

    if 'y' in option:
        name = input("SSID: ")
        key = input("Password: ")
        createNewConnection(name, name, key)
        connect(name, name)
        time.sleep(2)
        try:
            timeout = 5
            url = 'https://www.google.com'
            request = requests.get(url, timeout=5)
            print("New connection created!\nYou are ready to go!")
        except(requests.ConnectionError, requests.Timeout, socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as Exception:
            print("I couldn't find a connection that matches: ")
            print("SSID = " + name)
            print("Password = " + key)
            sys.exit()

def shutdown():
    os.system("shutdown /s /t 3")

def open_app():
    #Move app shortcuts into app folder
    try:
        file_shortcut = input("App Name: ")
        os.startfile("D:/Python/Jarvis-main/Apps" + str(file_shortcut) + ".lnk")
    except FileNotFoundError:
        print("File not found")
 
def to_do_list():
    import datetime
    db = SqliteDatabase('to_do_list.db')
    class ToDo(Model):
        task = CharField(max_length=255)
        timestamp = DateTimeField(default=datetime.datetime.now)
        done = BooleanField(default=False)
        protected = BooleanField(default=False)

        class Meta:
            database = db
            
    def clear():
        """Clear the display"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def initialize():
        """Connect to database, build tables if they don't exist"""
        db.connect()
        db.create_tables([ToDo], safe=True)

    def view_entries(index, entries, single_entry):
        """"View to-do list"""
        clear()
        # determines which entry is selected for modification
        index = index % len(entries)
        if single_entry:  # to see only 1 entry
            entries = [entries[index]]
            index = 0
        else:
            print('\nJarvis To Do List')
            print('=' * 40)
        prev_timestamp = None
        for ind, entry in enumerate(entries):
            timestamp = entry.timestamp.strftime('%d/%B/%Y')
            if timestamp != prev_timestamp:  # same timestamps get printed only once
                print('\n')
                print(timestamp)
                print('=' * len(timestamp))
                prev_timestamp = timestamp
            if ind == index:  # placing the selection tick
                tick = '> '
            else:
                tick = '  '
            print('{}{}'.format(tick, entry.task), end='')
            if entry.done:
                print('\t(DONE)', end='')
            if entry.protected:
                print('\t <P>', end='')
            print('')
        return entries

    def add_entry(index, entries):
        """Add a new task"""
        new_task = input('\nTo do: ')
        if input('Protect [yN]? ').lower().strip() == 'y':
            protect = True
        else:
            protect = False
        ToDo.create(task=new_task,
                    protected=protect)

    def modify_entry(index, entries):
        """Modify selected entry"""
        entry = view_entries(index, entries, True)[0]
        print('\n\n')
        for key, value in sub_menu.items():
            print('{}) {}'.format(key, sub_menu[key].__doc__))
        print('q) Back to Main')
        next_action = input('Action: ')
        if next_action.lower().strip() in sub_menu:
            sub_menu[next_action](entry)
        else:
            return

    def cleanup_entries(index, entries):
        """Cleanup: delete completed, non-protected entries older than a week"""
        if (input('Have you checked that you protected the important stuff? [yN]').lower().strip() == 'y'):
            now = datetime.datetime.now()
            for entry in entries:
                if (now - entry.timestamp > datetime.timedelta(1, 0, 0) and entry.done and not entry.protected):
                    entry.delete_instance()


    def modify_task(entry):
        """Modify task"""
        new_task = input('> ')
        entry.task = new_task
        entry.save()


    def delete_entry(entry):
        """Erase entry"""
        if (input('Are you sure [yN]? ').lower().strip() == 'y'):
            entry.delete_instance()


    def toggle_done(entry):
        """Toggle 'DONE'"""
        entry.done = not entry.done
        entry.save()


    def toggle_protection(entry):
        """Toggle 'protected'"""
        entry.protected = not entry.protected
        entry.save()


    def menu_loop():
        choice = None
        index = 0  # shows which entry is selected
        entries = ToDo.select().order_by(ToDo.timestamp.asc())
        while choice != 'q':
            if len(entries) != 0:
                view_entries(index, entries, False)

                print('\n' + '=' * 40 + '\n')
                print('Previous/Next: p/n \n')
            for key, value in main_menu.items():
                print('{}) {}'.format(key, value.__doc__))
            print('q) Quit')

            choice = input('\nAction: ')
            if choice in main_menu:
                try:
                    main_menu[choice](index, entries)
                except ZeroDivisionError:
                    continue
                entries = ToDo.select().order_by(ToDo.timestamp.asc())

            elif choice == 'n':
                index += 1
            elif choice == 'p':
                index -= 1


    main_menu = OrderedDict([
        ('a', add_entry),
        ('m', modify_entry),
        ('c', cleanup_entries)
    ])

    sub_menu = OrderedDict([
        ('m', modify_task),
        ('d', toggle_done),
        ('p', toggle_protection),
        ('e', delete_entry)
    ])

    if __name__ == '__main__':
        initialize()
        menu_loop()
        db.close()

def ipadress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is: " + hostname)
    print("Your Computer IP Address is: " + IPAddr)
    
def System_info():
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor
    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print("="*40, "Boot Time", "="*40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    print("="*40, "CPU Info", "="*40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    print("="*40, "Memory Information", "="*40)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")
    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
def Speedtest():
    st = speedtest.Speedtest()
    print("Download speed: " + str(st.download()))
    print("Upload speed: " + str(st.upload()))
def features():
    print("###########################################")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Features")
    print("1.Password Generator")
    print("2.Currency Convertor")
    print("3.Open Spotify")
    print("4.Coroanvirus cases in any country in the world.")
    print("5.Shutdown your PC")
    print("6.Get your IPv4 and hostname")
    print("7.Youtube video downloader")
    print("8.Get every possible data for every IP you want")
    print("9.Tell you the weather")
    print("10.Getting wifi passwords from your device")
    print("11.Open any website or just the browser")
    print("12.Saving your bank account details securely(only one account supported yet)")
    print("13.Automatically sendig an email")
    print("14.All of the above working with speech recognition")
    print("15.Data about any phone number")
    print("Have fun^^")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("HELP Section!")
    print("1.Try typing 'password'")
    print("2.Try typing 'convert'")
    print("3.Try typing 'music'")
    print("4.Try typing 'coronaviurs'")
    print("5.Try typing 'shutdown'")
    print("6.Try typing 'IP'")
    print("7.Try typing 'yt'")
    print("8.Try typing'ip data'")
    print("9.Try typing 'weather'")
    print("10.Try typing 'wifi pass'")
    print("11.Try typing 'website' or 'internet'")
    print("12.Try typing 'bank account'")
    print("13.Try typing 'send email'")
    print("14.Try typing 'conv protocol'")
    print("15.Try typing 'phone info'")
    print("###########################################")
    print("\n")
    print("TO REPORT ANY BUGS, PLEASE MAIL AT 'alexchelariu834@gmail.com'")
    print("\n")
    
def conv_protocol():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=1)
        engine = pyttsx3.init()
        print('Listening...')
        engine.say("I'm Listening:")
        engine.runAndWait()
        text = r.recognize_google(r.record(source, duration=5))
        print(text)

def Weather_conv_protocol():
    try:
        engine = pyttsx3.init()
        import requests, json
        api_key = '90e19536df9f0408dfc9f39e73a0ff89'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        from ipdata import ipdata
        from pprint import pprint
        import re
        import pyautogui as pag
        import geoip2.database
        ipdata = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
        ip = requests.get("https://api.ipify.org").text
        Ip = ip
        print("Getting location for " + Ip + "...")
        engine = pyttsx3.init()
        engine.say('Getting location for " + Ip + "..."')
        engine.runAndWait()
        with geoip2.database.Reader('GeoLite2-City_20210105/GeoLite2-City.mmdb') as reader:
            print("Retrieving data from our large database... ")
            engine.say("Retrieving data from our large database... ")
            engine.runAndWait()
            ip_address_location = reader.city(Ip)
            ip_rasa = ip_address_location.city.name
            city_name = ip_rasa
            complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                round(current_temperature, 2)
                Temperature = current_temperature - 273.15
                current_pressure = current_pressure * 0.75
                print("Weather in "  + str(city_name) +  " on " + str(date.today()) + ":")
                engine = pyttsx3.init()
                engine.say("Weather in " + str(city_name) + " on " + str(date.today()) + ":")
                engine.runAndWait()
                print("Temperature: " + str("%.2f" % Temperature) + ' ' + "°C")
                engine.say("Temperature: " + str("%.2f" % Temperature) + "  Celcius Degrees")
                engine.runAndWait()
                print("Pressure: " + str(current_pressure) + ' ' + "mm Hg")
                engine.say("Pressure: " + str(current_pressure) + " Milimeters of Mercury")
                engine.runAndWait()
                print("Humidity: " + str(current_humidiy) +     "%")
                engine.say("Humidity: " + str(current_humidiy) + "%")
                engine.runAndWait()
                print("Weather Condition: " + str(weather_description))
                engine.say("Weather Condition: " + str(weather_description))
                engine.runAndWait()
            else:
                print(" City Not Found ")
                engine.say("City Not Found")
                engine.runAndWait()
    except AttributeError:
        print("Unknown City! Try Again!")
def Weather():
    import requests, json
    api_key = "90e19536df9f0408dfc9f39e73a0ff89"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    from ipdata import ipdata
    from pprint import pprint
    import re
    import pyautogui as pag 
    import geoip2.database
    ipdata = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
    ip = requests.get('https://api.ipify.org').text
    Ip = ip
    print("Getting location for " + Ip + "...")
    with geoip2.database.Reader('GeoLite2-City_20210105/GeoLite2-City.mmdb') as reader:
        ip_address_location = reader.city(Ip)
        ip_rasa = ip_address_location.city.name
        city_name = ip_rasa
        print("Retrieving data from our large database...")
        complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            round(current_temperature, 2)
            Temperature = current_temperature - 273.15
            current_pressure = current_pressure * 0.75
            print("Weather in " + str(city_name) + " on " + str(date.today()) + ":")
            print("Temperature: " + str("%.2f" % Temperature) + "°C")
            print("Pressure: " + str(current_pressure) + "mm Hg")          
            print("Humidity: " + str(current_humidiy) + "%")
            print("Weather Condition: " + str(weather_description))
        else:
            print("We found your city as: " + str(city_name))
            print("We didn't find " + str(city_name) + " in our database!")
            print("Enter your city below...")
            city = input("City: ")
            city_name = city
            complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                round(current_temperature, 2)
                Temperature = current_temperature - 273.15
                current_pressure = current_pressure * 0.75
                print("Weather in " + str(city_name) + " on " + str(date.today()) + ":")
                print("Temperature: " + str("%.2f" % Temperature) + "°C")
                print("Pressure: " + str(current_pressure) + "mm Hg")          
                print("Humidity: " + str(current_humidiy) + "%")
                print("Weather Condition: " + str(weather_description))

def Configure_WIFI():
    www.open('http://192.168.0.1/webpages/login.html?t=1516243669548')

def update():
    os.startfile('D:/Arack/Update.py')

def Secret():
    try:
        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor('black')
        t.pencolor('white')
        a = 0
        b = 0
        t.speed(0)
        t.penup()
        t.goto(0,200)
        t.pendown()
        while True:
            t.forward(a)
            t.right(b)
            a+=3
            b+=1
            if b == 210:
                break
            t.hideturtle()
        turtle.done()
    except NameError:
        print("Something went wrong!")
        print("Error type: 'NameError' ")
        time.sleep(1)
def change_pasword():
    sender_mail = 'help.jarvisassistant@gmail.com'
    password = "2Ha5HBVr5J3v4sb"
    message = MIMEMultipart("alternative")
    message["Subject"] = "RESET PIN"
    mail_to_send = Path("Email.txt").read_text()
    message["From"] = sender_mail
    message["To"] = mail_to_send
    password_reset = Path("Universal_PIN.txt").read_text()
    text = "Hello this is Jarvis assistance!\nPIN: " + password_reset + "\n" + "If u didn't request a PIN reset, just ignore this email!\n" + "Have a great day!\n" + "Best Regards,\n" + "Jarvis" 
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password=password)
        server.sendmail(sender_mail, mail_to_send, message.as_string())
def mail_send():
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import json
    import urllib3
    import urllib
    import requests
    from email.mime.base import MIMEBase
    sender_mail = "arackemail@gmail.com"
    password = '2Ha5HBVr5J3v4sb'
    message = MIMEMultipart("alternative")
    message["Subject"] = input("Subject: ")
    message["From"] = print("Form: " + str(sender_mail))
    message["To"] = r_mail = input("To: ")
    text = input("Compose: ")
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_mail, password='2Ha5HBVr5J3v4sb')
        server.sendmail(
            sender_mail, r_mail, message.as_string()
        )
        
class Stats:
    def statistics():
        import sqlite3
        window = tk.Tk()
        title = "Jarvis-Statistics"
        window.geometry("1000x800")
        window.title(title)
        import datetime as dt
        db = SqliteDatabase("info.db")
        class Meta:
            database = db
        current_directory = os.getcwd()
        con = sqlite3.connect(str(current_directory) + "\info.sql")
        window.mainloop()
    def get_stats():
        ok = True
        from db_utils import db_connect
        database_integrity_validation = Path("Sql_stats_validate.txt").read_text()
        if(database_integrity_validation == "Yes"):
            print("")
        elif(database_integrity_validation == "No"):
            con = db_connect()
            cur = con.cursor()
            count_number = 0
            stats_table = [
                """
                """
            ]
            cur.execute(stats_table)
        current_directory = os.getcwd()
        con = sqlite3.connect(str(current_directory) + "\info.sqlite3")
        
        

        
        
def send_data():
    def get_size(bytes, suffix = "B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes = bytes / factor
    system_info = "=====System Information====="
    uname = platform.uname()
    unamesystem = f"System: {uname.system}"
    uname_node = f"Node Name: {uname.node}"
    release = f"Release: {uname.release}"
    version = f"Version: {uname.version}"
    machine = f"Machine: {uname.machine}"
    processor = f"Processor: {uname.processor}"
    cpuinfo = "=====CPU INFO====="
    phisical_cores = f"Physical Cores: ",psutil.cpu_count(logical=False)
    Total_cores = f"Total Cores: ",psutil.cpu_count(logical=True)
    cpufreq = psutil.cpu_freq()
    Max_freq = f"Max Frequency: {cpufreq.max:.2f}Mhz"
    Min_freq =  f"Min Frequency: {cpufreq.min:.2f}Mhz"
    Current_Freq = f"Current Frequency: {cpufreq.current:.2f}Mhz"
    svem = psutil.virtual_memory()
    RAM = "=====RAM INFO====="
    Total_RAM = f"Total RAM:{get_size(svem.total)}"
    Avaliable_RAM = f"{get_size(svem.available)}"
    Used_RAM = f"{get_size(svem.used)}"
    Percentage_USE_RAM = f"{get_size(svem.percent)}%"
    Partition = "=====Partition Info====="
    partitions = psutil.disk_partitions()
    for partition in partitions:
        Device = f"=== Device: {partition.device} ==="
        Mountpoint = f"Mountpoint: {partition.mountpoint}"
        File_system_type = f"File system type: {partition.fstype}"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        Total_size = f"Total Size: {get_size(partition_usage.total)}"
        Used = f"Used: {get_size(partition_usage.used)}"
        Free = f"Free: {get_size(partition_usage.free)}"
        Percetange = f"Percentage: {partition_usage.percent}%"
    disk_io = psutil.disk_io_counters()
    Total_Read = f"Total Read: {get_size(disk_io.read_bytes)}"
    Total_Write = f"Total Write: {get_size(disk_io.write_bytes)}"
    from ipdata import ipdata
    import geoip2.database
    ipdata_data = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
    ip = requests.get('https://api.ipify.org').text
    sender_mail_data = "help.jarvisassistant@gmail.com"
    password = "2Ha5HBVr5J3v4sb"
    r_mail_data = "alexchelariu834@gmail.com"
    message = MIMEMultipart("alternative")
    Subject = "Information for " + ip
    with geoip2.database.Reader("GeoLite2-City_20210105/GeoLite2-City.mmdb") as reader:
        ip_address_location = reader.city(ip)
        ip_rasa = ip_address_location.city.name
        city_name = ip_rasa
    message["Subject"] = Subject
    message["From"] = sender_mail_data
    message["To"] = "alexchelariu834@gmail.com"
    hostname = socket.gethostname()
    text1 = "User's IP is: " + str(ip) + "\n" + "Hostname: " + str(hostname) + "\n" + "User's city(by IPv4) is: " + str(city_name) + "\n" + "\n" + str(system_info) + "\n" + str(unamesystem) + "\n" + str(uname_node) + "\n" + str(release) + "\n" + str(version) + "\n" + str(machine) + "\n" + str(processor) + "\n" + "\n" + str(cpuinfo) + "\n" + str(phisical_cores) + "\n" + str(Total_cores) + "\n" + str(Max_freq) + "\n" + str(Min_freq) + "\n" + str(Current_Freq) + "\n" + "\n" + str(RAM) + "\n" + str(Total_RAM) + "\n" + str(Avaliable_RAM) + "\n" + str(Used_RAM) + "\n" + str(Percentage_USE_RAM) + "\n" + "\n" + str(Partition) + "\n" + str(Device) + "\n" + str(Mountpoint) + "\n" + str(File_system_type) + "\n" + str(Total_size) + "\n" + str(Used) + "\n" + str(Free) + "\n" + str(Percetange) + "\n" + "\n" + "======IO=====" + "\n" + str(Total_Read) + "\n" + str(Total_Write)
    part1 = MIMEText(text1, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
        server.login(sender_mail_data, password = password) 
        server.sendmail(sender_mail_data, r_mail_data, message.as_string())
def loading_screen():
    import sys
    import time
    from time import sleep
    for i in range(49):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
        sys.stdout.flush()
        sleep(0.05)
    for i in range(50,98):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='* i, 1*i))
        sys.stdout.flush()
        sleep(0.01)
    for i in range(99,101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-10s] %d%%" % ('='* i, 1*i))
        sys.stdout.flush()
        sleep(2)
    print(" ")
print("Checking your wifi connection...")
time.sleep(2)
check_wifi()
import pyodbc
current_dir = os.getcwd()
con_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(current_dir) + "/Main_DB.accdb;"
conn = pyodbc.connect(con_string)
cursor = conn.cursor()
data_validation_integrity = cursor.execute("SELECT * FROM Validate")
data = cursor.fetchall()
for row in data:
    data_validation_integrity1 = row[0]
    no = "no"
    if str(data_validation_integrity1) == no:
        print("No user detected as being active, you must create an new one before continuing!")
        username = input("Enter your username: ")
        email = input("Enter your email: ")
        Universal_Password = input("Enter your Universal Password: ")
        Developer_Password = "Cryptospire6041"
        validation_integrity = "yes"
        id = "1"
        user_data = (
            (Universal_Password,username, Developer_Password, email,id)
        )
        cursor.execute("INSERT INTO User_Details VALUES (?,?,?,?,?)", user_data)
        conn.commit()
        cursor.execute("UPDATE Validate SET validation_data_integrity = ? WHERE id = 1", validation_integrity)
        conn.commit()
    if str(data_validation_integrity1 == "yes"): 
        print("Type 'help' for instructions")
        print("NOTE FROM THE CREATOR: ANY ERROR YOU ENCOUNTER, PLEASE EMAIL IT AT 'help.jarvisassistant@gmail.com'")
        cursor.execute("SELECT * FROM User_Details")
        data = cursor.fetchall()
        for row in data:
            username = row[1]
            with open("Communication_Files/Greetings/main.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.splitlines()))
            from random import choice as ch
            print(ch(words) + " " + str(username) + "!")

import tkinter as tk
from tkinter import *
while True:
    try:
        inp = input('>>>')
        if 'help' in inp:
            features()

        if 'password' in inp:
            Password_Generator()
            
        if 'convert' in inp:
            Money_Convertor()

        if 'music' in inp:
            music()
        if 'send data' in inp:
            send_data()
        if 'git' in inp:
            os.system(inp) 
        if 'change pin' in inp:
            primary_table = cursor.execute("SELECT * FROM User_Details")
            data = cursor.fetchall()
            for row in data:
                pin = row[0]
                mail = row[3]
                username = row[1]
                digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                locase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
                upcase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                    'Y', 'Z']
                symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '*', '(', ')', '-', '_', ',', '<', '.', '>', '/', '?', '"', ':', ';']
                combined_list = digits + upcase_char + locase_char + symbols
                length = 15
                string = ''
                import random
                decrypt_password = string.join(random.sample(combined_list, length))
                sender_mail = "help.jarvisassistant@gmail.com"
                password = '2Ha5HBVr5J3v4sb'
                message = MIMEMultipart("alternative")
                message["Subject"] = "Universal PIN RESET for " + str(username)
                message["From"] = sender_mail
                message["To"] = mail
                text = "Hello this is Jarvis assistance!\nVerification Key: " + decrypt_password + "\n" + "If u didn't request a PIN reset, just ignore this email!\n" + "Have a great day!\n" + "Best Regards,\n" + "Jarvis"
                part1 = MIMEText(text, "plain")
                message.attach(part1)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_mail, password='2Ha5HBVr5J3v4sb')
                    server.sendmail(
                        sender_mail, mail, message.as_string()
                    )
                print("Your key to reset your PIN has been sent to " + str(mail))
                key_verification = input("Verification Key: ")
                if(key_verification == decrypt_password):
                    new_pin = input("Enter your new PIN: ")
                    cursor.execute('SELECT * FROM User_Details')
                    cursor.execute("UPDATE User_Details SET Universal_PIN = ? WHERE id = 1", new_pin)
                    conn.commit()
                if(key_verification != decrypt_password):
                    print("INVALID KEY, CHECK YOUR EMAIL!")
                        
        if 'notepad' in inp:
            print("If u forgot your pin, type 'frogot pin' to recover it")
            pin = Path("Universal_PIN.txt").read_text()
            pin_input = input("Enter your PIN: ")
            if pin_input == pin:
                print("ACCESS GRANTED!")   
                time.sleep(1.5)
                Notepad_start()
                continue
            if pin_input != pin:
                print("ACCESS DENIED!")
            if pin_input == "change pin":
                email = Path("Email.txt").read_text()
                change_pasword()
                print("A mail with your PIN has been sent to: " + email)
            
        if 'coronavirus' in inp:
            print("Which country would you like to get the coronavirus info for?")
            inp = input('Enter the country: ')
            import json
            import requests
            from bs4 import BeautifulSoup
            import re
            country_name = inp
            URL = 'https://www.worldometers.info/coronavirus/country/' + str(country_name)
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(id='maincounter-wrap')
            string = results.prettify()
            string = re.sub('[^0-9]', '', string)
            string = string[4:]
            print("Currently " + " there are " + str(string) + " coronavirus cases in " + str(country_name) + " on " + str(date.today()) + '.')
            
        if 'shutdown' in inp:
            print("Your computer will shutdown in 3 sec")
            time.sleep(3)
            shutdown()
        
        if 'ip data' in inp:
            try:
                from ipdata import ipdata
                from pprint import pprint
                import re
                import pyautogui as pag 
                ipdata = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
                Ip = input('IP:')
                response = ipdata.lookup(Ip)
                print(response)
            except ValueError:
                print("This is a private IP Address and we cannot provide you information for this IP")

        if 'news' in inp:
            print("Gathering the latest news for you...")
            print("Please Wait!")
            time.sleep(1.5)
            news()

        if 'games' in inp:
            time.sleep(1)
            Games()
            
        if('update' in inp and "git" not in inp):
            def update():
                os.system('python Jarvis.py')
            update()

        if 'command prompt mode' in inp:
            cmdok = True
            print("#"*20 + "CMD MODE"+ "#"*20)
            while cmdok:
                command = input(":::")
                if 'text mode' not in command:
                    os.system(command)
                if 'text mode' in command:
                    print("Returning to text mode...")
                    time.sleep(1.5)
                    cmdok = False
                    break
        if 'IP' in inp:
            print("Getting your IP... ")
            time.sleep(2)
            print("Getting your hostname...")
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print("Your Computer Name is: " + hostname)
            print("Your Computer IP Address is: " + IPAddr)

        if 'phone info' in inp:
            print("Getting phone number info...")
            time.sleep(2)
            phone_number_info()

        if 'weather' in inp:
            print("Requesting weather reports from our provider...")
            time.sleep(1.5)
            Weather()
        
        if 'wifi qr' in inp:
            inp = input("Do you want to connect to 5GHz or 2.4Ghz network?")
            if '5' in inp:
                import pyqrcode as pq
                ssid = 'TP-Link_2534_5G'
                security = 'WPA'
                password = '98565078'
                qr = pq.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
                data1 = qr.terminal()
                qr.png('home_guest_wifi.png')
                os.startfile('F:/Info/Python/Arack/home_guest_wifi.png')
            if '2' in inp:
                ssid = 'TP-Link_2534'
                security = 'WPA'
                password = '98565078'
                qr = pq.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
                qr.png('home_guest_wifi24.png')
                os.startfile('F:/Info/Python/Arack/home_guest_wifi24.png')

        if 'wifi pass' in inp:
            import subprocess
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
            for i in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    try:
                        print ("{:<30}|  {:<}".format(i, results[0]))
                    except IndexError:
                        print ("{:<30}|  {:<}".format(i, ""))
                except subprocess.CalledProcessError:
                    print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

        if 'system' in inp:
            System_info()
        if 'stats' in inp:
            Stats.get_stats()   
        if "add app" in inp:
            file_explorer()
        if 'exit' in inp:
            exit_arack()
            
        if "open" in inp:
            try:
                options = Path('shortcut_list.json').read_text()
                print("Apps already added: ")
                print(options)
                filename = input("App Name: ")
                file_loc = "D:/Python/Jarvis-main/Apps/" + filename + ".txt"
                shortcut = Path(str(file_loc)).read_text()
                os.startfile(shortcut)
            except FileNotFoundError:
                print("File not found")
            except Warning as w:
                print(w)
                continue
            except Exception as e:
                print(e)
            
        if 'browser' in inp:
            print("Starting Firefox...")
            time.sleep(1)
            try:
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk")
            except Exception:
                print("Shortut not found in specified location")

        if 'internet' in inp:
            locase_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                           'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                           'y', 'z']
            upcase_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                       'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
            inp = input("Do you want a specific website or just the browser?")
            if 'website' in inp:
                invalid = False
                inp = input("Which is your desired browser? ")
                print("Starting " + str(inp) + "...")
                try:
                    print("Trying to connect through port 443...")
                    time.sleep(1)
                    requests.get("https://www." + inp)
                    time.sleep(1)
                    www.open("www." + inp) 
                except Exception:
                    try:
                        print("Trying to connect through port 80...")
                        time.sleep(1)
                        requests.get("http://www." + inp)
                        www.open("www." + inp) 
                    except Exception:
                        try:
                            requests.get("https://www.google.com")
                            print("INVALID URL!")
                        except Exception:
                            print("Unable to connect to Wi-Fi!")
                            Auto_wifi_connection()

            if 'browser' in inp:
                print("Starting Firefox...")
                time.sleep(1)
                try:
                    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk")
                except Exception:
                    print("Shourtcut not found in specified location!")
        if 'clear' in inp:
            def clear():
                os.system('cls')
            clear()
        if 'hello' in inp:
            with open("Communication_Files/Greetings/main.txt")as file:
                allText = file.read()
                words = list(map(str, allText.splitlines()))
            from random import choice as ch
            print(ch(words))
        
        if 'bank account' in inp:
            import pyodbc
            try:
                current_dir = os.getcwd()
                con_string = r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(current_dir) + "/Main_DB.accdb;"
                conn = pyodbc.connect(con_string)
                cursor = conn.cursor()
                q = input("Do you want to create a new account? ")
                if "yes" in q:
                    pin = input("Enter your new PIN: ")
                    card_number = input("Enter your cardnumber:")
                    currency = input("Currency that you use on this credit/debit card:")
                    holder_name = input("Enter your holdername: ")
                    cvv = input("Enter your cvv(found on the back of the credit/debit card): ")
                    exp_date = input("Enter your card's expiration date: ")
                    new_user = (
                        (pin,card_number,currency,holder_name,cvv,exp_date)
                    )
                    cursor.execute('INSERT INTO Bank_Details VALUES (?,?,?,?,?,?)', new_user)
                    conn.commit()
                    print("Data Inserted")
                if "no" in q:
                    pin_input = input("Provide your PIN in order to access your debit/credit card information: ")
                    pin = cursor.execute('SELECT * FROM Bank_Details')
                    data = cursor.fetchall()
                    for row in data:
                        pin = row[0]
                        if pin_input == pin:
                            all_data = cursor.execute('SELECT * FROM Bank_Details')
                            print("Cardnumber: " + row[1] + " " + row[2])
                            print("Holder Name: " + row[3])
                            print("CVV: " + row[4])
                            print("Expiration_Date: " + row[5])
            except pyodbc.Error as e:
                print("Error: ", e)
            

        if 'website' in inp:
            invalid = False
            inp = input("Which is your desired website? ")
            print("Starting " + str(inp) + "...")
            try:
                print("Trying to connect through port 443...")
                time.sleep(1)
                requests.get("https://www." + inp)
                time.sleep(1)
                www.open("www." + inp) 
            except Exception:
                try:
                    print("Trying to connect through port 80...")
                    time.sleep(1)
                    requests.get("http://www." + inp)
                    www.open("www." + inp) 
                except Exception:
                    try:
                        requests.get("https://www.google.com")
                        print("INVALID URL!")
                    except Exception:
                        print("Unable to connect to Wi-Fi!")
                        Auto_wifi_connection()
        if 'developer mode' in inp:
            developer_mode()
        if 'secret' in inp:
            print("Get Ready!")
            time.sleep(1)
            print("Generating the Secret...")
            time.sleep(2)
            Secret()

        
        if 'send email' in inp:
            print("Connecting to email...")
            time.sleep(1.5)
            mail_send()

        if 'speedtest' in inp:
            Speedtest()
            
        if 'to do' in inp:
            to_do_list()
            
        if 'are you' in inp:
            with open("Communication_Files/Wyd/main.txt") as file:
                allText = file.read()
                words = list(map(str, allText.splitlines()))
            from random import choice as ch
            print(ch(words))
        
        if 'morning' in inp:
            now  = datetime.now()
            current_time = now.strftime("%H:%M")
            hour = now.strftime("%H")
            if(7<int(hour)<12):
                print("Good Morning sir! " + "It's " + str(current_time) + '.')
                print("Hope you'll have a great day!")
            else:
                print("Boss, it's not morning anymore. You lost your time sense. It's " + str(current_time))
    except socket.gaierror and urllib3.exceptions.NewConnectionError and urllib3.exceptions.MaxRetryError and requests.exceptions.ConnectionError as Exception:
        Auto_wifi_connection()
    except FileNotFoundError as Exception:
        print("File not found!")

    if 'voice control' in inp:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
        with open("Communication_Files/Greetings/main.txt") as file:
            allText = file.read()
            words = list(map(str, allText.splitlines()))
        username = Path('Username.txt').read_text()
        from random import choice as ch
        engine.say(ch(words))
        engine.runAndWait()
        ok = True
        while ok:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=1)
                    engine = pyttsx3.init()
                    print('Listening...')
                    engine.say("I'm Listening:")
                    engine.runAndWait()
                    text = r.recognize_google(r.listen(source, timeout=5, phrase_time_limit=5, snowboy_configuration=None))
                    print(text)
                    if 'good morning' in text:
                        now = datetime.now()
                        current_time = now.strftime("%H" + ":" + "%M")
                        print("Good Morning sir! " + "It's " + str(current_time) + '.')
                        engine.say("Good Morning sir! " + "It's " + str(current_time) + '.')
                        engine.runAndWait()
                        print("Hope you'll have a great day!")
                        engine.say("Hope you'll have a great day!")
                    if 'open' in text:
                        try:
                            options = Path('shortcut_list.json').read_text()
                            print("Apps already added: ")
                            print(options)
                            filename = input("App Name: ")
                            file_loc = "D:/Python/Jarvis-main/Apps/" + filename + ".txt"
                            shortcut = Path(str(file_loc)).read_text()
                            os.startfile(shortcut)
                        except FileNotFoundError:
                            print("File not found")
                        except Warning as w:
                            print(w)
                            continue
                        except Exception as e:
                            print(e)

                    if 'clear' in text:
                        os.system('cls')
                    if 'weather' in text:
                        print("Requesting weather info from our provider...")
                        import requests
                        import json
                        api_key = '90e19536df9f0408dfc9f39e73a0ff89'
                        base_url = "http://api.openweathermap.org/data/2.5/weather?"
                        from ipdata import ipdata
                        from pprint import pprint
                        import re
                        import pyautogui as pag
                        import geoip2.database
                        ipdata = ipdata.IPData('cb885e8fa8f25a578285d2043c59d2dc6f54a77b87cb6455f3d7c30f')
                        ip = requests.get("https://api.ipify.org").text
                        Ip = ip
                        print("Getting location for " + Ip + "...")
                        time.sleep(1.5)
                        with geoip2.database.Reader('GeoLite2-City_20210105/GeoLite2-City.mmdb') as reader:
                            print("Retrieving data from our large database... ")
                            time.sleep(0.5)
                            ip_address_location = reader.city(Ip)
                            ip_rasa = ip_address_location.city.name
                            city_name = ip_rasa
                            complete_url = base_url + "appid=" + api_key + "&q=" + str(city_name)
                            response = requests.get(complete_url)
                            x = response.json()
                            if x["cod"] != "404":
                                y = x["main"]
                                current_temperature = y["temp"]
                                current_pressure = y["pressure"]
                                current_humidiy = y["humidity"]
                                z = x["weather"]
                                weather_description = z[0]["description"]
                                round(current_temperature, 2)
                                Temperature = current_temperature - 273.15
                                current_pressure = current_pressure * 0.75
                                print("Weather in " + str(city_name) +" on " + str(date.today()) + ":")
                                engine = pyttsx3.init()
                                engine.say("Weather in " + str(city_name) + " on " + str(date.today()) + ":")
                                engine.runAndWait()
                                print("Temperature: " + str("%.2f" % Temperature) + ' ' + "°C")
                                engine.say("Temperature: " + str("%.2f" % Temperature) + "  Celcius Degrees")
                                engine.runAndWait()
                                print("Pressure: " + str(current_pressure) + ' ' + "mm Hg")
                                engine.say("Pressure: " + str(current_pressure) + " Milimeters of Mercury")
                                engine.runAndWait()
                                print("Humidity: " + str(current_humidiy) + "%")
                                engine.say("Humidity: " + str(current_humidiy) + "%")
                                engine.runAndWait()
                                print("Weather Condition: " + str(weather_description))
                                engine.say("Weather Condition: " + str(weather_description))
                                engine.runAndWait()
                            else:
                                print(" City Not Found ")
                                engine.say("City Not Found")
                                engine.runAndWait()
                                
                    if 'convert' in text:
                        class Currency_convertor:
                            rates = {}
                            def __init__(self, url):
                                data = requests.get(url).json()
                                self.rates = data["rates"]
                            def convert(self, from_currency, to_currency, amount):
                                initial_amount = amount
                                if from_currency != 'EUR' :
                                    amount = amount / self.rates[from_currency]
                                amount = round(amount * self.rates[to_currency], 2)
                                print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

                        if __name__ == "__main__":
                            try:
                                engine = pyttsx3.init()
                                print("Starting currency convertor...")
                                engine.say("Starting Currency convertor:")
                                engine.runAndWait()
                                url = str.__add__('http://data.fixer.io/api/latest?access_key=', "03638ce484feacf1482a1199cb48d8d4")
                                c = Currency_convertor(url)
                                from_country = input("From Country: ")
                                to_country = input("TO Country: ")
                                amount = int(input("Amount: "))
                                print("Gathering Information from our trustworthy provider...")
                                engine = pyttsx3.init()
                                engine.say("Gathering Information from our trustworthy provider:")
                                engine.runAndWait()
                                time.sleep(1)
                                c.convert(from_country, to_country, amount)
                            except KeyError:
                                print("Unknown Currency! Try Again!")
                                engine = pyttsx3.init()
                                engine.say("Unknown Currency: Try Again:")
                                engine.runAndWait()
                                print("Error type: KeyError")
                                engine = pyttsx3.init()
                                engine.say("Error type: KeyError:")
                                engine.runAndWait()
                            except ValueError:
                                print("Amount error! Try Again!")
                                engine = pyttsx3.init()
                                engine.say("Amount error: Try Again:")
                                engine.runAndWait()
                                print("Error type: ValueError:")
                                engine = pyttsx3.init()
                                engine.say("Error type: ValueError:")
                                engine.runAndWait()
                        
                    if 'password' in text:
                        print("Starting password generator...")
                        engine = pyttsx3.init()
                        engine.say("Starting password generator:")
                        engine.runAndWait()
                        Password_Generator()

                    if 'hello' in text:
                        engine = pyttsx3.init()
                        with open("Communication_Files/Greetings/main.txt") as file:
                            allText = file.read()
                            words = list(map(str, allText.splitlines()))
                        print(ch(words))
                        engine.say(ch(words))
                        engine.runAndWait()

                    if 'internet' in text:
                        engine = pyttsx3.init()
                        engine.say("Do you want a website or just the browser?")
                        engine.runAndWait()
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio_data = r.record(source, duration=1)
                            print('Listening...')
                            text = r.recognize_google(r.listen(source, timeout=5, phrase_time_limit=5, snowboy_configuration=None))
                            print(text)
                        if 'browser' in text:
                            engine = pyttsx3.init()
                            engine.say("Opening Firefox...")
                            engine.runAndWait()
                            try:
                                os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Firefox.lnk")
                            except Exception:
                                print("Could not found the shortcut in specified location!")
                        if 'website' in text:
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                audio_data = r.record(source, duration=1)
                                engine = pyttsx3.init()
                                print("Listening to your desired browser: ")
                            #inp = input('Enter your desired browser: ')
                                engine.say("Tell your desired browser...")
                                engine.runAndWait()
                                text = r.recognize_google(r.listen(source, timeout=5, phrase_time_limit=5, snowboy_configuration=None))
                                print(text)
                            invalid = False
                            print("Starting " + str(text) + "...")
                            try:
                                print("Trying to connect through port 443...")
                                time.sleep(1)
                                requests.get("https://www." + text)
                                time.sleep(1)
                                www.open("www." + text) 
                            except Exception:
                                try:
                                    print("Trying to connect through port 80...")
                                    time.sleep(1)
                                    requests.get("http://www." + text)
                                    www.open("www." + text) 
                                except Exception:
                                    try:
                                        requests.get("https://www.google.com")
                                        print("INVALID URL!")
                                    except Exception:
                                        print("Unable to connect to Wi-Fi!")
                                        Auto_wifi_connection()

                    if 'sleep' in text:
                        engine = pyttsx3.init()
                        with open("Communication_Files/Sleep/main.txt") as file:
                            allText = file.read()
                            words = list(map(str, allText.splitlines()))
                        engine.say(ch(words))
                        engine.runAndWait()
                        inp = input('sleeping...')

                    if 'exit' in text:
                        with open("Communication_Files/Goodbyes/main.txt") as file:
                            allText = file.read()
                            words = list(map(str, allText.splitlines()))
                        engine.say(ch(words))
                        engine.runAndWait()
                        sys.exit()
                        
                    if "update" in text:
                        update()

                    if 'news' in text:
                        engine.say('Gathering the latest news for you!')
                        print("Gathering the latest news for you!")
                        engine.runAndWait()
                        engine.say("Please Wait...")
                        print('Please Wait...')
                        engine.runAndWait()
                        time.sleep(1.5)
                        news()

                    if 'system' in text:
                        System_info()

                    if 'music' in text:
                        engine = pyttsx3.init()
                        engine.say("Get ready for the party.: Some cool music is coming right now:")
                        engine.runAndWait()
                        print("Starting Spotify:")
                        os.startfile('C:/Users/alexc/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify.lnk')

                    if 'shut down' in text:
                        engine = pyttsx3.init()
                        print("Your PC will shutdown in 5 seconds...")
                        engine.say("Your PC will shutdown in 5 seconds:")
                        engine.runAndWait()
                        os.system('shutdown /s /t 6')
                        inp = input("")

                    if 'Gmail' in text:
                        engine = pyttsx3.init()
                        print("Opening gmail...")
                        engine.say("Opening gmail")
                        engine.runAndWait()
                        time.sleep(0.5)
                        mail_url = 'https://mail.google.com/mail/u/0/#inbox'
                        www.open(mail_url)
                    
                    if 'games' in text:
                        print("Opening your game lanuncher...")
                        engine = pyttsx3.init()
                        engine.say("Opening you game launcher")
                        engine.runAndWait()
                        Games()
                    if 'phone number' in text:
                        print("Getting phone number data... ")
                        engine.say("Getting phone number data... ")
                        time.sleep(0.5)
                        phone_number_info()
                        
                    if 'IP' in text:
                        engine = pyttsx3.init()
                        print("Getting your IP...")
                        engine.say("Getting your IP")
                        engine.runAndWait()
                        print("Getting your hostname...")
                        engine.say("Getting your hostname")
                        engine.runAndWait()
                        hostname = socket.gethostname()
                        IPAddr = socket.gethostbyname(hostname)
                        print("Your Computer name is: " + str(hostname))
                        engine.say("Your Computer name is: " + str(hostname))
                        engine.runAndWait()
                        print("Your Computer IP Address is: " + str(IPAddr))
                        engine.say("Your Computer IP Address is: " + str(IPAddr))
                        engine.runAndWait()
                    
                    if 'coronavirus' in text:
                        import requests
                        import json
                        from bs4 import BeautifulSoup
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            engine = pyttsx3.init()
                            print("Which country would you like to get the coronavirus info for?")
                            engine.say("Which country would you like to get the coronavirus info for?")
                            engine.runAndWait()
                            audio_data = r.record(source, duration=1)
                            engine = pyttsx3.init()
                            print("Listening...")
                            engine.say("I'm listening")
                            engine.runAndWait()
                            text = r.recognize_google(r.listen(source, timeout=5, phrase_time_limit=5, snowboy_configuration=None))
                            print(text)
                            import json
                            import requests
                            from bs4 import BeautifulSoup
                            import re
                            try:
                                country_name = text
                                URL = 'https://www.worldometers.info/coronavirus/country/' + str(country_name)
                                page = requests.get(URL)
                                soup = BeautifulSoup(page.content, 'html.parser')
                                results = soup.find(id='maincounter-wrap')
                                string = results.prettify()
                                string = re.sub('[^0-9]', '', string)
                                string = string[4:]
                                engine = pyttsx3.init()
                                print("There are " + str(string) + " coronavirus cases in " + str(country_name) + " on " + str(date.today()) + '.')
                                engine.say("There are " + str(string) + " coronavirus cases in " + str(country_name) + " on " + str(date.today()) + '.')
                                engine.runAndWait()
                            except AttributeError:
                                engine = pyttsx3.init()
                                engine.say("Unknown country, try again!")
                                print("Unknown country, try again!")
                                engine.runAndWait()
                            except ConnectionError:
                                engine = pyttsx3.init()
                                engine.say("Check your internet connection and try again!")
                                print("Check your internet connection and try again!")
                                engine.runAndWait()
                    
                    if 'website' in text:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio_data = r.record(source, duration=1)
                            engine = pyttsx3.init()
                            print("Listening to your desired browser: ")
                            #inp = input('Enter your desired browser: ')
                            engine.say("Tell me your desired browser...")
                            engine.runAndWait()
                            text = r.recognize_google(r.listen(source, timeout=5, phrase_time_limit=5, snowboy_configuration=None))
                            print(text)
                        invalid = False
                        print("Starting " + str(text) + "...")
                        try:
                            print("Trying to connect through port 443...")
                            time.sleep(1)
                            requests.get("https://www." + text)
                            time.sleep(1)
                            www.open("www." + text) 
                        except Exception:
                            try:
                                print("Trying to connect through port 80...")
                                time.sleep(1)
                                requests.get("http://www." + text)
                                www.open("www." + text) 
                            except Exception:
                                try:
                                    requests.get("https://www.google.com")
                                    print("INVALID URL!")
                                except Exception:
                                    print("Unable to connect to Wi-Fi!")
                                    Auto_wifi_connection()

                    if 'help' in text:
                        features()
        
                    if 'Wi-Fi' in text:
                        time.sleep(2)
                        import subprocess
                        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
                        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
                        for i in profiles:
                            try:
                                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                                try:
                                    print ("{:<30}|  {:<}".format(i, results[0]))
                                except IndexError:
                                    print ("{:<30}|  {:<}".format(i, ""))
                            except subprocess.CalledProcessError:
                                print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
                    
                    if 'stop conversation' in text:
                        engine = pyttsx3.init()
                        engine.say("OK, it's your wish!")
                        engine.runAndWait()
                        ok = False
                        
                    if 'deactivate' in text:
                        print("Goodbye! Have a nice day!")
                        engine = pyttsx3.init()
                        engine.say("Goodbye: Have a nice day:")
                        engine.runAndWait()
                        exit_arack()
                        
                    if 'text mode' in text:
                        engine = pyttsx3.init()
                        engine.say("OK, it's your wish!")
                        engine.runAndWait()
                        ok = False
            except TimeoutError:
                engine = pyttsx3.init()
                print("Process timed out. We are sorry for this but I will return u to text mode.")
                engine.say("Process timed out. We are sorry for this but I will return u to text mode")
                engine.runAndWait()
                ok = False
            except IndentationError:
                print("Indendatioon error. Check if u 'tabbed' your lines correctly!")
                engine = pyttsx3.init()
                engine.say("Indendatioon error. Check if u 'tabbed' your lines correctly!")
                engine.runAndWait()
                sys.exit()
            except sr.UnknownValueError as Exception:
                engine = pyttsx3.init()
                print("No audio detected, you will be returned to text mode.")
                engine.say("No audio detected, you will be returned to text mode.")
                engine.runAndWait()
                ok = False
            except sr.WaitTimeoutError as Exception:
                engine = pyttsx3.init()
                print("Process timed out. We are sorry for this but we will return u to text mode.")
                engine.say("Process timed out. We are sorry for this but we will return u to text mode.")
                engine.runAndWait()
                ok = False
                inp = input('>>>')
            except socket.gaierror and urllib.error.URLError and sr.RequestError as Exception:
                engine = pyttsx3.init()
                print("No internet connection detected! Check your WiFi connection and try again!")
                engine.say("No internet connection detected! Check your WiFi connection and try again!")
                engine.runAndWait()
                def createNewConnection(name, SSID, key):
                    config = """<?xml version=\"1.0\"?>
                <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                    <name>"""+name+"""</name>
                    <SSIDConfig>
                        <SSID>
                            <name>"""+SSID+"""</name>
                        </SSID>
                    </SSIDConfig>
                    <connectionType>ESS</connectionType>
                    <connectionMode>auto</connectionMode>
                    <MSM>
                        <security>
                            <authEncryption>
                                <authentication>WPA2PSK</authentication>
                                <encryption>AES</encryption>
                                <useOneX>false</useOneX>
                            </authEncryption>
                            <sharedKey>
                                <keyType>passPhrase</keyType>
                                <protected>false</protected>
                                <keyMaterial>"""+key+"""</keyMaterial>
                            </sharedKey>
                        </security>
                    </MSM>
                </WLANProfile>"""
                    if platform.system() == "Windows":
                        command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"
                        with open(name+".xml", 'w') as file:
                            file.write(config)
                    elif platform.system() == "Linux":
                        command = "nmcli dev wifi connect '"+SSID+"' password '"+key+"'"
                    os.system(command)
                    if platform.system() == "Windows":
                        os.remove(name+".xml")

                def connect(name, SSID):
                    if platform.system() == "Windows":
                        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
                    elif platform.system() == "Linux":
                        command = "nmcli con up "+SSID
                    os.system(command)
                    
                def displayAvailableNetworks():
                    if platform.system() == "Windows":
                        command = "netsh wlan show networks interface=Wi-Fi"
                    elif platform.system() == "Linux":
                        command = "nmcli dev wifi list"
                    os.system(command)
                
                displayAvailableNetworks()
                option = input("Do you want to register a new connection?(yes or no)")
                if 'n' in option:
                    name = input("Name: ")
                    connect(name, name)
                    time.sleep(2)
                    try:
                        url = 'https://google.com'
                        timeout = 5
                        request = requests.get(url, timeout=5)
                        print("You are ready to go")
                        engine.say("You are ready to go")
                        engine.runAndWait()
                    except(requests.ConnectionError, requests.Timeout, socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as Exception:
                        print("I couldn't connect you to the Internet through Wi-Fi...")
                        engine.say("I couldn't connect you to the Internet through Wi-Fi...")
                        engine.runAndWait()
                        print("TRY AGAIN WITH CORRECT CREDENTIALS!")
                        engine.say("TRY AGAIN WITH CORRECT CREDENTIALS!")
                        engine.runAndWait()
                        print("If still not working, please contact your Internet service provider and somehow, get along with this issue!")
                        engine.say("If still not working, please contact your Internet service provider and somehow, get along with this issue!")
                        engine.runAndWait()
                        sys.exit()

                if 'y' in option:
                    name = input("SSID: ")
                    key = input("Password: ")
                    createNewConnection(name, name, key)
                    connect(name, name)
                    time.sleep(2)
                    try:
                        timeout = 5
                        url = 'https://www.google.com'
                        request = requests.get(url, timeout=5)
                        print("New connection created!\nYou are ready to go!")
                        engine.say("New connection created, you are ready to go!")
                        engine.runAndWait()
                    except(requests.ConnectionError, requests.Timeout, socket.gaierror, urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError, requests.exceptions.ConnectionError) as Exception:
                        print("I couldn't find a connection that matches: ")
                        engine.say("I couldn't find a connection that matches to your credentials!")
                        engine.runAndWait()
                        print("SSID = " + name)
                        print("Password = " + key)
                        sys.exit()
