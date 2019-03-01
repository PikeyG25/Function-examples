#Parker Gowans
#Simple Gui
#3/19

from tkinter import *

# Create the root window
root = Tk()
#Modify the window
root.title("Simple GUI")
root.geometry("1920x1080")
root.configure(bg = "aqua")
root.iconbitmap("mushroom")
root.attributes('-alpha','.5')
app = Frame(root)
app.grid()

#Create a label inside the frame
label = Label(app,text = "this is a fancy Label", fg= "red", font = ("Times New Roman","70"))
lbl = Label(app, text = "I'm a label!")
lbl3 = Label(app, text = "This is another label")
label.grid()
lbl.grid()
lbl3.grid()



#Kick off the window's event-loop
root.mainloop()