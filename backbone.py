from threading import Thread
import serial
import time
import dataBaseClass as db

class serialRead:
    def __init__(self, serialBaud = 9600, serialPort = "COM5"):
        #Strings
        self.noDataAvailable = "No Data Available"

        #Neded variables
        self.dbConnection = db.sqlLiteDataBase()
        self.serialBaud = serialBaud
        self.serialPort = serialPort
        self.thread = None
        self.isRun = True
        self.isReceiving = False
        self.rawData = 0
        self.rawDataSplit = 0
        self.refinedData = []

        #Connect to the arduino Board
        print('Trying to connect to: ' + str(self.serialPort) + ' at ' + str(self.serialBaud) + ' BAUD.')
        try:
            self.serialConnection = serial.Serial(self.serialPort, self.serialBaud, timeout=4)
            print('Connected to ' + str(self.serialPort) + ' at ' + str(self.serialBaud) + ' BAUD.')
            self.readSerialStart()
        except:
            print("Failed to connect with " + str(self.serialPort) + ' at ' + str(self.serialBaud) + ' BAUD.')


#Start a thread for reading the data from the arduino
    def readSerialStart(self):
        if self.thread == None:
            self.thread = Thread(target=self.backgroundThread)
            self.thread.start()
            # Block untill we start receiving values
            while self.isReceiving != True:
                time.sleep(0.1)

#Retrive the data from the arduino
    def backgroundThread(self):    # retrieve data
        #try:
            time.sleep(1.0)  # give some buffer time for retrieving data
            self.serialConnection.reset_input_buffer()
            while (self.isRun):
                    if self.serialConnection.in_waiting > 0:
                        self.rawData = self.serialConnection.readline()
                        self.isReceiving = True
                        self.processReceivedData()
                        #print(self.rawData)
        #except:
            #print("Interrupted Serial Connection")
            #self.rawDataSplit = 0

#Transform the received string in usable data
    def processReceivedData(self):
        self.rawDataSplit = self.rawData.decode().split('_') # The "_" elemnt divides the transmited values
        #print(self.rawDataSplit)
        self.refinedData.append({"humidity": self.rawDataSplit[1], "temperature": self.rawDataSplit[2], "air_quality": self.rawDataSplit[3], "lux": self.rawDataSplit[4], "lux_ratio": self.rawDataSplit[5]})

#send Data to teh dataBase
    def sendDataToDB(self):
        print("Impulse received !")
        self.dbConnection.insertData(self.rawDataSplit[2], self.rawDataSplit[1], self.rawDataSplit[3], self.rawDataSplit[4], self.rawDataSplit[5])

#Close the Thread
    def close(self):
        try:
            self.isRun = False
            self.thread.join()
            self.serialConnection.close()
        except:
            print("No thread to close...")
        print('Disconnected...')

#GET METHODS
#Current Values
    def getCurrentTemperature(self):
        if self.rawDataSplit == 0:
            return self.noDataAvailable
        return self.rawDataSplit[2]

    def getCurrentHumidity(self):
        if self.rawDataSplit == 0:
            return self.noDataAvailable
        return self.rawDataSplit[1]

    def getCurrentAirQuality(self):
        if self.rawDataSplit == 0:
            return self.noDataAvailable
        return self.rawDataSplit[3]

    def getCurrentLuminosity(self):
        if self.rawDataSplit == 0:
            return self.noDataAvailable
        return self.rawDataSplit[4]

    def getCurrentLuminosityRatio(self):
        if self.rawDataSplit == 0:
            return self.noDataAvailable
        return self.rawDataSplit[5]

#GET METHODS
#Max Values
    def getMaxTemperature(self):
        return self.dbConnection.getMaxTemperature()
    def getMaxHumidity(self):
        return self.dbConnection.getMaxHumidity()
    def getWorstAirQuality(self):
        return self.dbConnection.getWorstAirQuality()
    def getMaxLuminosity(self):
        return self.dbConnection.getMaxLuminosity()
    def getMaxLuminosityR(self):
        return self.dbConnection.getMaxLuminosityR()

#GET METHODS
#Min Values
    def getMinTemperature(self):
        return self.dbConnection.getMinTemperature()
    def getMinHumidity(self):
        return self.dbConnection.getMinHumidity()
    def getBestAirQuality(self):
        return self.dbConnection.getBestAirQuality()
    def getMinLuminosity(self):
        return self.dbConnection.getMinLuminosity()
    def getMinLuminosityR(self):
        return self.dbConnection.getMinLuminosityR()

#GET METHODS
#All data
    def getAllData(self):
        return self.dbConnection.fetchAllData()

    def getLastEntry(self):
        return self.dbConnection.fetchLast()

#Average values
    def averageTemperature(self):
        dataList = self.getAllData()
        sum = 0
        for data in dataList:
            sum += data[0]
        return round(sum/len(dataList),2)

    def averageHumidity(self):
        dataList = self.getAllData()
        sum = 0
        for data in dataList:
            sum += data[1]
        return round(sum/len(dataList),2)

    def averageAirQlt(self):
        dataList = self.getAllData()
        sum = 0
        for data in dataList:
            sum += data[2]
        return round(sum/len(dataList),2)