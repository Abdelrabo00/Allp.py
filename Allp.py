# Imports
####################################
from urllib.request import *       #
from requests import get, post     #
from socket import *               #
import scapy.all as scapy          #
from os import system              #
from time import sleep             #
from subprocess import call        #
from art import *                  #
import sys                         #
from termcolor import colored      #
####################################
tools = ["1 : Arping", "2 : IP Identifier", "3 : Portchecker", "4 : Macchanger", "5 : Pic&PDFdownloader"]
# Vars
######
system('clear')
sleep(2)
print(colored("Loading .......",'blue'))
sleep(1)
print(colored("Loading ....",'blue'))
sleep(1)
print(colored("Loading ..",'blue'))
sleep(1)
system('clear')
txt = "The Final Project"
tprint(txt.center(50))
print('\n')
for x in tools:
    print(x)
print('\n')
sleep(1)

# User input for tool selection
try:
    user = int(input(f"Kindly enter your required Tool : "))
except Exception:
    pass
    user = int(input(f"kindly enter your required Tool :"))
if user =="exit":
    sys.exit()
##################################################################################################
system("clear")

# FUNCTIONS
##########
def IP():
    sleep(2)
    text = 'IPIdentfier'.center(50)
    tprint(text)
    while True:
        try:
            sleep(2)
            user = input("Kindly enter your required DNS : ")
            if user == "exit":
                sys.exit()
            data = gethostbyname(user)
            print(f"Your Target IP Address is : {data} \n would you like to check the open ports of this IP ?\n ")
            user2 = input("Kindly choose between yes or no : ")
            if user2 == "exit":
                sys.exit()
            if user2 == 'yes':
                start = int(input('Kindly enter your Start Port : '))
                end = int(input("Kindly enter your end port : "))
                system('clear')
                print('Stats' , '\t' , 'Port' , '\t' , 'Service')
                for port in range(start,end):
                    sockj = socket(AF_INET , SOCK_STREAM)
                    sockj.settimeout(0.1)
                    try:
                        sockj.connect((data,port))
                        print(f"Opened \t {port}" , '\t' , getservbyport(port))
                    except Exception:
                        #print(f"Closed \t {port}" , '\t'  ,  'None')
                         pass
            elif user2 == 'no':
                sys.exit()
        except Exception:
            print("Loading ...... ")

def Portchecker():
    text = 'Portchecker'.center(50)
    sleep(1)
    tprint(text)
    sleep(1)
    try:
            user = input('Kindly enter your required Ip : ')
            start = int(input('Kindly enter your Start Port : '))
            end = int(input("Kindly enter your end port : "))
            if "exit" in [user , start , end]:
                sys.exit()
            system('clear')
            print('Stats' , '\t' , 'Port' , '\t' , 'Service')
            for port in range(start,end):
                sockj = socket(AF_INET , SOCK_STREAM)
                sockj.settimeout(0.05)
                try:
                     sockj.connect((user,port))
                     print(f"Opened \t {port}" , '\t' , getservbyport(port))
                except Exception:
                    #print(f"Closed \t {port}" , '\t'  ,  'None')
                    pass
    except Exception:
        print("something went wrong")

def arping():
    sleep(2)
    txt = "ARPING".center(50)
    tprint(txt)
    scapy.arping("192.168.1.0/24")
    print('\n')
    user = input(colored('Would you like to take a look to the menu again , [yes or no] :','red'))
    if user == 'yes':
        call("python3 allp2.py",shell = True)
        
def mac():
    sleep(2)
    text = "Macchanger".center(50)
    tprint(text)
    sleep(2)
    mac_list = ['1 : 64:51:06:2b:29:da', '2 : 64:51:06:2b:29:e1', '3 : 64:51:06:2b:29:f4', '4 : 64:51:06:2b:29:ab', '5 : 64:51:06:2b:29:88']
    try:
        sleep(1)
        user1 = input(f"Kindly choose between auto or man : ")
        if user1 =="exit":
            sys.exit()
        if user1 == 'auto':
            print('\n')
            print("Now copy one of them and paste it after picking the interface ")
            for i in mac_list:
                print(i)
        sleep(1)
        user2 = input("Kindly enter your required Interface [EX: eth0 , wlan0 , eno1] : ")
        sleep(1)
        user3 = input("Kindly type your required Mac address [xx:xx:xx:xx:xx:xx] :")
        if "exit" in [user2 , user3]:
            sys.exit()
        if user2:
            call(f"ifconfig {user2}  down", shell=True)
            call(f"ifconfig {user2} hw ether {user3}", shell=True)
            call(f"ifconfig {user2} up", shell=True);print('\n')
            print(f"[+]Your Mac  has been changed successfully to : {user3} ")
            call(f"ifconfig {user2} | grep ether" ,shell=True);print('\n')
            user4 = input(colored("Would you like to take a look to the menu again , [yes or no] :",'red'))
            print('\n')
            if user4 == 'yes':
                call("python3 allp2.py",shell=True)

    except Exception as e:
            print('Something went wrong', e)
            mac()

def downloader():
    sleep(2)
    text = "Downloader".center(50)
    tprint(text)
    sleep(1)
    try:
        print("Just copy the image or the pdf address ")
        print('\n')
        data = input('Kindly enter your required link : ')
        response2 = data.split('/')
        response3 = data[-1]
        response = get(data)
        with open(response3, mode='wb') as f:
            f.write(response.content);print('\n')
        print(f"Your file {response3} has sucessfully downloaded")
        user = input(colored('Would you like to take a look to the menu again , [ yes or no ] :' , 'red'))

    except Exception as e:
        if data == 'exit':
            sys.exit()
        system("clear")
        downloader()
        print("Something went wrong ", e)

#Run
if user == 5:
    downloader()
elif user == 4:
    mac()
elif user == 3:
    Portchecker()
elif user == 2:
    IP()
elif user == 1:
    arping()

