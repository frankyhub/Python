"""
Board: ESP32 R32
Funktion:Interne LED blinkt
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
khf 25.01.2021

"""
from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
while True:
        led.value(not led.value())
        sleep(0.5)
