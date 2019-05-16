# Parker Gowans
# 3/19
# Movie Picker
from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,text = "Choose your favorite movie types").grid(row = 0, column = 0, sticky = W)
        # Create instruction label
        Label(self,text = "Select all that apply: "
              ).grid(row = 1, column = 0, sticky = W)

        # self.likes_comedy = BooleanVar()
        # Checkbutton(self,
        #             text = "Comedy",
        #             variable = self.likes_comedy,
        #             command = self.update_text).grid(row = 2, column = 0, sticky = W)
        #
        # self.likes_drama = BooleanVar()
        # Checkbutton(self,
        #             text="Drama",
        #             variable=self.likes_drama,
        #             command=self.update_text).grid(row=3, column=0, sticky=W)
        #
        # self.likes_romance = BooleanVar()
        # Checkbutton(self,
        #             text="Romance",
        #             variable=self.likes_romance,
        #             command=self.update_text).grid(row=4, column=0, sticky=W)
        self.favorite = StringVar()
        self.favorite.set(None)

        # Create Comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "comedy",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
        # Create radio romance button
        Radiobutton(self,
                    text="Romance",
                    variable=self.favorite,
                    value="romance",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)
        # Create radio Drama button
        Radiobutton(self,
                    text="Drama",
                    variable=self.favorite,
                    value="Drama",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)


        # Create text field to display results
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)

    def update_text(self):
        message = "Your favorite type of movie is "
        message += self.favorite.get()

        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0, message)





root = Tk()
root.title("")
root.geometry("400x300")
app = Application(root)

root.mainloop()