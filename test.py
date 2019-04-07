import subprocess
import os

def usbMovieFolder():
    usb = "/home/retr0"
    dirlist = os.listdir(usb)
    for item in dirlist:
        dirs = usb + "/" +item
        if os.path.isdir(dirs):
            if "movies" in os.listdir(dirs):
                movieDir = dirs + "/" + "movies"
                return movieDir
    return None
print(usbMovieFolder())
