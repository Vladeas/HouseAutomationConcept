import sqlite3
from sqlite3 import Error

class sqlLiteDataBase:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.createConnection()

        self.createTable()

    def createConnection(self):
        try:
            self.connection = sqlite3.connect("homeData.db")
        except Error as e:
            print(e)
        finally:
            if self.connection:
                self.connection.close()

    def createTable(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS houseData (
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            airQuality REAL NOT NULL,
            luminosityVal REAL NOT NULL,
            luminosityRatio REAL NOT NULL
        )""")

        self.connection.commit()
        self.connection.close()

    def insertData(self, temperature, humidity, airQuality, luminosityVal, luminosityRatio):
        print("Data Saved !")
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO houseData VALUES(?,?,?,?,?)", [temperature, humidity, airQuality, luminosityVal, luminosityRatio])
        self.connection.commit()
        self.connection.close()


#Max Values for different Data
    def getMaxTemperature(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY temperature DESC")
        val = self.cursor.fetchone()[0]
        self.connection.commit()
        self.connection.close()
        return val

    def getMaxHumidity(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY humidity DESC")
        val = self.cursor.fetchone()[1]
        self.connection.commit()
        self.connection.close()
        return val

    def getWorstAirQuality(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY airQuality DESC")
        val = self.cursor.fetchone()[2]
        self.connection.commit()
        self.connection.close()
        return val

    def getMaxLuminosity(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY luminosityVal DESC")
        val = self.cursor.fetchone()[3]
        self.connection.commit()
        self.connection.close()
        return val

    def getMaxLuminosityR(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY luminosityRatio DESC")
        val = self.cursor.fetchone()[4]
        self.connection.commit()
        self.connection.close()
        return val
        

#Min Values for different Data
    def getMinTemperature(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY temperature")
        val = self.cursor.fetchone()[0]
        self.connection.commit()
        self.connection.close()
        return val
        

    def getMinHumidity(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY humidity")
        val =  self.cursor.fetchone()[1]
        self.connection.commit()
        self.connection.close()
        return val

    def getBestAirQuality(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY airQuality")
        val = self.cursor.fetchone()[2]
        self.connection.commit()
        self.connection.close()
        return val

    def getMinLuminosity(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY luminosityVal")
        val = self.cursor.fetchone()[3]
        self.connection.commit()
        self.connection.close()
        return val

    def getMinLuminosityR(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData ORDER BY luminosityRatio")
        print(self.cursor.fetchone()[4])
        val = self.cursor.fetchone()[4]
        self.connection.commit()
        self.connection.close()
        return val

#return full data
    def fetchAllData(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData")
        allDataHere = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return allDataHere

    def fetchLast(self):
        self.connection = sqlite3.connect("homeData.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM houseData")
        allDataHere = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        for data in allDataHere:
            pass
        return data