import pynput
from pynput.keyboard import Key, Listener
import time
import threading
import ctypes 
import webbrowser
import sys;
key_is_pressed = False
startPressed = time.time()
key_pressed_list = []
key_released_list = []
c=0
a=0
out=0

def on_press(key):
    global key_is_pressed
    global startRelease
    global startPressed
    global a
    a+=1
    endPressed = time.time()
    miliSeconds = '%.1f' % ((endPressed-startPressed)*1000) 
    writeToFile(miliSeconds,"pressed.txt")
    key_pressed_list.append(miliSeconds + ", ")
    startPressed = time.time()
    if key_is_pressed == False:
        startRelease = time.time()
        key_is_pressed = True


def on_release(key):
    global key_is_pressed
    global endRelease
    global startRelease
    global c
    global out
    key_is_pressed = False
    endRelease = time.time()
    miliSeconds = '%.1f' % ((endRelease-startRelease)*1000)
    try:
      if key in [Key.media_volume_mute,Key.enter,Key.space]: 
        print(miliSeconds,': {0}'.format(key))
        c+=float(miliSeconds)
      elif key.char.isalnum():
        print(miliSeconds,': {0}'.format(key))
        c+=float(miliSeconds)
    except AttributeError:
        pass
    key_released_list.append(miliSeconds + ", ")
    if key == Key.esc:
        print("res= ",c)
        out=c/(a-1)
        print("total= ",out)
        if(out>150):
           return Mbox('Warning ', 'Keylogger symptoms are shown, plz look for an antivirus/antimalware to resolve this issue.', 49)
        else:
            return Mbox2('Result ', 'For now your system is safe from keylogger malwares', 0)

def writeToFile(tempList,filename):
    with open(filename, "a") as file:
        file.write("".join(tempList))

def Mbox(title, text, style):
    res= ctypes.windll.user32.MessageBoxW(0, text, title, style)
    if res==1:   
      webbrowser.open('http://www.google.com/search?q=keylogger identification and anti-malware softwares')
      quits()
    else:
        Mbox2('Confirmation ', 'Are you sure not to resolve this issue.', 33)
    return res
def Mbox2(title,text,style):
    res= ctypes.windll.user32.MessageBoxW(0, text, title, style)
    if res==1:
        quits()
        
    else:
        Mbox('Warning ', 'Keylogger symptoms are shown, plz look for an antivirus/antimalware to resolve this issue.', 49)

def quits():
    sys.exit(0)


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
