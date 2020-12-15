import tkinter as tk # Use tk.FUNCTION to call a function from tkinter
import backbone as bk #Use bk.FUNCTION to call a function from background
import tkinter.font as font #Use font.Function to access a function from font library
import time
from PIL import Image, ImageTk

class dataWindowGUI():
    def __init__(self, parent, backBoneObj):
        self.parent = tk.LabelFrame(parent) # The label is the new parent
        self.configureMainFrame()
        self.serialRead_Home = backBoneObj
        #separate the data into labels
        self.realTimeDataWin = tk.LabelFrame(self.parent)
        self.toBeSeenWin = tk.LabelFrame(self.parent)
        self.graphDataWin = tk.LabelFrame(self.parent)
        self.configureSecondaryFrame()

        self.textFont = font.Font(size = 15)

        #items within the realTimeData frame
        self.currentTemperatureTextLabel = tk.Label(self.realTimeDataWin, text = "Current Temperature : ")
        self.maxTemperatureTextLabel = tk.Label(self.realTimeDataWin, text = "Max Temperature : ")
        self.averageTemperatureTextLabel = tk.Label(self.realTimeDataWin, text = "Average Temperature : ")
        self.minTemperatureTextLabel = tk.Label(self.realTimeDataWin, text = "Min Temperature : ")

        self.currentTemperatureDataLabel = tk.Label(self.realTimeDataWin, text = "420 C")
        self.maxTemperatureDataLabel = tk.Label(self.realTimeDataWin, text = "420 C")
        self.averageTemperatureDataLabel = tk.Label(self.realTimeDataWin, text = "420 C")
        self.minTemperatureDataLabel = tk.Label(self.realTimeDataWin, text = "420 C")

        self.configureRealTimeData()

        #VALUES
        self.currentTemperatureVal = None
        self.currentHumidityVal = None
        self.currentAirQualityVal = None
        self.currentLuminosity = None
        self.refreshValues()
        #items within the realTimeData frame
        


#configure the main Frame
    def configureMainFrame(self):
        self.parent["bg"] = "blue"
        self.parent.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)

#configure all the frames within the main Frame
    def configureSecondaryFrame(self):
        self.realTimeDataWin.configure(bg = "white")
        self.realTimeDataWin.grid(row = 0, column = 0)
        self.toBeSeenWin.grid(row = 0, column = 1)
        self.graphDataWin.grid(row = 1, columnspan = 2)

#configure all the elements within the real time Frame
    def configureRealTimeData(self):
        self.currentTemperatureTextLabel.config(font = self.textFont, bg = "white")
        self.currentTemperatureDataLabel.config(font = self.textFont, bg = "white")
        self.maxTemperatureTextLabel.config(font = self.textFont, bg = "white")
        self.maxTemperatureDataLabel.config(font = self.textFont, bg = "white")
        self.averageTemperatureTextLabel.config(font = self.textFont, bg = "white")
        self.averageTemperatureDataLabel.config(font = self.textFont, bg = "white")
        self.minTemperatureTextLabel.config(font = self.textFont, bg = "white")
        self.minTemperatureDataLabel.config(font = self.textFont, bg = "white")
        #pack the items in the frame within a grid
        self.currentTemperatureTextLabel.grid(row = 0, column = 0)
        self.currentTemperatureDataLabel.grid(row = 0, column = 1)
        self.maxTemperatureTextLabel.grid(row = 1, column = 0)
        self.maxTemperatureDataLabel.grid(row = 1, column = 1)
        self.averageTemperatureTextLabel.grid(row = 2, column = 0)
        self.averageTemperatureDataLabel.grid(row = 2, column = 1)
        self.minTemperatureTextLabel.grid(row = 3, column = 0)
        self.minTemperatureDataLabel.grid(row = 3, column = 1)

    def refreshValues(self):
        self.currentTemperatureVal = self.serialRead_Home.getCurrentTemperature()
        self.currentTemperatureDataLabel["text"] = self.currentTemperatureVal + " C "
        self.parent.after(2000, self.refreshValues)

#Close the Thread
    def close(self):
        print("Shutting Down...")