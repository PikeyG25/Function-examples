from tkinter import *
from tkinter import font

root = Tk()
root.title("Lazy Buttons")
root.geometry("1920x1080")
root.configure(bg = "Red")

app = Frame(root)
app.grid()
app.configure(bg = "green")



bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.config(text = "don't click me")
bttn2.config(bg = "yellow")
bttn2.config(fg = "red")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"]= "Same here!"




















root.mainloop()