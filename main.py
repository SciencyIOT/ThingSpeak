from PicoSensor import Temperature
from WiFiNetwork import WiFi
from ThingSpeak import ThingSpeakApi
from time import sleep

#Sensor Initialization
sensor = Temperature()

#ThingSpeak Initialization
thingspeak = ThingSpeakApi()

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()

#Main Program
while True:
    temperature = sensor.ReadTemperature()
    print(f"T = {temperature}°C")
    
    temperatureF = round((temperature*1.8) + 32, 2)
    
    field_data = (temperature, temperatureF)
    thingspeak.WriteMultipleFields(field_data)
    
    sleep(20)