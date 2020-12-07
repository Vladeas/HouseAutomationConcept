import tkinter as tk # Use tk.FUNCTION to call a function from tkinter
import backbone as bk #Use bk.FUNCTION to call a function from background
from PIL import Image, ImageTk

class dataWindowGUI():
    def __init__(self, parent):
        self.parent = tk.LabelFrame(parent)
        self.configureFrame()
        self.parent.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)

    def configureFrame(self):
        self.parent["bg"] = "blue"

    def displayImageHome(self, path):
        self.myImg = ImageTk.PhotoImage(Image.open(path))
        self.imageLabel = tk.Label(self.parent, image = self.myImg)
        self.imageLabel.grid(row = 0, column = 0, sticky = "nsew")