import tkinter as tk
import backbone as bk  #Use bk.FUNCTION to call a function from background
import tkinter.font as font
import menuBarClassGUI as mb
import ShowcaseGUI as sc

#Main Frame, Window of the App
class MainAppGUI():
    def __init__(self, parent, backBoneObj, resolution, appTitle):
        self.parent = parent
        self.serialRead_Home = backBoneObj
        self.parent.title(appTitle)
        self.parent.geometry(resolution)
        self.parent.configure(bg = "white")

        self.menuBar = mb.MenuBarGUI(self.parent)
        self.displayWindow = sc.dataWindowGUI(self.parent, self.serialRead_Home)

    def close(self):
        self.displayWindow.close()

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

    
    serialRead_Home = bk.serialRead(9600, "COM4")

    app = MainAppGUI(root, serialRead_Home, resolution, appTitle)

    root.mainloop()

    app.close()
    serialRead_Home.close()