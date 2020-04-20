import socket
from Settings import HOST, PORT, PASS, BOT, CHANNEL

def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send((f"PASS " + PASS + "\r\n").encode('utf-8'))
    s.send((f"NICK " + BOT + "\r\n").encode('utf-8'))
    s.send((f"JOIN #" + CHANNEL + "\r\n").encode('utf-8'))
    return s

def sendMessage(s, message):
    messageTemp = f"PRIVMSG #" + CHANNEL + " :" + message
    s.send((messageTemp + "\r\n").encode('utf-8'))
    print("Send: " + messageTemp)
