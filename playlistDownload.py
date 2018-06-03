#!/usr/local/bin/python3

import subprocess
import time
import sys
import os
version=2.0

#Ask for filename, put into list
def readFile(filename):
    songList=[]
    with open(filename,"r") as f:
        songList=f.read().splitlines()
    return songList

#Pull files
def pullFiles(listIn,destination):
    for i in listIn:
        #The ADB part of the command
        adbCommand = "adb pull "
        #Adding filename to pull and destination to pull to
        adbList = adbCommand.split()
        adbList.append(i)
        adbList.append(destination)
        # print(adbList)
        #Execute
        subprocess.Popen(adbList)

def autoMode():
    filesList=[]
    dirName=""
    print("Automatic mode: pulling from all m3u8 files in directory")
    for files in os.listdir("./"):
        if files.endswith(".m3u8"):
            filesList.append(os.path.join("./",files))
    for i in filesList:
        dirName=i.strip(".")
        dirName=dirName.strip("/")
        dirName=dirName.strip(".m3u8")
        # print("Pure dirname: ",dirName)
        subprocess.Popen(("mkdir",dirName))
        dirName="./"+dirName
        # print(i)
        # print("Dirname:",dirName)
        pullFiles(readFile(i),dirName)
    print("Done")

def dispHelp():
    print("Playlist ADB version ",version)
    print("\nUsage: ./playlistDownload.py [ -ahf ]\n")
    print("\nArguments:\n")
    print("-a, --auto\t\t\t Automatically download from every playlist in directory\n")
    print("-f, --file <filename>\t\t Specify playlist to download from command line\n")
    print("-h, --help\t\t\t Display this help message\n")

if __name__ == "__main__":
    caught=False
    # print(sys.argv)
    # print(("-a" or "--auto") in sys.argv)
    #guess I don't know how python works lol
    
    if ("-a" or "--auto") in sys.argv:
        autoMode()
        caught=True
    if ("-h" or "--help") in sys.argv:
        dispHelp()
        caught=True
    if "-f" in sys.argv:
        argPlacement=sys.argv.index("-f")
        pullFiles(readFile(sys.argv[argPlacement+1]))
        caught=True
    if "--file" in sys.argv:
        argPlacement=sys.argv.index("-file")
        pullFiles(readFile(sys.argv[argPlacement+1]))
        caught=True
    elif caught==False:
        filename = input("Enter filename of playlist: ")
        pullFiles(readFile(filename),"./")
        print("Done")
