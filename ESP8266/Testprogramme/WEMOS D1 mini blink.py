#Wemos mini blink
#WEMOS D1 mini blink.py
#khf 24.01.2021
#http://docs.micropython.org/en/latest/esp8266/quickref.html
#Flash: esp8266-20200911-v1.13.bin

from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
while True:
        led.value(not led.value())
        sleep(0.5)