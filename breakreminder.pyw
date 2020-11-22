import tkinter
import tkinter.messagebox
import datetime
import time


nextBreak = (datetime.datetime.now().minute + 20) % 60

while True:
    if datetime.datetime.now().minute == nextBreak:
        tk = tkinter.Tk()
        tk.withdraw()
        tk.wm_attributes("-topmost", 1) 
        tk.focus()
        MsgBox = tkinter.messagebox.askquestion('5 dk mola', "Break Time")
        if MsgBox == 'yes':
            nextBreak = (datetime.datetime.now().minute + 20) % 60
        else:
            break

        tk.quit()

    time.sleep(1)
