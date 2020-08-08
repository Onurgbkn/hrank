import tkinter
import tkinter.messagebox
import datetime
import time


nextBreak = (datetime.datetime.now().minute + 15) % 60

while True:
    if datetime.datetime.now().minute == nextBreak:
        tk = tkinter.Tk()
        tk.withdraw()
        tk.wm_attributes("-topmost", 1) 
        tk.focus()
        tkinter.messagebox.showerror('5 dk mola aq', "Break Time")
        nextBreak = (datetime.datetime.now().minute + 15) % 60
        tk.quit()

    time.sleep(1)
