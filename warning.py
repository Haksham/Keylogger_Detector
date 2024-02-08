import ctypes 
import webbrowser
def Mbox(title, text, style):
    res= ctypes.windll.user32.MessageBoxW(0, text, title, style)
    if res==1:   
      webbrowser.open('http://www.google.com/search?q=keylogger identification and anti-malware softwares')
    else:
        Mbox2('Confirmation ', 'Are you sure not to resolve this issue.', 33)
    return res
def Mbox2(title,text,style):
    res= ctypes.windll.user32.MessageBoxW(0, text, title, style)
    if res==1:
        return 0
    else:
        Mbox('Warning ', 'Keylogger symptoms are shown, plz look for an antivirus/antimalware to resolve this issue.', 49)
Mbox('Warning ', 'Keylogger symptoms are shown, plz look for an antivirus/antimalware to resolve this issue.', 49)