from tkinter import * 
from tkinter.ttk import *

class View:

    def __init__(self, controller):
        #
        self.controller = controller
        return

    def display_options(self):
        optionsWindow = Tk()
        optionsWindow.title("MVC Demo")

        button1 = Button(optionsWindow, text = "Display alpha data",command = self.display_data_alpha)
        button1.pack(side = TOP)

        button2 = Button(optionsWindow, text = "Display beta data",command = self.display_data_beta)
        button2.pack(side = TOP)

        optionsWindow.mainloop()
        return

    def display_data_alpha(self):
        displayWindow = Tk()
        displayWindow.title("Display Alpha Data")
        data = self.controller.get_data_alpha()
        label = Label(displayWindow, text = data)
        label.pack()
        displayWindow.mainloop()
        return

    def display_data_beta(self):
        displayWindow = Tk()
        displayWindow.title("Display Beta Data")
        data = self.controller.get_data_beta()
        label = Label(displayWindow, text = data)
        label.pack()
        displayWindow.mainloop()
        return
