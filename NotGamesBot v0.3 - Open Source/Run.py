#!/usr/bin/python
import string
import random
import threading
from pynput import keyboard
from Socket import openSocket, sendMessage
from Initalize import joinRoom
from Read import getUser, getMessage
from Settings import NEWS, CHANNEL, MODS
from TwitchIntergration import uptime, live

schedule = ["Roger", "Paul", "Dan and Hannah", "Claire", "Andrea", "Jon", "Lucy"]
index = 0
UpNext = "Coming up next: "
ComingUp = ""

def next(index):
    index = index + 1
    ComingUp = UpNext + schedule[index]
    globals()["index"] = index
    globals()["ComingUp"] = ComingUp

def back(index):
    index = index - 1
    ComingUp = UpNext + schedule[index]
    globals()["index"] = index
    globals()["ComingUp"] = ComingUp

def HotKey():
    def on_release(key):
        if key == keyboard.Key.page_up:
            next(index)
            print(UpNext + schedule[index])
        if key == keyboard.Key.page_down:
            back(index)
            print(UpNext + schedule[index])
    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

HotKeys = threading.Thread(target=HotKey)
HotKeys.start()

def twitch():
    s = openSocket()
    joinRoom(s)
    readbuffer = ""
    Item=["Buy and review our game on steam: https://store.steampowered.com/app/1147550/Not_For_Broadcast/", "Buy the OST here: https://store.steampowered.com/app/1351390/Not_For_Broadcast_Original_Soundtrack/", "Join the discord: https://discord.gg/notforbroadcast", "Sign the petition: http://chng.it/qf7rkttHkB", "Follow us on Instagram and Twitter: @NotGamesUK"]
    ItemCount = 0
    DevCount = 0
    length = ""

    while True:
            readbuffer = readbuffer + s.recv(2048).decode('utf-8')
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()

            for line in temp:
                if line.startswith('PING'):
                    print("---PING RECEIVED---")
                    s.send("PONG\n".encode('utf-8'))
                    print("---PONG SENT---")

                else:
                    #Inport chat
                    user = getUser(line)
                    message = getMessage(line)
                    print(user + ": " + message)

                    #Comands--------------------------------------------------------------------------



                    if "!uptime" in message:
                        Live = live()
                        if Live == True:
                            TimeDiff = uptime()
                            uptime()
                            sendMessage(s, "@"+ user + " " + CHANNEL + " has been live for: " + TimeDiff)
                        elif Live == False:
                            sendMessage(s, "@"+ user + " " + CHANNEL + " is not live :(")


                    if "!commands" in message or "!help" in message:
                        sendMessage(s,"Here is a list of the current avalible commands: !uptime | !notgamesbot |")


#                    if "!schedule" in message:
#                        sendMessage(s,ComingUp)

                    if "!notgamesbot" in message:
                        sendMessage(s,"Hello I am The Not Games UK Twitch Bot v(0.4). I am currently in development at the moment. HOWEVER my source code is now available for free here: https://github.com/fluxcabury/NotGamesBot | If you want to know more you can always ask my creator Fluxcabury :)")



                    #Ban
                    if "Wanna become famous? Buy followers, primes and views on bigfollows.com (bigfollows. com)!" in message:
                        sendMessage(s, "/ban " + user)


MainThread = threading.Thread(target=twitch)
MainThread.start()
