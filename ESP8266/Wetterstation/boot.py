

# boot.py
import machine
from machine import Pin, I2C

import BME280
import network
import urequests
from time import sleep

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'R2-D2'
password = '2QK384JVPX'

api_key = 'bQZDfPulxRsRZW65I0AxgU'

ms_sleep_time = 600000

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)


while station.isconnected() == False:
  pass

print('Verbindung erfolgreich')
print(station.ifconfig())

def deep_sleep(msecs) :
  # RTC konfigurieren. ALARM0, um das Gerät zu aktivieren
  rtc = machine.RTC()
  rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

  # RTC einstellen. ALARM0 nach X Millisekunden feuern (Aufwachen des Geräts)
  rtc.alarm(rtc.ALARM0, msecs)

  # setze das Gerät in den Schlaf
  machine.deepsleep()

# ESP8266 - i2c Pins
i2c = I2C(scl=Pin(5),sda=Pin(4), freq=10000)

# ESP32 - i2c Pins
#i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)

try:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure 

  # Uncomment für Temperatur in Fahrenheit
  #temp = (bme.read_temperature()/100) * (9/5) + 32
  #temp = str(round(temp, 2)) + 'F'

  sensor_readings = {'value1':temp[:-1], 'value2':hum[:-1], 'value3':pres[:-3]}
  print(sensor_readings)

  request_headers = {'Content-Type': 'application/json'}

  request = urequests.post(
    'https://maker.ifttt.com/trigger/bme_280_readings/with/key/' + api_key,
    json=sensor_readings,
    headers=request_headers)
  print(request.text)
  request.close()

except OSError as e:
  print('Fehler beim Lesen oder Veröffentlichen der Sensorwerte.')

##sleep(3)

#ESP8266
#deep_sleep(ms_sleep_time)

#ESP32
#machine.deepsleep(ms_sleep_time)