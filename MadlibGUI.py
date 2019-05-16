# Parker Gowans
# 3/19
# Madlib

from tkinter import *


class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(text = "Madlibs Program").grid(row = 0, column = 0, columnspan = 2)
        Label(text = "Person").grid(row = 1, column = 0, sticky = W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        self.pluralnoun = Entry(self).grid(row = 2, column = 2, sticky = W)





root = Tk()
root.title("")
root.geometry("400x300")
app = Application(root)

root.mainloop()