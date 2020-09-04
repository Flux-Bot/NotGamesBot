#This runs of the Twitch API v5. This needs to bu upgraded to the new Twitch API.

import sys, json, requests;
import datetime
from dateutil.relativedelta import relativedelta
from Settings import ClientID, OAuth
temp = ""
tempArr = []

oauth = (OAuth)
headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': (ClientID),
    'Authorization': 'OAuth ' + oauth,
}

try:
    response = requests.get('https://api.twitch.tv/kraken/streams/00000000', headers=headers)  #Replace 00000000 with the cliant ID of the channel you whant to connect to. This will be fixed in the futer to automaticly fill this in
    data = response.json()
except (KeyError, ValueError):
    print("Error - make sure your OAuth is formatted correctly")
    sys.exit(1)

def live():
    temp = json.dumps(data)
    print(temp)
    if temp == ('{"stream": null}'):
        Live = False
        print("not Live")
    elif temp != ('{"stream": null}'):
        Live = True
        print("We are Live")
    return Live


def uptime():
    temp = json.dumps(data)
    #Seperates the time and date from Twitch API
    tempArr = temp.split(",")
    temp = (tempArr[9])
    created_at = temp.split(': "')
    created_at = created_at[1]
    DateTime = created_at.split("T")
    Date = DateTime[0]
    Time = DateTime[1]
    Time = Time.rstrip('"Z')

    #calculates the diffrense in time
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    a = (current_time)
    b = (Date + " " + Time)

    start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

    diff = relativedelta(start, ends)
    days = ("%d days" % diff.days)
    hours = (" %d hours" % (diff.hours))
    mins = (" %d minutes" % (diff.minutes))
    sec = (" %d seconds" % (diff.seconds))
    TimeDiff = ("%d days %d hours %d minutes %d seconds" % (diff.days, diff.hours -1, diff.minutes, diff.seconds))
    return TimeDiff
