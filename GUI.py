import tkinter as tk
from backbone import test1, test2
import tkinter.font as font
from menuBarClassGUI import *

#Fram for showing informations and data
class DisplayFrameGUI():
    def __init__(self, parent):
        self.parent = tk.LabelFrame(parent)
        self.parent.pack(fill = tk.BOTH)


#Main Frame, Window of the App
class MainAppGUI():
    def __init__(self, parent, resolution, appTitle):
        self.parent = parent

        self.parent.title(appTitle)
        self.parent.geometry(resolution)
        self.parent.configure(bg = "white")
        
        self.btnFont = font.Font(size = 15)

        self.roomList = ["Vlad's room", "Living room", "Kitchen"]

        self.menuBar = MenuBarGUI(self.parent)
        self.menuBar.create_button("Home", self.btnFont, "test1", "undefined")
        self.menuBar.create_menu_button("Rooms", self.btnFont, self.roomList)
        self.menuBar.create_button("Settings", self.btnFont, "test1", "bottom")

        self.displayFrame = DisplayFrameGUI(self.parent)


#Get the resolution of the current device screen
#Return it in a format to be used witk tkinter
def _get_screen_resolution(parent):
    width = parent.winfo_screenwidth()
    height = parent.winfo_screenheight()
    return str(width - 100) + "x" + str(height - 100) 


#Main Function of the GUI -->> Here it starts
#Needs to be called to Create the GUI
def start_GUI():
    root = tk.Tk()

    print("app start")

    resolution = _get_screen_resolution(root)
    appTitle = "Home Hub"

    app = MainAppGUI(root, resolution, appTitle)

    root.mainloop()