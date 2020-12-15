import tkinter as tk # Use tk.FUNCTION to call a function from tkinter
import backbone as bk #Use bk.FUNCTION to call a function from background
import ShowcaseGUI as sc #Use bk.FUNCTION to call a function from background
import tkinter.font as font

#Menu Bar Frame Added to the Main Frame
class MenuBarGUI():
    def __init__(self, parent):
        self.parent = tk.LabelFrame(parent) # The label is the new parent
        self.configureMainFrame()

        self.textFont = font.Font(size = 15)

        # Buttons
        self.homeButton = tk.Button(self.parent, text = "Home")
        self.configureButton()

        # Button Menu
        self.roomsButtonMenu = tk.Menubutton(self.parent, text = "Rooms")
        self.configureButtonMenu()


#configure the main Frame
    def configureMainFrame(self):
        self.parent["bg"] = "white"
        self.parent.pack(fill = tk.Y, side = tk.LEFT, expand = False)


    def configureButton(self):
        self.homeButton.config(font = self.textFont, bg = "white", bd = 0, padx = 10, pady = 10)
        self.homeButton.pack(fill = tk.X)
    
    def configureButtonMenu(self):
        self.roomsButtonMenu.config(font = self.textFont, bg = "white", bd = 0, padx = 10, pady = 10, activebackground = "lightgrey")
        self.roomsButtonMenu.menu = tk.Menu(self.roomsButtonMenu)
        self.roomsButtonMenu.menu.config(tearoff = 0, bg = "white", font = self.textFont)
        self.roomsButtonMenu.menu.add_radiobutton(label = "Vlad's room", value = 1)
        self.roomsButtonMenu.menu.add_radiobutton(label = "Kitchen room", value = 2)
        self.roomsButtonMenu.menu.add_radiobutton(label = "Bathroom room", value = 3)
        self.roomsButtonMenu.menu.add_radiobutton(label = "Living room", value = 4)
        self.roomsButtonMenu["menu"] = self.roomsButtonMenu.menu
        self.roomsButtonMenu.pack(fill = tk.X)
    
    def close(self):
        return 0