"""
Board: ESP32 R32
Funktion: Am Analogeingang GPIO39 Poti anschliessen, der Spannungswert wird in der Kommandozeile angezeigt
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
#khf 25.01.2021

"""
import machine
import sys
import utime

# Pin  Definition

adc_pin = machine.Pin(39)

# Erstellen eines ADC-Objekts fuer den PIN
adc = machine.ADC(adc_pin)

# 11 dB map fuer 0 - 3.3V range
adc.atten(adc.ATTN_11DB)

# Blink Schleife
while True:


    # Lade ADC und konvertiere in V
    val = adc.read()
    val = val * (3.3 / 4095)
    print(round(val,2), "V")
    # 1000ms Pause
    utime.sleep_ms(1000)
