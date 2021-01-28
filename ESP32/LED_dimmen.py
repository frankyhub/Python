"""
Board: ESP32 R32
Funktion: Am Analogeingang GPIO39 das Poti anschliessen, der Dimmwert der internen LED wird in der Kommandozeile angezeigt
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
#khf 25.01.2021
"""
import machine
import sys
import utime
import time
pwm = machine.PWM(machine.Pin(2))
pwm.freq(60)

# Pin  Definition
adc_pin = machine.Pin(39)

# Erstellen eines ADC-Objekts fuer den PIN
adc = machine.ADC(adc_pin)

# 11 dB map
adc.atten(adc.ATTN_11DB)
while True:
    # Lade ADC
    val = adc.read()
    val = val/4
    print("Dimmwert: ", int(val))
    out = int(val)
    pwm.duty(out)
    time.sleep(0.1)
