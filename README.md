# PlaylistADB

I had a bunch of playlists on my phone and wanted them on my computer. However, the music library on my computer is much less organized than the music on my phone! This script reads a playlist file (tested with .m3u8) and downloads every song from your phone to your computer.

## Dependencies
This script is written in Python 3.

It relies on Android Debug Bridge (ADB), which is packaged with the Android SDK. You can also just download ADB if you search for it.

## Setup
0. Install and set up ADB.
1. Enable ADB on your Android phone:
    1. Settings - About phone
    2. Tap "Build number" seven times. A toast should come up informing you that you are now a developer.
    3. Go back to settings, and click on the new Developer options
    4. Scroll down to USB debugging. Switch it on and confirm.
    5. Plug phone into your computer, and run `adb devices`. A prompt should come up on your phone screen, asking you to accept the RSA key. Confirm.
2. Pull the playlist files off of your phone. You might have to export them from your music player. You can do this with the GUI, or just `adb pull /path/to/your/playlist/files`.
3. Copy the playlist files to the same directory as the script and run it. When it asks for the filename, enter the full name of the playlist you want to import (e.g. 'playlist.m3u8').
4. Enjoy!

## To do
  *Read arguments from command line
  *Automatic mode - iterates through every playlist file in directory automatically
  *Make new directory with same name as playlist for each file
  *Organize code
  *Pretend this took longer than fifteen minutes to make
