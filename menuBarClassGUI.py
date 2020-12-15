import tkinter as tk # Use tk.FUNCTION to call a function from tkinter
import backbone as bk #Use bk.FUNCTION to call a function from background
import ShowcaseGUI as sc #Use bk.FUNCTION to call a function from background

#Menu Bar Frame Added to the Main Frame
class MenuBarGUI():
    def __init__(self, parent):
        self.parent = tk.LabelFrame(parent)
        #self.parent.configure(bg = "white")
        self.configureFrame()
        self.parent.pack(fill = tk.Y, side = tk.LEFT, expand = False)
        self.buttonList = [] # All created buttons are part of this list
        self.btnCounter = 0 # count the elements in the button list (Not sure if necessary yet)
        self.menuButtonList = [] # All created menus are part of this list
        self.menBtnCounter = 0 # count the elements in the menu list (Not sure if necessary yet)

        self.displayWindow = sc.dataWindowGUI(parent)

    def configureFrame(self):
        self.parent["bg"] = "white"

    

    #Create a button with the given data
    def create_button(self, dataList, font):
        #Create the button and give its propeties
        self.buttonList.append(tk.Button(self.parent, text = dataList["name"], font = font))
        self.buttonList[self.btnCounter]["bd"] = 0 #border width
        self.buttonList[self.btnCounter]["bg"] = "white" #background color
        self.buttonList[self.btnCounter]["padx"] = 10 #padding on X axis (Horizontal)
        self.buttonList[self.btnCounter]["pady"] = 10 #padding on Y axis (Vertical)
        self.buttonList[self.btnCounter]["command"] = lambda : self.displayDataWindow(dataList["name"]) #trigger a function
        #Check if the function has an alignment option
        if "undefined" == dataList["alignment"]:
            self.buttonList[self.btnCounter].pack(fill = tk.X)
        elif "bottom" == dataList["alignment"]:
            self.buttonList[self.btnCounter].pack(fill = tk.X, side = dataList["alignment"])
        #Increase the Counter in case there will be more menus
        self.btnCounter += 1


    def create_menu_button(self, name, font, roomList):
        value = 0
        #The button that enables the Menu
        self.menuButtonList.append(tk.Menubutton(self.parent, text = name, font = font))
        self.menuButtonList[self.menBtnCounter]["bg"] = "white" #background color
        self.menuButtonList[self.menBtnCounter]["bd"] = 0 #border width
        self.menuButtonList[self.menBtnCounter]["padx"] = 10 #padding on X axis (Horizontal)
        self.menuButtonList[self.menBtnCounter]["pady"] = 10 #padding on Y axis (Vertical)
        self.menuButtonList[self.menBtnCounter]["activebackground"] = "lightgrey" #foreground color when button is selected
        #The List that appears once the button is pressed
        self.menuOptions = tk.Menu(self.menuButtonList[self.menBtnCounter])
        self.menuOptions["tearoff"] = 0
        self.menuOptions["bg"] = "white"
        self.menuOptions["font"] = font
        #Add elemnts to the menu list
        for x in roomList:
            self.menuOptions.add_radiobutton(label = x, value = value, command = lambda : self.displayDataWindow(x))
            value += 1
        #Put them all together with a nice red bow :))
        self.menuButtonList[self.menBtnCounter]["menu"] = self.menuOptions
        self.menuButtonList[self.menBtnCounter].pack(fill = tk.X)
        #Increase the Counter in case there will be more menus
        self.menBtnCounter += 1

    def displayDataWindow(self, name):
        return 0