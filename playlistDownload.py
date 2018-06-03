#!/usr/local/bin/python3
#Version 1.0

import subprocess
import time

#Ask for filename, put into list
filename = input("What's your filename? ")
songList=[]
with open(filename,"r") as f:
    songList=f.read().splitlines()
print(songList)

#Pull files
for i in songList:
    #The ADB part of the command
    adbCommand = "adb pull "
    #Adding filename to pull
    adbList = adbCommand.split()
    adbList.append(i)
    # print(adbList)
    #Execute
    subprocess.Popen(adbList)
print("Done")
