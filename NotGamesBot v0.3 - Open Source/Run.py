#!/usr/bin/python
import string
from Socket import openSocket, sendMessage
from Initalize import joinRoom
from Read import getUser, getMessage
from Settings import CHANNEL
from TwitchIntergration import uptime, live

s = openSocket()
joinRoom(s)
readbuffer = ""
Num=int(0)
DevCount = 0

while True:
        readbuffer = readbuffer + s.recv(2048).decode('utf-8')
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()



        for line in temp:
            if line.startswith('PING'):
                print("---PING RECEIVED---")
                s.send("PONG\n".encode('utf-8'))
                print("---PONG SENT---")

                #Timer
                if Num>3:
                    Num=0
                    TimerOutput=Item[Num]
                    sendMessage(s, TimerOutput)
                    Num=1
                else:
                    TimerOutput=Item[Num]
                    sendMessage(s, TimerOutput)
                    Num=Num+1

            else:
                #Inport chat
                user = getUser(line)
                message = getMessage(line)
                print(user + ": " + message)


                #ENTER COMANDS BELOW

                if "!hello" in message:
                    sendMessage(s,"Hello " + user + " Wellcome to " + CHANNEL + " channel")

                #Uptime Command
                if "!uptime" in message:
                    Live = live()
                    if Live == True:
                        TimeDiff = uptime()
                        uptime()
                        sendMessage(s, user + " " + CHANNEL + " has been live for: " + TimeDiff)
                    elif Live == False:
                        sendMessage(s, "@"+ user + " " + CHANNEL + " is not live :(")

                if "!notgamesbot" in message:
                    sendMessage(s,"Hello I am The Not Games UK Twitch Bot v(0.3). I am currently in development at the moment. HOWEVER my source code is now available for free here: https://github.com/fluxcabury/NotGamesBot | If you want to know more you can always ask my creator Fluxcabury :)")

                if "!commands" in message:
                    sendMessage(s,"Here is a list of the current avalible commands: !hello | !uptime | !commands | !notgamesbot |")
