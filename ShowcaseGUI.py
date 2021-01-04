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
        self.temperatureDataWin = tk.LabelFrame(self.parent)
        self.humidityDataWin = tk.LabelFrame(self.parent)
        self.airQualityDataWin = tk.LabelFrame(self.parent)
        self.luminosityDataWin = tk.LabelFrame(self.parent)
        self.toBeSeenWin = tk.LabelFrame(self.parent)
        self.graphDataWin = tk.LabelFrame(self.parent)
        self.configureSecondaryFrame()

        self.textFont = font.Font(size = 15)

        #items within the temperature Data frame
        self.currentTemperatureTextLabel = tk.Label(self.temperatureDataWin, text = "Current Temperature : ")
        self.maxTemperatureTextLabel = tk.Label(self.temperatureDataWin, text = "Max Temperature : ")
        self.averageTemperatureTextLabel = tk.Label(self.temperatureDataWin, text = "Average Temperature : ")
        self.minTemperatureTextLabel = tk.Label(self.temperatureDataWin, text = "Min Temperature : ")

        self.currentTemperatureDataLabel = tk.Label(self.temperatureDataWin, text = "420 C")
        self.maxTemperatureDataLabel = tk.Label(self.temperatureDataWin, text = "420 C")
        self.averageTemperatureDataLabel = tk.Label(self.temperatureDataWin, text = "420 C")
        self.minTemperatureDataLabel = tk.Label(self.temperatureDataWin, text = "420 C")

        self.configureTemperatureData()

        #items within the humidity Data frame
        self.currentHumidityTextLabel = tk.Label(self.humidityDataWin, text = "Current Humidity Level : ")
        self.highHumidityTextLabel = tk.Label(self.humidityDataWin, text = "Highest Humidity Level : ")
        self.averageHumidityTextLabel = tk.Label(self.humidityDataWin, text = "Average Humidity Level : ")
        self.lowHumidityTextLabel = tk.Label(self.humidityDataWin, text = "Lowest Humidity Level : ")

        self.currentHumidityDataLabel = tk.Label(self.humidityDataWin, text = "50 %")
        self.highHumidityDataLabel = tk.Label(self.humidityDataWin, text = "50 %")
        self.averageHumidityDataLabel = tk.Label(self.humidityDataWin, text = "50 %")
        self.lowHumidityDataLabel = tk.Label(self.humidityDataWin, text = "50 %")

        self.configureHumidityData()

        #items within the air quality data frame
        self.currentAirQualityTextLabel = tk.Label(self.airQualityDataWin, text = "Current Air Qlt : ")
        self.worstAirQualityTextLabel = tk.Label(self.airQualityDataWin, text = "Worst Air Qlt : ")
        self.averageAirQualityTextLabel = tk.Label(self.airQualityDataWin, text = "Average Air Qlt : ")
        self.bestAirQualityTextLabel = tk.Label(self.airQualityDataWin, text = "Best Air Qlt : ")

        self.currentAirQualityDataLabel = tk.Label(self.airQualityDataWin, text = "420 PPM")
        self.worstAirQualityDataLabel = tk.Label(self.airQualityDataWin, text = "420 PPM")
        self.averageAirQualityDataLabel = tk.Label(self.airQualityDataWin, text = "420 PPM")
        self.bestAirQualityDataLabel = tk.Label(self.airQualityDataWin, text = "420 PPM")

        self.configureAirQualityData()

        #items within the light data frame
        self.currentLuminosityTextLabel = tk.Label(self.luminosityDataWin, text = "Luminosity value : ")
        self.currentLuminosityRatioTextLabel = tk.Label(self.luminosityDataWin, text = "Luminosity ratio : ")

        self.currentLuminosityDataLabel = tk.Label(self.luminosityDataWin, text = "420 LUX")
        self.currentLuminosityRatioDataLabel = tk.Label(self.luminosityDataWin, text = " 15 %")

        self.configureLuminosityData()

        #VALUES
        self.currentTemperatureVal = None
        self.currentHumidityVal = None
        self.currentAirQualityVal = None
        self.currentLuminosityVal = None
        self.currentLuminosityRatioVal = None
        self.refreshValues()
        #items within the realTimeData frame
        


#configure the main Frame
    def configureMainFrame(self):
        self.parent["bg"] = "blue"
        self.parent.pack(fill = tk.BOTH, side = tk.RIGHT, expand = True)
        self.parent.columnconfigure(0, weight = 1)
        self.parent.columnconfigure(1, weight = 1)
        self.parent.columnconfigure(2, weight = 1)
        self.parent.columnconfigure(3, weight = 1)
        self.parent.rowconfigure(0, weight = 1)
        self.parent.rowconfigure(1, weight = 2)

#configure all the frames within the main Frame
    def configureSecondaryFrame(self):
        #temperature frame config
        self.temperatureDataWin.configure(bg = "white")
        self.temperatureDataWin.grid(row = 0, column = 0, sticky = "nsew")
        #temperature frame config
        self.humidityDataWin.configure(bg = "white")
        self.humidityDataWin.grid(row = 0, column = 1, sticky = "nsew")
        #air quality frame config
        self.airQualityDataWin.config(bg = "white")
        self.airQualityDataWin.grid(row = 0, column = 2, sticky = "nsew")
        #light frame config
        self.luminosityDataWin.config(bg = "white")
        self.luminosityDataWin.grid(row = 0, column = 3, sticky = "nsew")
        #other frames
        self.toBeSeenWin.grid(row = 0, column = 1)
        self.graphDataWin.grid(row = 1, columnspan = 2)

#configure all the elements within the real time Frame
    def configureHumidityData(self):
        #config items in temperature frame
        self.currentHumidityTextLabel.config(font = self.textFont, bg = "white")
        self.currentHumidityDataLabel.config(font = self.textFont, bg = "white")
        self.highHumidityTextLabel.config(font = self.textFont, bg = "white")
        self.highHumidityDataLabel.config(font = self.textFont, bg = "white")
        self.averageHumidityTextLabel.config(font = self.textFont, bg = "white")
        self.averageHumidityDataLabel.config(font = self.textFont, bg = "white")
        self.lowHumidityTextLabel.config(font = self.textFont, bg = "white")
        self.lowHumidityDataLabel.config(font = self.textFont, bg = "white")
        #pack the items in the frame within a grid
        self.currentHumidityTextLabel.grid(row = 0, column = 0)
        self.currentHumidityDataLabel.grid(row = 0, column = 1)
        self.highHumidityTextLabel.grid(row = 1, column = 0)
        self.highHumidityDataLabel.grid(row = 1, column = 1)
        self.averageHumidityTextLabel.grid(row = 2, column = 0)
        self.averageHumidityDataLabel.grid(row = 2, column = 1)
        self.lowHumidityTextLabel.grid(row = 3, column = 0)
        self.lowHumidityDataLabel.grid(row = 3, column = 1)

#configure all the elements within the real time Frame
    def configureTemperatureData(self):
        #config items in temperature frame
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

#configure all the elements within the real time Frame
    def configureAirQualityData(self):
        #config items in air quality frame
        self.currentAirQualityTextLabel.config(font = self.textFont, bg = "white")
        self.currentAirQualityDataLabel.config(font = self.textFont, bg = "white")
        self.worstAirQualityTextLabel.config(font = self.textFont, bg = "white")
        self.worstAirQualityDataLabel.config(font = self.textFont, bg = "white")
        self.averageAirQualityTextLabel.config(font = self.textFont, bg = "white")
        self.averageAirQualityDataLabel.config(font = self.textFont, bg = "white")
        self.bestAirQualityTextLabel.config(font = self.textFont, bg = "white")
        self.bestAirQualityDataLabel.config(font = self.textFont, bg = "white")
        #pack the items in the frame within a grid
        self.currentAirQualityTextLabel.grid(row = 0, column = 0)
        self.currentAirQualityDataLabel.grid(row = 0, column = 1)
        self.worstAirQualityTextLabel.grid(row = 1, column = 0)
        self.worstAirQualityDataLabel.grid(row = 1, column = 1)
        self.averageAirQualityTextLabel.grid(row = 2, column = 0)
        self.averageAirQualityDataLabel.grid(row = 2, column = 1)
        self.bestAirQualityTextLabel.grid(row = 3, column = 0)
        self.bestAirQualityDataLabel.grid(row = 3, column = 1)

#configure all the elements within the real time Frame
    def configureLuminosityData(self):
        #config items in luminosity frame
        self.currentLuminosityTextLabel.config(font = self.textFont, bg = "white")
        self.currentLuminosityDataLabel.config(font = self.textFont, bg = "white")
        self.currentLuminosityRatioTextLabel.config(font = self.textFont, bg = "white")
        self.currentLuminosityRatioDataLabel.config(font = self.textFont, bg = "white")
        #pack the items in the frame within a grid
        self.currentLuminosityTextLabel.grid(row = 0, column = 0)
        self.currentLuminosityDataLabel.grid(row = 0, column = 1)
        self.currentLuminosityRatioTextLabel.grid(row = 1, column = 0)
        self.currentLuminosityRatioDataLabel.grid(row = 1, column = 1)

    def refreshValues(self):
        self.currentTemperatureVal = self.serialRead_Home.getCurrentTemperature()
        self.currentTemperatureDataLabel["text"] = self.currentTemperatureVal + " C "
        self.currentHumidityVal = self.serialRead_Home.getCurrentHumidity()
        self.currentHumidityDataLabel["text"] = self.currentHumidityVal + " % "
        self.currentAirQualityVal = self.serialRead_Home.getCurrentAirQuality()
        self.currentAirQualityDataLabel["text"] = self.currentAirQualityVal + " PPM "
        self.currentLuminosityVal = self.serialRead_Home.getCurrentLuminosity()
        self.currentLuminosityDataLabel["text"] = self.currentLuminosityVal + " LUX "
        self.currentLuminosityRatioVal = self.serialRead_Home.getCurrentLuminosityRatio()
        self.currentLuminosityRatioDataLabel["text"] = self.currentLuminosityRatioVal + " % "
        self.parent.after(2000, self.refreshValues)

#Close the Thread
    def close(self):
        print("Shutting Down...")