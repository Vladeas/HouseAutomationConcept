from tkinter import *

#Menu Bar Frame Added to the Main Frame
class MenuBarGUI():
    def __init__(self, parent):
        self.parent = parent
        self.homeButton = Button(self.actionBar, text = "Home")

#Main Frame, Window of the App
class MainAppGUI():
    def __init__(self, parent, resolution, appTitle):
        self.parent = parent

        self.parent.title(appTitle)
        self.parent.geometry(resolution)


    def _create_action_bar():
        self.actionBar = LabelFrame(self.parent)
        self.settingsButton = Button(self.actionBar, text = "Settings")
        self.helpButton = Button(self.actionBar, text = "Help")
        
        self.actionBar.grid(row = 0, column = 0)
        self.settingsButton.grid(row = 0, column = 0)
        self.helpButton.grid(row = 0, column = 1)

#Get the resolution of the current device screen
#Return it in a format to be used witk tkinter
def _get_screen_resolution(parent):
    width = parent.winfo_screenwidth()
    height = parent.winfo_screenheight()
    return str(width) + "x" + str(height) 

#Main Function of the GUI -->> Here it starts
#Needs to be called to Create the GUI
def start_GUI():
    root = Tk()

    resolution = _get_screen_resolution(root)
    appTitle = "Home Hub"

    app = MainAppGUI(root, resolution, appTitle)

    root.mainloop()