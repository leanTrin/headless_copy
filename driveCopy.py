import os
from shutil import copyfile
import time

dev = False

usb = "/media/pi/9132-18E9/movies"
usbDisk = "/dev/sda1"
storage = "/home/pi/Movies"

def printlog(text):
    if dev:
        print("[%s]: %s" %(time.asctime( time.localtime(time.time())),text))
while True:
    try:
        if(os.path.isdir(usb)):
            copy = []
            usbFiles = [f for f in os.listdir(usb)]
            storageFiles = [f for f in os.listdir(storage)]
            for i in usbFiles:
                if(i not in storageFiles):
                    copy.append(i)
            if(copy): # if there is a new file in the usb that is not already in the server
                printlog(copy)
                for item in copy:
                    printlog("copying " + item)
                    copyfile(usb + "/" + item, storage + "/" + item)
                    printlog("done")
            #TODO: gpio lights
            os.system('sudo eject ' + usbDisk)
            printlog("Files Copied")
            time.sleep(10)
    except:
        pass
    time.sleep(60)

