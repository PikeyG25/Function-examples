from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn1 = Button(self, text="I do nothing!")
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.config(text="don't click me")
        self.bttn2.config(bg="yellow")
        self.bttn2.config(fg="red")

        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "Same here!"
        self.bttn3["bg"] = "blue"
        self.bttn3["fg"] = "green"































root = Tk()
root.title("Lazy Buttons")
root.geometry("1920x1080")
app = Application(root)

root.mainloop()