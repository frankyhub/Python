"""
Board: ESP32 R32
Funktion: main.py WEB-Server schaltete die interne LED (alternativ ein Relais) 
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
khf 25.01.2021

"""

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'R2-D2'
password = '2QK384JVPX'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Mit WLAN verbunden. IP-Adresse:')
print(station.ifconfig())

# ESP32 GPIO 26
relay = Pin(2, Pin.OUT)

# ESP8266 GPIO 5
#relay = Pin(5, Pin.OUT)
