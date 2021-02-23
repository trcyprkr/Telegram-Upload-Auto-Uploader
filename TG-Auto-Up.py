import datetime as dt
import time
import os
import subprocess

PATH = '/home/pi/Public/'
def get_sleeptime(minute, second):
    now = dt.datetime.now()
    sched = now.replace(minute=minute, second=second)
    sleeptime = (sched - now).total_seconds()
    if sleeptime < 0:
        sleeptime += 3600
    return sleeptime

for root, subFolder, files in os.walk(PATH):
    files.sort(key=str.lower) #Sorts files alphabetically
    subFolder.sort()
    for item in files:
        fileNamePath = os.path.join(root, item)
        print("Uploading: " + fileNamePath)
        print("")
        subprocess.run(['telegram-upload', '-d', '-f', 'YOUR_CHANNEL_GOES_HERE', str(fileNamePath)])
        # See Telegram-Upload Usage here for install and option https://docs.nekmo.org/telegram-upload/usage.html
        print("")
        print("Upload Successful >> " + time.asctime())
        print("")
        time.sleep(1) # This was needed to break the loop long enough for the 'get_sleep' timer below become active
        print(" <<... Waiting To Upload New File ...>> ")
        time.sleep(get_sleeptime(0, 0)) #Here the sleep timer is set to 0 Hour, 0 Second, which is the top of the hour
