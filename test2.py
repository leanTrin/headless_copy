#!/usr/bin/env python3
##########################################################
# Created by Leandro Trinidad
# Description:
#   Copies a certain folder of a usb to another folder in
#   the pi. Useful for Copying files while the pi is in
#   headless mode.
#
# Prequsities
#   - eject -- run 'sudo apt install eject'
####################################
import os
from shutil import copyfile
import time
import subprocess

dev = False                         # If True: logs the information in the terminal

usb = "/media/pi/9132-18E9/movies"  #TODO: this will be different when using other usbs
usbDisk = "/dev/sda1"               #TODO: auto detect a new usb pluged in and see the folders
storage = "/home/pi/Movies"         #TODO: the storage folder can be in another usb

def printlog(text):
    if dev:
        print("[%s]: %s" %(time.asctime( time.localtime(time.time())),text))

def usbMovieFolder():
    usb = "/media/pi/"
    dirlist = os.listdir(usb)
    for item in dirlist:
        dirs = usb + "/" +item
        if os.path.isdir(dirs):
            if "movies" in os.listdir(dirs):
                movieDir = dirs + "/" + "movies"
                return movieDir
    return None

while True: #TODO: check if a while loop is a good idea ran as a service in pi
    try:
        if(os.path.isdir(usb)): # When the usb is pluged in

            copy = []

            usbFiles = [f for f in os.listdir(usb)]
            storageFiles = [f for f in os.listdir(storage)]

            for usbItem in usbFiles:

                if(usbItem not in storageFiles):
                    copy.append(usbItem)

            if(copy): # if there is a new file in the usb that is not already in the server

                printlog(copy)

                for item in copy:

                    printlog("copying " + item)
                    copyfile(usb + "/" + item, storage + "/" + item) #TODO: error checking
                    printlog("done")

            #TODO: gpio lights
            os.system('sudo eject ' + usbDisk) # need 'eject' to be installed
            printlog("Files Copied")
            time.sleep(10)
    except:
        pass

