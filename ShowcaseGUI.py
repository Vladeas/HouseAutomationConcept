import tkinter as tk # Use tk.FUNCTION to call a function from tkinter
import backbone as bk #Use bk.FUNCTION to call a function from background
from PIL import Image, ImageTk

class dataWindowGUI():
    def __init__(self, parent):
        self.parent = tk.LabelFrame(parent) # The label is the new parent
        self.configureFrame()
        self.parent.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
        self.source

    def temperatureNumberData(self):
        self.tempOneBox = tk.LabelFrame(self.parent)

    def createButton(self):
        

    def configureFrame(self):
        self.parent["bg"] = "blue"

    def displayImageHome(self, path):
        self.addImageToList(path)
        self.myImg = ImageTk.PhotoImage(Image.open(path))
        self.imageLabel = tk.Label(self.parent, image = self.myImg)
        self.imageLabel.grid(row = 0, column = 0, sticky = "nsew")

    def addImageToList(self, path):
        self.imageList.append(path)