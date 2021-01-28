"""
Board: ESP32 R32
Funktion: Die interne LED pulst
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
#khf 25.01.2021

"""

import time
import machine
pwm = machine.PWM(machine.Pin(2))
pwm.freq(60)
while True:
    for i in range(1024):
        pwm.duty(i)
        time.sleep(0.001)
    for i in range(1023, -1, -1):
        pwm.duty(i)
        time.sleep(0.001)
