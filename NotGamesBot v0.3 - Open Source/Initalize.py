import string
from Socket import sendMessage
from Settings import JoinMessage

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(2048).decode('utf-8')
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = LoadingCompleat(line)
    sendMessage(s, JoinMessage)

def LoadingCompleat (line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
