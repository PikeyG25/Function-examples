from tkinter import *

class Application(Frame):
    """ GUI application which counts button clicks """
    def __init__(self, master):
        """ Initialize the Frame."""
        super(Application, self).__init__(master)
        self.clicks = 0
        self.grid()
        self.create_widget()
    def create_widget(self):
        """ Create button which displays number of clicks. """
        self.lbl = Label(text = "Calculator program").grid(row = 0, column = 1)
        self.lbl2 = Label(text = str(self.clicks))
        self.lbl2.grid()
        self.bttn = Button(self)
        self.bttn["text"]= "+"
        self.bttn["command"] = self.add_to_count
        self.bttn.grid()
        self.bttn2 = Button(self)
        self.bttn2["text"]= "-"
        self.bttn2.grid()
        self.bttn3 = Button(self)
        self.bttn3["text"]= "*"
        self.bttn3.grid()
        self.bttn4 = Button(self)
        self.bttn4["text"]= "/"
        self.bttn4.grid()
    def add_to_count(self):
        self.clicks += 1
        self.lbl2["text"] = str(self.clicks)








root = Tk()
root.title("")
root.geometry("300x150")
app = Application(root)

root.mainloop()