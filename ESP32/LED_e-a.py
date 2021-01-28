"""
Board: ESP32 R32
Funktion:Interne LED ein/aus schalten
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
khf 25.01.2021

"""
#Intere LED EIN:
import machine
led = machine.Pin(2, machine.Pin.OUT)
led.value(1)

#Intere LED AUS:
import machine
led = machine.Pin(2, machine.Pin.OUT)
led.value(0)
