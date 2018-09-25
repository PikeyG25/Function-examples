from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime
h = 0
m = 0
s = 0
t = 'AM'


def current_time(h,m,s,t):
    total_mil_sce = calendar.timegm(time.gmtime())* 1000
    total_sec = total_mil_sce // 1000
    cur_sec = total_sec % 60
    total_min = total_sec // 60
    cur_min = total_min % 60
    total_hrs = total_min // 60
    cur_hrs = total_hrs % 24


    #set the time zone
    cur_hrs = cur_hrs - 6
    if cur_hrs>=12:
        tag='PM'
    else:
        tag='AM'
    a = str(h)+":"+str(m)+":"+str(s)+t
        
    timex = str(cur_hrs)+":"+ str(cur_min)+":"+str(cur_sec)+tag
    if timex == a:
        beep()
    
    return timex
x=current_time(h,m,s,t)
print(x)

#winsound.Beep(540,8000)
def quit(*args):
    root.destroy()
    
def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)

def get_alarm(*args):
    global h
    h = input("set hour")
    global m
    m = input("set min")
    global s
    s = input("set sec")
    global t
    t = input("am or pm").upper()



root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='Green')
root.bind("x", quit)
root.bind("a",get_alarm)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='Yellow', background='red')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()




