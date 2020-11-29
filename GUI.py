from tkinter import *

class MainAppGUI():
    def __init__(self, parent):
        self.parent = parent
        
        self.parent.title("Home Hub")
        self.parent.geometry("1600x900")
        _create_action_bar()

    def _create_action_bar():
        self.actionBar = LabelFrame(self.parent)
        self.settingsButton = Button(self.actionBar, text = "Settings")
        self.helpButton = Button(self.actionBar, text = "Help")
        
        self.actionBar.grid(row = 0, column = 0)
        self.settingsButton.grid(row = 0, column = 0)
        self.helpButton.grid(row = 0, column = 1)

def start_GUI():
    root = Tk()

    app = MainAppGUI(root)

    root.mainloop()