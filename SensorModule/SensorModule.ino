//Libraries
#include <DHT.h>

//Constants
#define DHTPIN 2     // pin for the digital input from the DHT22 sensor
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
#define MQ135DPIN 3 // pin for the digital input from MQ-135 sensor
#define MQ135APIN 0 // pin for the analog input from MQ-135 sensor
#define LIGTHSENSORPIN 1 // pin for the analog input from the temt6000 sensor

//Variables temperature sensor
float humidity;
float temperature;

//Variables air quality sensor
float analog_airQualityPPM;
float digital_airQualityTreshold;

//Variables light sensor
float ambientalLightReading;
float luminosityRatio;

//Variables Loop
int timeDelay = 2000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  //Temperature code segment DHT22
  temperatureSensor();
  //Air quality code segment MQ135
  airQualitySensor();
  //Ambiental Light Sensor code segment temt 6000
  ambientalLightSensor();
  //Method for printing the results
  //printResults();
  //Method for comunicating with the pc
  writeResults();
  //Delay before the next loop
  delay(timeDelay);
}

//Temperature code segment DHT22
void temperatureSensor()
{
    humidity = dht.readHumidity();
    temperature = dht.readTemperature();
}

//Air quality code segment MQ135
void airQualitySensor()
{
  analog_airQualityPPM = analogRead(MQ135APIN);
  digital_airQualityTreshold = digitalRead(MQ135DPIN);
}

//Ambiental Light Sensor code segment temt 6000
void ambientalLightSensor()
{
  ambientalLightReading = analogRead(LIGTHSENSORPIN);
  luminosityRatio = (ambientalLightReading / 1023.0) * 100.0;
}

//Print the sensor outputs on the screen
void printResults()
{
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %, Temp: ");
  Serial.print(temperature);
  Serial.println(" Celsius");
  Serial.print("Air Quality : ");
  Serial.println(analog_airQualityPPM);
  Serial.print("Ambiental Ligth : ");
  Serial.print(ambientalLightReading);
  Serial.print(" , Percentage : ");
  Serial.print(luminosityRatio);
  Serial.println(" % ");
  Serial.println("==========");
}

void writeResults()
{
  String message = "_" + String(humidity) + "_" + temperature + "_" + analog_airQualityPPM + "_" + ambientalLightReading + "_" + luminosityRatio + "_";
  Serial.println(message);
}
