import tkinter as tk
import backbone as bk
import tkinter.font as font
import menuBarClassGUI as mb
import ShowcaseGUI as sc #Use bk.FUNCTION to call a function from background

#Main Frame, Window of the App
class MainAppGUI():
    def __init__(self, parent, resolution, appTitle):
        self.parent = parent

        self.parent.title(appTitle)
        self.parent.geometry(resolution)
        self.parent.configure(bg = "white")

        self.btnList = []
        self.imageList = []
        self.roomList = []
        self.btnFont

        self.initializeDictionaries()
        self.initializeRoomList()
        self.initializeFont()

        self.displayWindow = sc.dataWindowGUI(self.parent)
        self.menuBar = mb.MenuBarGUI(self.parent)

        self.menuBar.create_button(self.btnList[0], self.btnFont)
        self.menuBar.create_menu_button("Rooms", self.btnFont, self.roomList)
        self.menuBar.create_button(self.btnList[1], self.btnFont)

    def initializeDictionaries(self):
        self.btnList.append({"name": "Home", "commandPath": "displayImageHome", "alignment": "undefined"})
        self.btnList.append({"name": "Settings", "commandPath": "displayImageHome", "alignment": "bottom"})

    def initializeRoomList(self):
        self.roomList = ["Vlad's room", "Living room", "Kitchen"]

    def initializeImageList(self):
        self.imageList.append("resources\House_Icon.png")
        self.imageList.append("resources\Bed_Icon.png")
        self.imageList.append("resources\firePlace_Icon.png")
        self.imageList.append("resources\oven_Icon.jpg")

    def initializeFont(self):
        self.btnFont = font.Font(size = 15)

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